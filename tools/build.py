import html
import json
import os
import random
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_DIR = os.path.join(ROOT, "questions")
CODING_DIR = os.path.join(ROOT, "coding")
LECTURES_DIR = os.path.join(ROOT, "lectures")
GENERATED_DIR = os.path.join(ROOT, "generated")
DOCS_DIR = os.path.join(ROOT, "docs")

TOPIC_LABELS = {
    "inheritance": "وراثة و Constructor Chaining",
    "polymorphism": "Polymorphism",
    "static-final-this-super": "static و final و this و super",
    "abstract-interface": "Abstract Classes و Interfaces",
    "access-modifiers": "Access Modifiers و Packages",
    "exceptions": "Exceptions",
    "strings-equals": "String و equals و hashCode",
    "casting": "Casting و instanceof",
    "inner-classes": "Inner Classes و Enums",
    "collections": "Collections",
}


def norm(text):
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


def read_explanation(path):
    with open(path, encoding="utf-8") as f:
        text = f.read().strip()
    title = ""
    if text.startswith("# "):
        first, _, rest = text.partition("\n")
        title = first[2:].strip()
        text = rest.strip()
    return title, text


def lecture_id_for_topic(topic):
    if topic.startswith("lec"):
        return topic[3:]
    return None


def collect_lectures():
    lectures = []
    if not os.path.isdir(LECTURES_DIR):
        return lectures
    for d in sorted(os.listdir(LECTURES_DIR)):
        ldir = os.path.join(LECTURES_DIR, d)
        mpath = os.path.join(ldir, "meta.json")
        lpath = os.path.join(ldir, "lecture.md")
        if not (os.path.isdir(ldir) and os.path.exists(mpath) and os.path.exists(lpath)):
            continue
        with open(mpath, encoding="utf-8") as f:
            meta = json.load(f)
        with open(lpath, encoding="utf-8") as f:
            content = f.read()
        lectures.append({
            "id": d,
            "title_ar": meta.get("title_ar", d),
            "title_en": meta.get("title_en", ""),
            "order": meta.get("order", 999),
            "content": content,
        })
    lectures.sort(key=lambda l: (l["order"], l["id"]))
    return lectures


def collect_questions(lectures):
    lec_titles = {l["id"]: l["title_ar"] for l in lectures}
    questions = []
    if not os.path.isdir(QUESTIONS_DIR):
        return questions
    for topic in sorted(os.listdir(QUESTIONS_DIR)):
        tdir = os.path.join(QUESTIONS_DIR, topic)
        if not os.path.isdir(tdir):
            continue
        lec = lecture_id_for_topic(topic)
        for q in sorted(os.listdir(tdir)):
            qdir = os.path.join(tdir, q)
            if not os.path.isdir(qdir):
                continue
            title, explanation = read_explanation(os.path.join(qdir, "explanation.md"))
            entry = {
                "id": f"{topic}/{q}",
                "topic": topic,
                "lecture": lec,
                "topicLabel": lec_titles.get(lec, TOPIC_LABELS.get(topic, topic)),
                "q": q,
                "title": title,
                "explanation": explanation,
            }
            opath = os.path.join(qdir, "options.json")
            if os.path.exists(opath):
                with open(opath, encoding="utf-8") as f:
                    opts = json.load(f)
                options = opts.get("options", [])
                answer = opts.get("answer", 0)
                if not isinstance(answer, int) or not (0 <= answer < len(options)):
                    raise ValueError(f"bad answer index in {qdir}")
                entry.update({
                    "code": "", "expected": "", "exception": None,
                    "compileError": False, "options": options,
                    "answerIndex": answer, "theory": True,
                })
            else:
                with open(os.path.join(qdir, "Main.java"), encoding="utf-8") as f:
                    code = f.read()
                with open(os.path.join(qdir, "expected.txt"), encoding="utf-8") as f:
                    raw_expected = f.read()
                exception, expected = parse_expected(raw_expected)
                compile_error = raw_expected.strip() == "COMPILE_ERROR"
                entry.update({
                    "code": code, "expected": expected, "exception": exception,
                    "compileError": compile_error, "options": None,
                    "answerIndex": None, "theory": False,
                })
            questions.append(entry)
    return questions


def collect_coding():
    problems = []
    if not os.path.isdir(CODING_DIR):
        return problems
    for p in sorted(os.listdir(CODING_DIR)):
        pdir = os.path.join(CODING_DIR, p)
        if not os.path.isdir(pdir):
            continue
        entry = {"id": p, "name": p.replace("-", " ")}
        for fname, key in (("problem.md", "problem"), ("Starter.java", "starter"),
                           ("Solution.java", "solution"), ("Tests.java", "tests")):
            path = os.path.join(pdir, fname)
            if os.path.exists(path):
                with open(path, encoding="utf-8") as f:
                    entry[key] = f.read()
        problems.append(entry)
    return problems


def answer_text(q):
    if q["compileError"]:
        return "COMPILE_ERROR"
    if q["exception"]:
        return f"EXCEPTION={q['exception']}\n{q['expected']}"
    return q["expected"]


def md_escape_code(code):
    return "```java\n" + code.rstrip("\n") + "\n```"


