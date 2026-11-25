import html
import json
import os
import random
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_DIR = os.path.join(ROOT, "questions")
CODING_DIR = os.path.join(ROOT, "coding")
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


def collect_questions():
    questions = []
    if not os.path.isdir(QUESTIONS_DIR):
        return questions
    for topic in sorted(os.listdir(QUESTIONS_DIR)):
        tdir = os.path.join(QUESTIONS_DIR, topic)
        if not os.path.isdir(tdir):
            continue
        for q in sorted(os.listdir(tdir)):
            qdir = os.path.join(tdir, q)
            if not os.path.isdir(qdir):
                continue
            with open(os.path.join(qdir, "Main.java"), encoding="utf-8") as f:
                code = f.read()
            with open(os.path.join(qdir, "expected.txt"), encoding="utf-8") as f:
                raw_expected = f.read()
            exception, expected = parse_expected(raw_expected)
            compile_error = raw_expected.strip() == "COMPILE_ERROR"
            title, explanation = read_explanation(os.path.join(qdir, "explanation.md"))
            questions.append({
                "id": f"{topic}/{q}",
                "topic": topic,
                "topicLabel": TOPIC_LABELS.get(topic, topic),
                "q": q,
                "title": title,
                "code": code,
                "expected": expected,
                "exception": exception,
                "compileError": compile_error,
                "explanation": explanation,
            })
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


