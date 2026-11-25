import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_DIR = os.path.join(ROOT, "questions")
CODING_DIR = os.path.join(ROOT, "coding")
LECTURES_DIR = os.path.join(ROOT, "lectures")
JAVAC_TIMEOUT = 30
JAVA_TIMEOUT = 10

FENCE_RE = re.compile(r"```([^\n]*)\n(.*?)```", re.DOTALL)


def run(cmd, cwd, timeout):
    try:
        p = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout,
            encoding="utf-8", errors="replace",
        )
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"


def normalize(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in text.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def parse_expected(raw):
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    lines = raw.split("\n")
    exception = None
    if lines and lines[0].startswith("EXCEPTION="):
        exception = lines[0][len("EXCEPTION="):].strip()
        lines = lines[1:]
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    return exception, "\n".join(lines)


def find_exception_class(stderr):
    m = re.search(r'Exception in thread "[^"]*"\s+([\w.$]+)', stderr)
    if not m:
        m = re.search(r"([\w.$]+(?:Exception|Error))\s*:", stderr)
    if not m:
        return None
    return m.group(1).split(".")[-1]


def build_java_file(code):
    imports = []
    body_lines = []
    for ln in code.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if re.match(r"^\s*import\s", ln):
            imports.append(ln.strip())
        else:
            body_lines.append(ln)
    body = "\n".join(body_lines).strip("\n")
    m = re.search(r"\b(?:public\s+)?class\s+(\w+)", body)
    if m:
        cls = m.group(1)
        src = "\n".join(imports) + ("\n" if imports else "") + body + "\n"
        return f"{cls}.java", cls, src
    wrapped = "\n".join(imports)
    if wrapped:
        wrapped += "\n"
    wrapped += "public class Main {\n    public static void main(String[] args) {\n"
    wrapped += body + "\n    }\n}\n"
    return "Main.java", "Main", wrapped


def compile_and_run(tmp, src_name, main_class):
    rc, out, err = run(["javac", src_name], tmp, JAVAC_TIMEOUT)
    if rc != 0:
        tail = (err or out).strip().split("\n")[-3:]
        return None, "javac failed:\n    " + "\n    ".join(tail)
    rc, out, err = run(["java", main_class], tmp, JAVA_TIMEOUT)
    if rc != 0:
        exc = find_exception_class(err)
        return ("EXC", exc or f"exit {rc}"), None
    return "OK", normalize(out)


def verify_lecture(path):
    label = os.path.relpath(path, ROOT).replace(os.sep, "/")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    blocks = [(m.group(1).strip().lower(), m.group(2)) for m in FENCE_RE.finditer(text)]
    results = []
    i = 0
    while i < len(blocks):
        lang, code = blocks[i]
        if lang == "java run":
            expected = ""
            if i + 1 < len(blocks) and blocks[i + 1][0] == "output":
                expected = normalize(blocks[i + 1][1])
                i += 1
            else:
                results.append((label, False, "java run block without following output block"))
                i += 1
                continue
            fname, main_class, src = build_java_file(code)
            tmp = tempfile.mkdtemp(prefix="lv_")
            try:
                with open(os.path.join(tmp, fname), "w", encoding="utf-8", newline="\n") as f:
                    f.write(src)
                status, payload = compile_and_run(tmp, fname, main_class)
                if status is None:
                    results.append((label, False, payload))
                elif status == "EXC":
                    results.append((label, False,
                                    f"example threw {payload} but output block expects clean output"))
                elif payload != expected:
                    results.append((label, False,
                                    "output mismatch:\n--- expected ---\n" + expected +
                                    "\n--- actual ---\n" + payload))
                else:
                    results.append((label, True, "ok"))
            finally:
                shutil.rmtree(tmp, ignore_errors=True)
        i += 1
    if not results:
        results.append((label, True, "no java run examples"))
    return results


def verify_question(qdir, topic):
    name = os.path.basename(qdir)
    label = f"{topic}/{name}"
    if os.path.exists(os.path.join(qdir, "options.json")):
        return (label, True, "theory question (options.json, not machine-verified)")
    if not os.path.exists(os.path.join(qdir, "Main.java")):
        return (label, False, "missing Main.java and options.json")
    with open(os.path.join(qdir, "expected.txt"), encoding="utf-8") as f:
        raw_expected = f.read()
    is_compile_error = raw_expected.strip() == "COMPILE_ERROR"
    expected_exception, expected_out = parse_expected(raw_expected)

    tmp = tempfile.mkdtemp(prefix="qv_")
    try:
        src = os.path.join(qdir, "Main.java")
        dst = os.path.join(tmp, "Main.java")
        shutil.copy2(src, dst)
        rc, out, err = run(["javac", "Main.java"], tmp, JAVAC_TIMEOUT)
        if is_compile_error:
            if rc != 0:
                return (label, True, "compile error as expected")
            return (label, False, "expected COMPILE_ERROR but javac succeeded")
        if rc != 0:
            tail = (err or out).strip().split("\n")[-3:]
            return (label, False, "javac failed:\n    " + "\n    ".join(tail))

        rc, out, err = run(["java", "Main"], tmp, JAVA_TIMEOUT)
        actual = normalize(out)
        if rc != 0:
            exc = find_exception_class(err)
            if expected_exception is None:
                return (label, False,
                        f"runtime error (exit {rc}) but expected clean output.\nstderr tail:\n{err.strip()[-400:]}")
            want = expected_exception.split(".")[-1]
            if exc != want:
                return (label, False,
                        f"exception mismatch: expected {expected_exception}, got {exc or 'none'}\nstderr tail:\n{err.strip()[-400:]}")
            if normalize(expected_out) != actual:
                return (label, False,
                        "stdout mismatch (exception ok):\n--- expected ---\n" + normalize(expected_out) +
                        "\n--- actual ---\n" + actual)
            return (label, True, f"runtime exception {expected_exception} as expected")
        if expected_exception is not None:
            return (label, False,
                    f"expected exception {expected_exception} but program exited cleanly")
        want = normalize(expected_out)
        if actual != want:
            return (label, False,
                    "output mismatch:\n--- expected ---\n" + want +
                    "\n--- actual ---\n" + actual)
        return (label, True, "ok")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def verify_coding(cdir):
    name = os.path.basename(cdir)
    label = f"coding/{name}"
    files = [f for f in ("Solution.java", "Tests.java") if os.path.exists(os.path.join(cdir, f))]
    if "Solution.java" not in files or "Tests.java" not in files:
        return (label, False, "missing Solution.java or Tests.java")
    tmp = tempfile.mkdtemp(prefix="cv_")
    try:
        for f in files:
            shutil.copy2(os.path.join(cdir, f), os.path.join(tmp, f))
        rc, out, err = run(["javac"] + files, tmp, JAVAC_TIMEOUT)
        if rc != 0:
            tail = (err or out).strip().split("\n")[-3:]
            return (label, False, "javac failed:\n    " + "\n    ".join(tail))
        rc, out, err = run(["java", "Tests"], tmp, JAVA_TIMEOUT)
        text = out + err
        if rc != 0 or "FAIL" in text or "PASS" not in text:
            tail = text.strip().split("\n")[-8:]
            return (label, False, f"tests failed (exit {rc}):\n    " + "\n    ".join(tail))
        return (label, True, "all tests pass")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    results = []
    if os.path.isdir(QUESTIONS_DIR):
        for topic in sorted(os.listdir(QUESTIONS_DIR)):
            tdir = os.path.join(QUESTIONS_DIR, topic)
            if not os.path.isdir(tdir):
                continue
            for q in sorted(os.listdir(tdir)):
                qdir = os.path.join(tdir, q)
                if os.path.isdir(qdir):
                    results.append(verify_question(qdir, topic))
    if os.path.isdir(CODING_DIR):
        for p in sorted(os.listdir(CODING_DIR)):
            pdir = os.path.join(CODING_DIR, p)
            if os.path.isdir(pdir):
                results.append(verify_coding(pdir))
    if os.path.isdir(LECTURES_DIR):
        for lec in sorted(os.listdir(LECTURES_DIR)):
            ldir = os.path.join(LECTURES_DIR, lec)
            lfile = os.path.join(ldir, "lecture.md")
            if os.path.isdir(ldir) and os.path.exists(lfile):
                results.extend(verify_lecture(lfile))

    width = max(len(r[0]) for r in results) if results else 0
    failed = 0
    for label, ok, msg in results:
        mark = "PASS" if ok else "FAIL"
        print(f"{mark}  {label:<{width}}  {msg if not ok else ''}")
        if not ok:
            failed += 1
            print("    " + msg.replace("\n", "\n    "))
    print(f"\n{len(results) - failed}/{len(results)} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