def generate_lecture_markdown(lectures, questions):
    os.makedirs(os.path.join(GENERATED_DIR, "lectures"), exist_ok=True)
    by_lec = {}
    for q in questions:
        if q["lecture"]:
            by_lec.setdefault(q["lecture"], []).append(q)
    index_lines = ["# أسئلة الامتحان حسب المحاضرة\n"]
    for lec in lectures:
        qs = by_lec.get(lec["id"], [])
        lines = [lec["content"].rstrip("\n"), "", "## الأسئلة\n"]
        for i, q in enumerate(qs, 1):
            heading = q["title"] or q["q"]
            lines.append(f"### سؤال {i}: {heading}\n")
            if q["options"]:
                for j, opt in enumerate(q["options"]):
                    mark = " ✔" if j == q["answerIndex"] else ""
                    lines.append(f"{j + 1}. {opt}{mark}")
                lines.append("")
            else:
                lines.append(md_escape_code(q["code"]))
                lines.append("")
            lines.append("<details>")
            lines.append("<summary>الإجابة</summary>\n")
            if q["options"]:
                lines.append(f"**الإجابة:** {q['options'][q['answerIndex']]}\n")
            elif q["compileError"]:
                lines.append("**COMPILE_ERROR** — الكود ده مش بيترجم.\n")
            else:
                lines.append("**الناتج:**\n")
                lines.append("```")
                lines.append(q["expected"] if q["expected"] else "(مفيش output)")
                lines.append("```")
                if q["exception"]:
                    lines.append(f"\nبيرمي `{q['exception']}`\n")
            lines.append("")
            lines.append(q["explanation"])
            lines.append("</details>\n")
        with open(os.path.join(GENERATED_DIR, "lectures", f"{lec['id']}.md"), "w",
                  encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines))
        index_lines.append(f"- [محاضرة {lec['order']}: {lec['title_ar']}"
                           f" ({lec['title_en']})](generated/lectures/{lec['id']}.md) — {len(qs)} سؤال")
    with open(os.path.join(GENERATED_DIR, "lectures", "README.md"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write("\n".join(index_lines) + "\n")


def generate_topic_markdown(questions):
    os.makedirs(GENERATED_DIR, exist_ok=True)
    by_topic = {}
    for q in questions:
        if q["lecture"]:
            continue
        by_topic.setdefault(q["topic"], []).append(q)
    index_lines = ["# أسئلة امتحان Java OOP\n",
                   "كل إجابة هنا متأكد منها فعليًا — السكريبت `tools/verify.py` بيترجم ويشغّل كل سؤال ويقارن الناتج.\n"]
    for topic in sorted(by_topic):
        qs = by_topic[topic]
        fname = os.path.join(GENERATED_DIR, f"{topic}.md")
        label = TOPIC_LABELS.get(topic, topic)
        lines = [f"# {label}\n"]
        for i, q in enumerate(qs, 1):
            heading = q["title"] or f"{q['q']}"
            lines.append(f"## {i}. {heading}\n")
            lines.append(md_escape_code(q["code"]))
            lines.append("")
            lines.append("<details>")
            lines.append(f"<summary>الإجابة</summary>\n")
            if q["compileError"]:
                lines.append("**COMPILE_ERROR** — الكود ده مش بيترجم.\n")
            else:
                lines.append("**الناتج:**\n")
                lines.append("```")
                lines.append(q["expected"] if q["expected"] else "(مفيش output)")
                lines.append("```")
                if q["exception"]:
                    lines.append(f"\nبيرمي `{q['exception']}`\n")
            lines.append("")
            lines.append(q["explanation"])
            lines.append("</details>\n")
        with open(fname, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines))
        index_lines.append(f"- [{label}](generated/{topic}.md) — {len(qs)} سؤال")
    with open(os.path.join(GENERATED_DIR, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(index_lines) + "\n")


SITE_TEMPLATE = r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Java OOP Exam Kit — كويز</title>
<style>
:root{
--bg:#0a0f1e;--bg2:#0d1526;--panel:rgba(21,29,50,.78);--panel2:#16203a;--code:#070c18;
--border:rgba(255,255,255,.09);--border-g:rgba(255,200,61,.35);
--text:#eef2ff;--muted:#93a0c2;
--gold:#FFC83D;--gold2:#F5A623;--on-gold:#201503;--gold-soft:rgba(255,200,61,.12);
--good:#3ddc97;--bad:#ff7b72;
--kw:#d0a2f7;--typ:#7cc7ff;--str:#9ece8a;--num:#fbbf24;--com:#5f6f96;--ann:#f472b6;
--shadow:0 10px 30px rgba(0,0,0,.35);color-scheme:dark}
@media (prefers-color-scheme:light){:root:not([data-theme="dark"]){
--bg:#f6f3ec;--bg2:#fffdf8;--panel:rgba(255,255,255,.88);--panel2:#ffffff;--code:#f2efe4;
--border:rgba(30,40,80,.13);--border-g:rgba(180,130,10,.4);
--text:#20294d;--muted:#5a6390;
--gold:#d99a12;--gold2:#b97f00;--on-gold:#fffdf5;--gold-soft:rgba(245,166,35,.16);
--good:#15803d;--bad:#b91c1c;
--kw:#7c3aed;--typ:#0369a1;--str:#15803d;--num:#b45309;--com:#8a94b8;--ann:#db2777;
--shadow:0 10px 30px rgba(60,50,10,.12);color-scheme:light}}
:root[data-theme="light"]{
--bg:#f6f3ec;--bg2:#fffdf8;--panel:rgba(255,255,255,.88);--panel2:#ffffff;--code:#f2efe4;
--border:rgba(30,40,80,.13);--border-g:rgba(180,130,10,.4);
--text:#20294d;--muted:#5a6390;
--gold:#d99a12;--gold2:#b97f00;--on-gold:#fffdf5;--gold-soft:rgba(245,166,35,.16);
--good:#15803d;--bad:#b91c1c;
--kw:#7c3aed;--typ:#0369a1;--str:#15803d;--num:#b45309;--com:#8a94b8;--ann:#db2777;
--shadow:0 10px 30px rgba(60,50,10,.12);color-scheme:light}
*{box-sizing:border-box}
html{scrollbar-color:var(--gold2) var(--bg)}
body{margin:0;color:var(--text);font-family:"Segoe UI",Tahoma,Arial,sans-serif;line-height:1.7;
background:
radial-gradient(640px 320px at 88% -6%,rgba(245,166,35,.13),transparent 62%),
radial-gradient(720px 380px at 4% 0%,rgba(56,110,246,.11),transparent 60%),
linear-gradient(180deg,var(--bg2),var(--bg) 30%);
background-attachment:fixed;min-height:100vh}
.wrap{max-width:920px;margin:0 auto;padding:20px 16px 40px}
.site-head{display:flex;align-items:center;gap:14px;margin:20px 0 4px}
.logo{width:48px;height:48px;flex:0 0 auto;border-radius:13px;border:1.5px solid var(--gold);background:var(--gold-soft);color:var(--gold);display:flex;align-items:center;justify-content:center}
.logo svg{width:24px;height:24px}
.site-head h1{font-size:1.35rem;margin:0;display:flex;align-items:center;gap:9px;letter-spacing:.2px}
.bolt{width:20px;height:20px;color:var(--gold);flex:0 0 auto}
.sub{color:var(--muted);font-size:.9rem;margin:3px 0 0}
.controls{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:16px 0 4px}
.selwrap{position:relative;display:inline-flex;align-items:center}
select{appearance:none;-webkit-appearance:none;background:var(--panel);color:var(--text);border:1px solid var(--border);border-radius:999px;padding:10px 36px 10px 16px;font-size:.95rem;cursor:pointer;min-height:44px;font-family:inherit;backdrop-filter:blur(6px)}
.selwrap .chev{position:absolute;inset-inline-end:12px;width:14px;height:14px;pointer-events:none;color:var(--muted)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:var(--panel);color:var(--text);border:1px solid var(--border);border-radius:999px;padding:10px 18px;cursor:pointer;font-size:.95rem;font-family:inherit;min-height:44px;transition:border-color .15s,filter .15s,transform .1s,box-shadow .15s;backdrop-filter:blur(6px)}
.btn:hover{border-color:var(--gold)}
.btn:active{transform:translateY(1px)}
.btn svg{width:16px;height:16px;flex:0 0 auto}
.btn.primary{background:linear-gradient(135deg,var(--gold),var(--gold2));color:var(--on-gold);border:none;font-weight:700;box-shadow:0 0 20px rgba(245,166,35,.35)}
.btn.primary:hover{filter:brightness(1.1);border:none}
.btn:disabled{opacity:.5;cursor:not-allowed;transform:none;box-shadow:none}
button:focus-visible,.btn:focus-visible,select:focus-visible,.opt:focus-visible,textarea:focus-visible,.codex:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.barwrap{display:flex;align-items:center;gap:12px;margin:8px 0 6px}
.bar{flex:1;height:6px;background:var(--panel2);border:1px solid var(--border);border-radius:99px;overflow:hidden}
.bar>div{height:100%;background:linear-gradient(90deg,var(--gold),var(--gold2));width:0;transition:width .3s}
.scorechip{display:inline-flex;align-items:center;gap:6px;background:var(--gold-soft);border:1px solid var(--border-g);color:var(--gold);border-radius:99px;padding:4px 13px;font-size:.85rem;font-weight:700;white-space:nowrap}
.scorechip svg{width:14px;height:14px}
.card{background:var(--panel);border:1px solid var(--border);border-radius:18px;padding:20px;margin:14px 0;box-shadow:var(--shadow);backdrop-filter:blur(8px)}
.tags{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}
.tag{background:var(--gold-soft);border:1px solid var(--border-g);color:var(--gold);border-radius:99px;padding:3px 12px;font-size:.8rem;font-weight:700}
.codewin{background:var(--code);border:1px solid var(--border);border-radius:14px;margin:12px 0;overflow:hidden;direction:ltr;text-align:left}
.codebar{display:flex;align-items:center;gap:6px;padding:8px 12px;border-bottom:1px solid var(--border)}
.dot{width:11px;height:11px;border-radius:50%;flex:0 0 auto}
.dot.r{background:#ff5f57}.dot.y{background:#febc2e}.dot.g{background:#28c840}
.codex{margin-inline-start:auto;background:none;border:0;color:var(--muted);cursor:pointer;padding:5px;border-radius:7px;display:inline-flex;align-items:center}
.codex:hover{color:var(--gold);background:var(--gold-soft)}
.codex svg{width:15px;height:15px}
.codelines{overflow-x:auto;padding:10px 0;font-family:Consolas,Menlo,monospace;font-size:.85rem;line-height:1.55}
.cl{display:flex;min-width:max-content}
.ln{flex:0 0 auto;width:2.6em;text-align:right;padding:0 14px 0 12px;color:var(--muted);opacity:.65;user-select:none}
.cl code{white-space:pre;padding-inline-end:16px}
.kw{color:var(--kw)}.str{color:var(--str)}.num{color:var(--num)}.com{color:var(--com);font-style:italic}.typ{color:var(--typ)}.ann{color:var(--ann)}
pre.code{background:var(--code);border:1px solid var(--border);border-radius:10px;padding:12px 14px;overflow-x:auto;direction:ltr;text-align:left;font-family:Consolas,Menlo,monospace;font-size:.85rem;line-height:1.55;margin:8px 0;color:var(--text)}
.opts{display:flex;flex-direction:column;gap:10px;margin:16px 0}
.opts.row{flex-direction:row;flex-wrap:wrap}
.opt{display:flex;align-items:center;gap:10px;background:var(--panel2);border:1px solid var(--border);border-radius:12px;padding:12px 16px;cursor:pointer;font-size:1rem;min-height:44px;transition:border-color .15s,background .15s;backdrop-filter:blur(4px)}
.opt:hover{border-color:var(--gold)}
.opt.sel{border-color:var(--gold);background:var(--gold-soft)}
.opt.right{border-color:var(--good);background:rgba(61,220,151,.12);color:var(--good)}
.opt.wrong{border-color:var(--bad);background:rgba(255,123,114,.1);color:var(--bad)}
textarea{width:100%;background:var(--code);color:var(--text);border:1px solid var(--border);border-radius:12px;padding:12px;font-family:Consolas,Menlo,monospace;direction:ltr;text-align:left;min-height:96px;font-size:.95rem;resize:vertical}
textarea:focus{border-color:var(--gold);outline:none}
.instr{color:var(--muted);font-size:.9rem;margin-bottom:8px}
.instr span[dir="ltr"]{unicode-bidi:isolate}
.feedback{border-radius:12px;padding:12px 14px;margin:14px 0;display:none;font-weight:600}
.feedback.ok{display:flex;align-items:center;gap:8px;background:rgba(61,220,151,.1);border:1px solid rgba(61,220,151,.4);color:var(--good)}
.feedback.no{display:flex;align-items:center;gap:8px;background:rgba(255,123,114,.08);border:1px solid rgba(255,123,114,.4);color:var(--bad)}
.feedback svg{width:17px;height:17px;flex:0 0 auto}
.expl{background:var(--panel2);border:1px dashed var(--border-g);border-radius:12px;padding:14px;margin-top:12px;display:none}
.expl.show{display:block}
.cardfoot{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:16px;flex-wrap:wrap}
.actions{display:flex;gap:10px;flex-wrap:wrap}
.themewrap{position:relative;display:inline-flex;align-items:center;gap:8px;color:var(--gold)}
.themewrap>svg{width:16px;height:16px;flex:0 0 auto}
.themepill{appearance:none;background:var(--panel2);border:1px solid var(--border);border-radius:999px;color:var(--text);font-family:inherit;font-size:.9rem;padding:9px 30px 9px 14px;min-height:44px;cursor:pointer}
.themewrap .chev{position:absolute;inset-inline-end:10px;width:14px;height:14px;pointer-events:none;color:var(--muted)}
.fsmodal{position:fixed;inset:0;background:rgba(4,8,18,.8);display:flex;align-items:center;justify-content:center;z-index:60;padding:16px}
.fsbox{width:min(1000px,96vw);height:min(82vh,760px);display:flex;flex-direction:column;background:var(--panel);border:1px solid var(--border);border-radius:16px;overflow:hidden;box-shadow:var(--shadow)}
.fsbar{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 14px;border-bottom:1px solid var(--border)}
.fsbody{flex:1;overflow:auto}
.muted{color:var(--muted);font-size:.9rem}
.explain-panel{max-height:70vh;overflow-y:auto}
.explain-panel h1,.explain-panel h2,.explain-panel h3,.explain-panel h4{margin:.8em 0 .3em;font-size:1.1rem}
.explain-panel p{margin:.5em 0}
.explain-panel ul{margin:.5em 0;padding-inline-start:1.4em}
.explain-panel table{border-collapse:collapse;width:100%;margin:.7em 0;font-size:.9rem}
.explain-panel th,.explain-panel td{border:1px solid var(--border);padding:5px 9px;text-align:right}
.explain-panel th{background:var(--panel2)}
.explain-panel code{background:var(--panel2);border:1px solid var(--border);border-radius:4px;padding:0 4px;font-family:Consolas,monospace;font-size:.85em;direction:ltr;unicode-bidi:embed}
.explain-panel pre.code{text-align:left}
.nazri{display:inline-block;background:var(--gold-soft);border:1px solid var(--border-g);color:var(--gold);border-radius:99px;padding:3px 12px;font-size:.8rem;font-weight:700}
@media (max-width:640px){
.wrap{padding:12px 10px 32px}
.controls{display:grid;grid-template-columns:1fr 1fr}
.controls .btn{width:100%}
.selwrap{width:100%}
select{width:100%}
#explainBtn{grid-column:1/-1}
.opts.row{flex-direction:column}
.opts.row .opt{width:100%}
.cardfoot{flex-direction:column;align-items:stretch}
.actions{flex-direction:column}
.actions .btn{width:100%}
.card{padding:16px;border-radius:14px}
.site-head h1{font-size:1.15rem}
}
</style>
</head>
<body>
<div class="wrap">
<header class="site-head">
<span class="logo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/><line x1="12" y1="4" x2="12" y2="20"/></svg></span>
<div><h1><svg class="bolt" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" fill="currentColor"/></svg>Java OOP Exam Kit</h1>
<div class="sub">كويز تفاعلي — الإجابات متأكد منها بتشغيل الكود فعليًا.</div></div>
</header>
<div class="controls">
<span class="selwrap"><select id="lecSel"></select><svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
<span class="selwrap"><select id="topicSel"></select><svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
<button id="explainBtn" class="btn" style="display:none" dir="ltr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>Read Explanation</button>
<button id="shuffleBtn" class="btn" dir="ltr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/><line x1="4" y1="4" x2="9" y2="9"/></svg>Shuffle</button>
<button id="reviewBtn" class="btn" dir="ltr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>Review Wrong</button>
<button id="resetBtn" class="btn" dir="ltr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2z"/></svg>Reset Score</button>
</div>
<div class="barwrap"><div class="bar"><div id="barFill"></div></div><span class="scorechip"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg><span id="scoreLabel"></span></span></div>
<div id="explainWrap" style="display:none"><div class="card explain-panel" id="explainCard"></div></div>
<div id="quizArea"></div>
</div>
<div id="fsModal" class="fsmodal" style="display:none"><div class="fsbox"><div class="fsbar"><span class="muted" dir="ltr">Code</span><button class="btn" id="fsClose" dir="ltr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>Close (Esc)</button></div><div class="fsbody" id="fsBody"></div></div></div>
<script>
const DATA = __DATA__;
const KEY = "javaOopQuizV1";
function loadState(){
  try{
    const raw = JSON.parse(localStorage.getItem(KEY) || "null");
    if(!raw || typeof raw !== "object") return {answers:{}, order:[], reviewOnly:false};
    const validIds = new Set(DATA.questions.map(q=>q.id));
    const answers = {};
    if(raw.answers && typeof raw.answers === "object"){
      for(const id of Object.keys(raw.answers)){
        const a = raw.answers[id];
        if(validIds.has(id) && a && typeof a === "object" && typeof a.correct === "boolean") answers[id] = a;
      }
    }
    const order = Array.isArray(raw.order) ? raw.order.filter(id=>validIds.has(id)) : [];
    return {answers, order, reviewOnly: !!raw.reviewOnly};
  }catch(e){ return {answers:{}, order:[], reviewOnly:false}; }
}
let state = loadState();
function save(){ localStorage.setItem(KEY, JSON.stringify(state)); }
function answerText(q){
  if(q.options) return q.options[q.answerIndex];
  if(q.compileError) return "COMPILE_ERROR";
  if(q.exception) return "EXCEPTION=" + q.exception + "\n" + q.expected;
  return q.expected;
}
const $ = id => document.getElementById(id);
const norm = s => (s||"").replace(/\r\n/g,"\n").replace(/\r/g,"\n").split("\n").map(l=>l.replace(/\s+$/,"")).join("\n").replace(/\n+$/,"");
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
const KEYWORDS = new Set(("abstract assert boolean break byte case catch char class const continue default do double else enum extends final finally float for goto if implements import instanceof int interface long native new package private protected public return short static strictfp super switch synchronized this throw throws transient try void volatile while var record sealed permits yield").split(" "));
function highlight(src){
  let out="", i=0, n=src.length;
  const token=(re)=>{const m=src.slice(i).match(re); if(m){out+=m[0]; i+=m[0].length; return true;} return false;};
  while(i<n){
    if(src.startsWith("//",i)){const e=src.indexOf("\n",i); const t=e<0?src.slice(i):src.slice(i,e); out+='<span class="com">'+esc(t)+'</span>'; i+=t.length; continue;}
    if(src.startsWith("/*",i)){const e=src.indexOf("*/",i+2); const t=e<0?src.slice(i):src.slice(i,e+2); out+='<span class="com">'+esc(t)+'</span>'; i+=t.length; continue;}
    if(src[i]==='"'||src[i]==="'"){const q=src[i]; let j=i+1; while(j<n){if(src[j]==="\\"){j+=2;continue;} if(src[j]===q){j++;break;} if(src[j]==="\n")break; j++;} out+='<span class="str">'+esc(src.slice(i,j))+'</span>'; i=j; continue;}
    if(/[0-9]/.test(src[i])){const m=src.slice(i).match(/^[0-9][\w.]*/); out+='<span class="num">'+m[0]+'</span>'; i+=m[0].length; continue;}
    if(/[A-Za-z_$]/.test(src[i])){const m=src.slice(i).match(/^[A-Za-z_$][\w$]*/); const w=m[0];
      let cls=""; if(KEYWORDS.has(w)) cls="kw"; else if(["String","System","Object","Integer","Exception","RuntimeException","Override","Deprecated","SuppressWarnings","FunctionalInterface","SafeVarargs","Test"].includes(w)) cls="typ";
      out+=(cls?'<span class="'+cls+'">'+w+'</span>':w); i+=w.length; continue;}
    out+=esc(src[i]); i++;
  }
  return out;
}
function mdInline(s){
  s=esc(s);
  s=s.replace(/\*\*([^*]+)\*\*/g,"<b>$1</b>");
  s=s.replace(/`([^`]+)`/g,"<code>$1</code>");
  return s;
}
function renderMd(src){
  const lines=src.replace(/\r\n/g,"\n").replace(/\r/g,"\n").split("\n");
  const isTable=l=>/^\s*\|.*\|\s*$/.test(l);
  const isSep=r=>/^[\s|:\-]+$/.test(r.trim());
  const cells=r=>r.trim().replace(/^\|/,"").replace(/\|$/,"").split("|").map(c=>c.trim());
  let out="",i=0;
  while(i<lines.length){
    const l=lines[i];
    if(/^```/.test(l)){
      const lang=l.slice(3).trim();let buf=[];i++;
      while(i<lines.length&&!/^```/.test(lines[i])){buf.push(lines[i]);i++;}
      i++;const code=buf.join("\n");
      out+='<pre class="code"><code>'+(lang==="output"?esc(code):highlight(code))+'</code></pre>';continue;
    }
    if(/^#{1,4}\s/.test(l)){
      const lv=l.match(/^#+/)[0].length;
      out+="<h"+(lv+1)+">"+mdInline(l.replace(/^#+\s*/,""))+"</h"+(lv+1)+">";i++;continue;
    }
    if(isTable(l)){
      const rows=[];
      while(i<lines.length&&isTable(lines[i])){rows.push(lines[i]);i++;}
      const head=cells(rows[0]);
      const body=rows.slice(1).filter(r=>!isSep(r));
      out+="<table><thead><tr>"+head.map(c=>"<th>"+mdInline(c)+"</th>").join("")+"</tr></thead><tbody>";
      body.forEach(r=>{out+="<tr>"+cells(r).map(c=>"<td>"+mdInline(c)+"</td>").join("")+"</tr>";});
      out+="</tbody></table>";continue;
    }
    if(/^\s*[-*]\s+/.test(l)){
      out+="<ul>";
      while(i<lines.length&&/^\s*[-*]\s+/.test(lines[i])){out+="<li>"+mdInline(lines[i].replace(/^\s*[-*]\s+/,""))+"</li>";i++;}
      out+="</ul>";continue;
    }
    if(l.trim()===""){i++;continue;}
    const buf=[];
    while(i<lines.length&&lines[i].trim()!==""&&!/^```|^#{1,4}\s|^\s*[-*]\s+/.test(lines[i])&&!isTable(lines[i])){buf.push(lines[i]);i++;}
    out+="<p>"+mdInline(buf.join(" "))+"</p>";
  }
  return out;
}
const ICONS={
check:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
x:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
expand:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3"/><path d="M21 8V5a2 2 0 0 0-2-2h-3"/><path d="M3 16v3a2 2 0 0 0 2 2h3"/><path d="M16 21h3a2 2 0 0 0 2-2v-3"/></svg>'};
let lastCode="";
function codeBlock(src){
  lastCode=src;
  const lines=src.replace(/\r\n/g,"\n").replace(/\r/g,"\n").replace(/\n+$/,"").split("\n");
  let h='<div class="codewin"><div class="codebar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span><button class="codex" dir="ltr" title="Expand">'+ICONS.expand+'</button></div><div class="codelines">';
  lines.forEach((ln,i)=>{h+='<div class="cl"><span class="ln">'+(i+1)+'</span><code>'+(highlight(ln)||" ")+'</code></div>';});
  return h+'</div></div>';
}
function correctPick(q){
  if(q.options) return String(q.answerIndex);
  if(q.compileError) return "compile";
  if(q.exception) return "exc";
  return null;
}
function optCls(q,pick,ans,answered){
  let c="opt";
  if(!answered) return c;
  const cp=correctPick(q);
  if(cp!==null&&String(pick)===cp) c+=" right";
  if(ans&&String(ans.pick)===String(pick)) c+=ans.correct?" sel":" wrong";
  return c;
}
function openFs(){
  if(!lastCode) return;
  $("fsBody").innerHTML=codeBlock(lastCode);
  bindCodex($("fsBody"));
  $("fsModal").style.display="flex";
}
function closeFs(){$("fsModal").style.display="none";}
function bindCodex(root){
  root.querySelectorAll(".codex").forEach(b=>{b.onclick=openFs;});
}
function initTheme(){
  let saved="";
  try{saved=localStorage.getItem("javaOopThemeV1")||"";}catch(e){}
  const sel=$("themeSel");
  if(sel){
    if(saved==="dark"||saved==="light") document.documentElement.dataset.theme=saved;
    else delete document.documentElement.dataset.theme;
    sel.value=saved==="dark"||saved==="light"?saved:"";
    sel.onchange=()=>{
      const v=sel.value;
      try{localStorage.setItem("javaOopThemeV1",v);}catch(e){}
      if(v) document.documentElement.dataset.theme=v; else delete document.documentElement.dataset.theme;
    };
  }
}
function filtered(){
  const lec=$("lecSel").value, t=$("topicSel").value;
  let qs=DATA.questions;
  if(lec) qs=qs.filter(q=>q.lecture===lec);
  else if(t) qs=qs.filter(q=>q.topic===t);
  if(state.reviewOnly){qs=qs.filter(q=>state.answers[q.id]&&!state.answers[q.id].correct);}
  return qs;
}
function renderTopics(){
  const sel=$("topicSel"); sel.innerHTML="";
  const all=document.createElement("option"); all.value=""; all.textContent="All Topics ("+DATA.questions.length+")"; sel.appendChild(all);
  const counts={}; DATA.questions.forEach(q=>{if(!q.lecture)counts[q.topic]=(counts[q.topic]||0)+1;});
  Object.keys(counts).sort().forEach(t=>{const o=document.createElement("option");o.value=t;o.textContent=DATA.topics[t]+" ("+counts[t]+")";sel.appendChild(o);});
}
function renderLectures(){
  const sel=$("lecSel"); sel.innerHTML="";
  const none=document.createElement("option"); none.value=""; none.textContent="All Lectures"; sel.appendChild(none);
  const counts={}; DATA.questions.forEach(q=>{if(q.lecture)counts[q.lecture]=(counts[q.lecture]||0)+1;});
  DATA.lectures.forEach(l=>{const o=document.createElement("option");o.value=l.id;o.textContent="Lecture "+l.order+": "+l.title_ar+" ("+(counts[l.id]||0)+")";sel.appendChild(o);});
}
function toggleExplain(){
  $("explainBtn").style.display=$("lecSel").value?"":"none";
}
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function start(){
  state.reviewOnly=false; save();
  const qs=filtered(); state.order=qs.map(q=>q.id); state.cur=0; state.phase="ask"; save(); draw();
}
function draw(){
  const area=$("quizArea");
  if(!state.order.length){
    area.innerHTML='<div class="card muted">No questions in this selection.</div>';
    return;
  }
  if(state.cur>=state.order.length) state.cur=0;
  const id=state.order[state.cur]; const q=DATA.questions.find(x=>x.id===id);
  if(!q){ state.order=state.order.filter(x=>x!==id); draw(); return; }
  const answered=!!state.answers[id];
  const ans=state.answers[id];
  const mode=q.options?"mcq":(q.compileError?"choice":(q.exception?"exc":"output"));
  const pos=state.order.indexOf(id)+1;
  const cp=correctPick(q);
  let html='<div class="card"><div class="tags"><span class="tag">Question '+pos+' of '+state.order.length+'</span><span class="tag">'+esc(q.topicLabel)+'</span>'+(q.theory?'<span class="tag nazri">Theory</span>':"")+(q.title?'<span class="tag">'+esc(q.title)+'</span>':"")+'</div>';
  if(q.code) html+=codeBlock(q.code);
  if(mode==="mcq"){
    html+='<div class="opts">';
    q.options.forEach((t,i)=>{
      html+='<div class="'+optCls(q,i,ans,answered)+'" data-idx="'+i+'" dir="auto">'+esc(t)+'</div>';
    });
    html+='</div>';
  } else if(mode==="choice"){
    html+='<div class="opts">';
    [["compile","Compile Error"],["run","Compiles &amp; Runs"]].forEach(([p,t])=>{
      html+='<div class="'+optCls(q,p,ans,answered)+'" data-pick="'+p+'" dir="ltr">'+t+'</div>';
    });
    html+='</div>';
  } else if(mode==="exc"){
    html+='<div class="opts">';
    [["exc","Throws Runtime Exception"],["compile","Compile Error"],["run","Runs Normally"]].forEach(([p,t])=>{
      html+='<div class="'+optCls(q,p,ans,answered)+'" data-pick="'+p+'" dir="ltr">'+t+'</div>';
    });
    html+='</div>';
    html+='<div class="instr">لو اخترت <span dir="ltr">Runtime Exception</span> اسم الـ Exception هيظهر في الإجابة تحت.</div>';
  } else {
    html+='<div class="instr">اكتب الناتج اللي هيطبعه البرنامج (<span dir="ltr">stdout</span>). لو بيقع بـ <span dir="ltr">Runtime Exception</span> اختار الزرار.</div>';
    html+='<textarea id="ansBox" dir="ltr" placeholder="Output here..."></textarea>';
    html+='<div class="opts row">';
    html+='<div class="'+optCls(q,"exc",ans,answered)+'" data-pick="exc" dir="ltr">Runtime Exception</div>';
    html+='<div class="'+optCls(q,"compile",ans,answered)+'" data-pick="compile" dir="ltr">Compile Error</div>';
    html+='</div>';
  }
  html+='<div class="cardfoot"><span class="themewrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg><select id="themeSel" class="themepill"><option value="">Auto</option><option value="dark">Dark</option><option value="light">Light</option></select><svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>';
  html+='<div class="actions">';
  if(mode==="output") html+='<button class="btn primary" id="checkBtn" dir="ltr"'+(answered?" disabled":"")+'>Check</button>';
  html+='<button class="btn" id="nextBtn" dir="ltr"'+(answered?"":" disabled")+'>Next</button></div></div>';
  html+='<div class="feedback" id="fb"></div>';
  html+='<div class="expl'+(answered?" show":"")+'" id="expl">';
  html+='<b>Correct answer:</b><pre class="code" style="margin:8px 0"><code>'+esc(answerText(q))+'</code></pre>';
  html+='<div>'+esc(q.explanation)+'</div></div>';
  html+='</div>';
  area.innerHTML=html;
  initTheme();
  bindCodex(area);
  const fb=$("fb");
  if(answered){
    fb.className="feedback "+(ans.correct?"ok":"no");
    fb.innerHTML=(ans.correct?ICONS.check:ICONS.x)+(ans.correct?"Correct!":"Wrong — see the answer below.");
  }
  area.querySelectorAll(".opt").forEach(o=>{
    if(answered) return;
    o.onclick=()=>{
      const pick=o.dataset.idx!==undefined?o.dataset.idx:o.dataset.pick;
      if(mode==="output"&&pick==="exc"){
        submitOutput(q,"exc"); return;
      }
      if(mode==="output"&&pick==="compile"){
        submitOutput(q,"compile"); return;
      }
      grade(q,pick,null);
    };
  });
  const cb=$("checkBtn");
  if(cb) cb.onclick=()=>submitOutput(q,"text");
  if(!answered&&mode==="output"){
    const box=$("ansBox"); box.addEventListener("keydown",e=>{if(e.key==="Enter"&&(e.ctrlKey||e.metaKey))submitOutput(q,"text");});
  }
  const nb=$("nextBtn");
  if(nb) nb.onclick=()=>{state.cur++; if(state.cur>=state.order.length){state.cur=0;} save(); draw();};
  updateScore();
}
function submitOutput(q,kind){
  const txt=$("ansBox")?$("ansBox").value:"";
  let correct=false;
  if(kind==="exc") correct=!!q.exception;
  else if(kind==="compile") correct=q.compileError;
  else {
    correct=!q.compileError&&!q.exception&&norm(txt)===norm(q.expected);
  }
  grade(q,kind,txt,correct);
}
function grade(q,pick,typed,precomputed){
  const id=q.id;
  let correct;
  if(precomputed!==undefined) correct=precomputed;
  else if(q.options) correct=String(pick)===String(q.answerIndex);
  else if(pick==="compile") correct=q.compileError;
  else if(pick==="exc") correct=!!q.exception;
  else if(pick==="run") correct=!q.compileError&&!q.exception;
  else correct=false;
  state.answers[id]={correct,pick,typed:typed||""}; save(); draw();
}
function updateScore(){
  const total=Object.keys(state.answers).length;
  const right=Object.values(state.answers).filter(a=>a.correct).length;
  $("scoreLabel").textContent=total?right+"/"+total:"0/0";
  const all=DATA.questions.length;
  const done=new Set(Object.keys(state.answers)).size;
  $("barFill").style.width=(done/all*100)+"%";
}
function showError(e){
  const area=$("quizArea") || document.body;
  area.innerHTML='<div class="card"><b>حصل خطأ غير متوقع في تحميل الكويز.</b><pre class="code">'+esc(String(e&&e.stack||e))+'</pre></div>';
}
try{
  $("lecSel").onchange=()=>{if($("lecSel").value)$("topicSel").value="";toggleExplain();start();};
  $("topicSel").onchange=()=>{if($("topicSel").value)$("lecSel").value="";toggleExplain();start();};
  $("explainBtn").onclick=()=>{
    const id=$("lecSel").value;
    const lec=DATA.lectures.find(l=>l.id===id);
    const wrap=$("explainWrap");
    if(wrap.style.display!=="none"){wrap.style.display="none";return;}
    if(!lec){wrap.style.display="none";return;}
    $("explainCard").innerHTML=renderMd(lec.content)+'<div style="margin-top:14px;text-align:center"><button class="btn primary" id="startLectureBtn" dir="ltr">Start Questions</button></div>';
    $("startLectureBtn").onclick=start;
    wrap.style.display="";
    wrap.scrollIntoView({behavior:"smooth",block:"start"});
  };
  $("shuffleBtn").onclick=()=>{const qs=filtered();state.order=shuffle(qs.map(q=>q.id));state.cur=0;state.phase="ask";save();draw();};
  $("reviewBtn").onclick=()=>{state.reviewOnly=true;const wrong=DATA.questions.filter(q=>state.answers[q.id]&&!state.answers[q.id].correct);if(!wrong.length){alert("No wrong answers to review!");return;}state.order=wrong.map(q=>q.id);state.cur=0;save();draw();};
  $("resetBtn").onclick=()=>{if(confirm("Clear all progress?")){localStorage.removeItem(KEY);state={answers:{},order:[],reviewOnly:false};start();}};
  $("fsClose").onclick=closeFs;
  $("fsModal").addEventListener("click",e=>{if(e.target.id==="fsModal")closeFs();});
  document.addEventListener("keydown",e=>{if(e.key==="Escape")closeFs();});
  initTheme();
  renderTopics();
  renderLectures();
  toggleExplain();
  updateScore();
  start();
}catch(e){
  showError(e);
}
</script>
</body>
</html>
"""


def update_readme(lectures, questions):
    path = os.path.join(ROOT, "README.md")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    start = "<!-- LECTURES:START -->"
    end = "<!-- LECTURES:END -->"
    if start not in text or end not in text:
        return
    counts = {}
    for q in questions:
        if q["lecture"]:
            counts[q["lecture"]] = counts.get(q["lecture"], 0) + 1
    rows = []
    total = 0
    for lec in lectures:
        n = counts.get(lec["id"], 0)
        total += n
        rows.append(f"| [محاضرة {lec['order']}: {lec['title_ar']}"
                    f" ({lec['title_en']})](generated/lectures/{lec['id']}.md) | {n} |")
    block = start + "\n" + "\n".join(rows) + f"\n\n**مجموع أسئلة المحاضرات: {total}**" + "\n" + end
    text = text[:text.index(start)] + block + text[text.index(end) + len(end):]
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def generate_site(questions, coding, lectures):
    os.makedirs(DOCS_DIR, exist_ok=True)
    data = {
        "topics": TOPIC_LABELS,
        "lectures": [{"id": l["id"], "title_ar": l["title_ar"],
                      "title_en": l["title_en"], "order": l["order"],
                      "content": l["content"]} for l in lectures],
        "questions": [{
            "id": q["id"], "topic": q["topic"], "lecture": q["lecture"],
            "topicLabel": q["topicLabel"],
            "q": q["q"], "title": q["title"], "code": q["code"],
            "expected": q["expected"], "exception": q["exception"],
            "compileError": q["compileError"], "explanation": q["explanation"],
            "options": q["options"], "answerIndex": q["answerIndex"],
            "theory": q["theory"],
        } for q in questions],
        "coding": [{"id": p["id"], "name": p["name"],
                    "problem": p.get("problem", ""),
                    "starter": p.get("starter", ""),
                    "solution": p.get("solution", ""),
                    "tests": p.get("tests", "")} for p in coding],
    }
    payload = json.dumps(data, ensure_ascii=False)
    html_out = SITE_TEMPLATE.replace("__DATA__", payload)
    with open(os.path.join(DOCS_DIR, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(html_out)


def main():
    lectures = collect_lectures()
    questions = collect_questions(lectures)
    coding = collect_coding()
    generate_topic_markdown(questions)
    generate_lecture_markdown(lectures, questions)
    update_readme(lectures, questions)
    generate_site(questions, coding, lectures)
    print(f"generated {len(questions)} questions ({sum(1 for q in questions if q['lecture'])} lecture), "
          f"{len(coding)} coding problems, {len(lectures)} lectures")


if __name__ == "__main__":
    main()