def generate_topic_markdown(questions):
    os.makedirs(GENERATED_DIR, exist_ok=True)
    by_topic = {}
    for q in questions:
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
:root{--bg:#0f172a;--panel:#1e293b;--text:#e2e8f0;--muted:#94a3b8;--accent:#38bdf8;--good:#4ade80;--bad:#f87171;--border:#334155;--code:#0b1220}
@media (prefers-color-scheme:light){:root{--bg:#f8fafc;--panel:#ffffff;--text:#0f172a;--muted:#475569;--accent:#0284c7;--good:#16a34a;--bad:#dc2626;--border:#cbd5e1;--code:#f1f5f9}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-family:Segoe UI,Tahoma,Arial,sans-serif;line-height:1.7}
.wrap{max-width:860px;margin:0 auto;padding:16px}
h1{font-size:1.5rem;margin:.4em 0}
.bar{height:8px;background:var(--border);border-radius:99px;overflow:hidden;margin:10px 0}
.bar>div{height:100%;background:var(--accent);width:0;transition:width .3s}
.controls{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0;align-items:center}
button,.btn{background:var(--panel);color:var(--text);border:1px solid var(--border);border-radius:8px;padding:8px 14px;cursor:pointer;font-size:1rem}
button:hover,.btn:hover{border-color:var(--accent)}
button.primary{background:var(--accent);color:#082f49;border:none;font-weight:700}
button:disabled{opacity:.4;cursor:default}
select{background:var(--panel);color:var(--text);border:1px solid var(--border);border-radius:8px;padding:8px}
.card{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:18px;margin:14px 0}
pre.code{background:var(--code);border:1px solid var(--border);border-radius:8px;padding:14px;overflow-x:auto;direction:ltr;text-align:left;font-family:Consolas,Menlo,monospace;font-size:.9rem;line-height:1.5}
pre.code code{font-family:inherit}
.kw{color:#c084fc}.str{color:#86efac}.num{color:#fbbf24}.com{color:#64748b;font-style:italic}.typ{color:#7dd3fc}.ann{color:#f472b6}
.opts{display:flex;flex-direction:column;gap:8px;margin:14px 0}
.opt{background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:10px 14px;text-align:right;cursor:pointer;font-size:1rem}
.opt:hover{border-color:var(--accent)}
.opt.sel{border-color:var(--accent);background:rgba(56,189,248,.12)}
textarea{width:100%;background:var(--code);color:var(--text);border:1px solid var(--border);border-radius:8px;padding:10px;font-family:Consolas,monospace;direction:ltr;text-align:left;min-height:90px;font-size:.95rem}
.feedback{border-radius:8px;padding:12px;margin:12px 0;display:none}
.feedback.ok{display:block;background:rgba(74,222,128,.12);border:1px solid var(--good)}
.feedback.no{display:block;background:rgba(248,113,113,.12);border:1px solid var(--bad)}
.expl{background:var(--bg);border:1px dashed var(--border);border-radius:8px;padding:12px;margin-top:10px;display:none}
.expl.show{display:block}
.score{font-weight:700;color:var(--accent)}
.muted{color:var(--muted);font-size:.9rem}
.tags{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}
.tag{background:var(--bg);border:1px solid var(--border);border-radius:99px;padding:2px 10px;font-size:.8rem;color:var(--muted)}
</style>
</head>
<body>
<div class="wrap">
<h1>⚡ Java OOP Exam Kit</h1>
<div class="muted">كويز تفاعلي — الإجابات متأكد منها بتشغيل الكود فعليًا. اختار موضوع، وبعدين "ابدأ".</div>
<div class="controls">
<select id="topicSel"></select>
<button id="shuffleBtn">خلط</button>
<button id="reviewBtn">راجع الغلط</button>
<button id="resetBtn">صفر التقدم</button>
<span class="score" id="scoreLabel"></span>
</div>
<div class="bar"><div id="barFill"></div></div>
<div id="quizArea"></div>
</div>
<script>
const DATA = __DATA__;
const KEY = "javaOopQuizV1";
let state = JSON.parse(localStorage.getItem(KEY) || "null") || {answers:{}, order:[], reviewOnly:false};
function save(){ localStorage.setItem(KEY, JSON.stringify(state)); }
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
function filtered(){
  const t=$("topicSel").value;
  let qs=DATA.questions.filter(q=>!t||q.topic===t);
  if(state.reviewOnly){qs=qs.filter(q=>state.answers[q.id]&&!state.answers[q.id].correct);}
  return qs;
}
function renderTopics(){
  const sel=$("topicSel"); sel.innerHTML="";
  const all=document.createElement("option"); all.value=""; all.textContent="كل المواضيع ("+DATA.questions.length+")"; sel.appendChild(all);
  const counts={}; DATA.questions.forEach(q=>counts[q.topic]=(counts[q.topic]||0)+1);
  Object.keys(counts).sort().forEach(t=>{const o=document.createElement("option");o.value=t;o.textContent=DATA.topics[t]+" ("+counts[t]+")";sel.appendChild(o);});
}
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function start(){
  state.reviewOnly=false; save();
  const qs=filtered(); state.order=qs.map(q=>q.id); state.cur=0; state.phase="ask"; save(); draw();
}
function draw(){
  const area=$("quizArea"); const id=state.order[state.cur]; const q=DATA.questions.find(x=>x.id===id);
  const answered=!!state.answers[id];
  const ans=state.answers[id];
  const mode=q.compileError?"choice":(q.exception?"exc":"output");
  let html='<div class="card"><div class="tags"><span class="tag">'+esc(q.topicLabel)+'</span><span class="tag">'+esc(q.q)+'</span>'+(q.title?'<span class="tag">'+esc(q.title)+'</span>':"")+'</div>';
  html+='<pre class="code"><code>'+highlight(q.code)+'</code></pre>';
  if(mode==="choice"){
    html+='<div class="opts">';
    ["فيه Compile Error","مفيش — بيترجم ويشتغل"].forEach((t,i)=>{
      const pick=i===0? "compile":"run";
      html+='<div class="opt'+(ans&&ans.pick===pick?" sel":"")+'" data-pick="'+pick+'">'+t+'</div>';
    });
    html+='</div>';
  } else if(mode==="exc"){
    html+='<div class="opts">';
    [["exc","بيرمي Runtime Exception"],["compile","Compile Error"],["run","بيطبع ناتج عادي"]].forEach(([p,t])=>{
      html+='<div class="opt'+(ans&&ans.pick===p?" sel":"")+'" data-pick="'+p+'">'+t+'</div>';
    });
    html+='</div>';
    html+='<div class="muted">لو اخترت "بيرمي Exception" الصح هوChoice — شوف الإجابة تحت بعد ما تجاوب.</div>';
  } else {
    html+='<div class="muted">اكتب الناتج اللي هيطبعه البرنامج (stdout). لو بيقع بـ Runtime Exception اختار الزرار.</div>';
    html+='<textarea id="ansBox" dir="ltr" placeholder="الناتج هنا..."></textarea>';
    html+='<div class="opts" style="flex-direction:row;flex-wrap:wrap">';
    html+='<div class="opt" data-pick="exc">بيرمي Runtime Exception</div>';
    html+='<div class="opt" data-pick="compile">Compile Error</div>';
    html+='<div class="opt" id="submitOut" style="background:var(--accent);color:#082f49;font-weight:700">شيك</div>';
    html+='</div>';
  }
  if(!answered){
    html+='<div style="display:flex;gap:8px;margin-top:10px"><button class="primary" id="nextBtn" disabled>التالي</button></div>';
  }
  html+='<div class="feedback" id="fb"></div>';
  html+='<div class="expl'+(answered?" show":"")+'" id="expl">';
  html+='<b>الإجابة الصحيحة:</b><pre class="code" style="margin:8px 0"><code>'+esc(answerText(q))+'</code></pre>';
  html+='<div>'+esc(q.explanation)+'</div></div>';
  html+='</div>';
  area.innerHTML=html;
  const fb=$("fb");
  if(answered){
    fb.className="feedback "+(ans.correct?"ok":"no");
    fb.textContent=ans.correct?"✔ إجابة صح!":"✘ إجابة غلط — شوف الإجابة تحت.";
  }
  area.querySelectorAll(".opt").forEach(o=>{
    if(answered) return;
    o.onclick=()=>{
      const pick=o.dataset.pick;
      if(mode==="output"&&pick==="exc"){
        submitOutput(q,"exc"); return;
      }
      if(mode==="output"&&pick==="compile"){
        submitOutput(q,"compile"); return;
      }
      if(mode==="output"&&o.id==="submitOut"){
        submitOutput(q,"text"); return;
      }
      grade(q,pick,null);
    };
  });
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
  else if(pick==="compile") correct=q.compileError;
  else if(pick==="exc") correct=!!q.exception;
  else if(pick==="run") correct=!q.compileError&&!q.exception;
  else correct=false;
  state.answers[id]={correct,pick,typed:typed||""}; save(); draw();
}
function updateScore(){
  const total=Object.keys(state.answers).length;
  const right=Object.values(state.answers).filter(a=>a.correct).length;
  $("scoreLabel").textContent=total?`${right}/${total} صح` : "";
  const all=DATA.questions.length;
  const done=new Set(Object.keys(state.answers)).size;
  $("barFill").style.width=(done/all*100)+"%";
}
$("topicSel").onchange=start;
$("shuffleBtn").onclick=()=>{const qs=filtered();state.order=shuffle(qs.map(q=>q.id));state.cur=0;state.phase="ask";save();draw();};
$("reviewBtn").onclick=()=>{state.reviewOnly=true;const wrong=DATA.questions.filter(q=>state.answers[q.id]&&!state.answers[q.id].correct);if(!wrong.length){alert("مفيش إجابات غلط للمراجعة!");return;}state.order=wrong.map(q=>q.id);state.cur=0;save();draw();};
$("resetBtn").onclick=()=>{if(confirm("تمسح كل التقدم؟")){localStorage.removeItem(KEY);state={answers:{},order:[],reviewOnly:false};start();}};
renderTopics();
updateScore();
start();
</script>
</body>
</html>
"""


def generate_site(questions, coding):
    os.makedirs(DOCS_DIR, exist_ok=True)
    data = {
        "topics": TOPIC_LABELS,
        "questions": [{
            "id": q["id"], "topic": q["topic"], "topicLabel": q["topicLabel"],
            "q": q["q"], "title": q["title"], "code": q["code"],
            "expected": q["expected"], "exception": q["exception"],
            "compileError": q["compileError"], "explanation": q["explanation"],
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
    questions = collect_questions()
    coding = collect_coding()
    generate_topic_markdown(questions)
    generate_site(questions, coding)
    print(f"generated {len(questions)} questions, {len(coding)} coding problems")


if __name__ == "__main__":
    main()
