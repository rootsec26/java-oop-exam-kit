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
.explain-panel{max-height:70vh;overflow-y:auto}
.explain-panel h1,.explain-panel h2,.explain-panel h3,.explain-panel h4{margin:.8em 0 .3em;font-size:1.1rem}
.explain-panel p{margin:.5em 0}
.explain-panel ul{margin:.5em 0;padding-inline-start:1.4em}
.explain-panel table{border-collapse:collapse;width:100%;margin:.7em 0;font-size:.9rem}
.explain-panel th,.explain-panel td{border:1px solid var(--border);padding:5px 9px;text-align:right}
.explain-panel th{background:var(--bg)}
.explain-panel code{background:var(--bg);border:1px solid var(--border);border-radius:4px;padding:0 4px;font-family:Consolas,monospace;font-size:.85em;direction:ltr;unicode-bidi:embed}
.explain-panel pre.code{text-align:left}
.nazri{display:inline-block;background:rgba(251,191,36,.15);border:1px solid #b45309;color:#fbbf24;border-radius:99px;padding:0 8px;font-size:.75rem;margin-inline-start:6px}
</style>
</head>
<body>
<div class="wrap">
<h1>⚡ Java OOP Exam Kit</h1>
<div class="muted">كويز تفاعلي — الإجابات متأكد منها بتشغيل الكود فعليًا. اختار موضوع، وبعدين "ابدأ".</div>
<div class="controls">
<select id="lecSel"></select>
<select id="topicSel"></select>
<button id="explainBtn" style="display:none">اقرأ الشرح</button>
<button id="shuffleBtn">خلط</button>
<button id="reviewBtn">راجع الغلط</button>
<button id="resetBtn">صفر التقدم</button>
<span class="score" id="scoreLabel"></span>
</div>
<div class="bar"><div id="barFill"></div></div>
<div id="explainWrap" style="display:none"><div class="card explain-panel" id="explainCard"></div></div>
<div id="quizArea"></div>
</div>
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
  const all=document.createElement("option"); all.value=""; all.textContent="كل الأسئلة ("+DATA.questions.length+")"; sel.appendChild(all);
  const counts={}; DATA.questions.forEach(q=>{if(!q.lecture)counts[q.topic]=(counts[q.topic]||0)+1;});
  Object.keys(counts).sort().forEach(t=>{const o=document.createElement("option");o.value=t;o.textContent=DATA.topics[t]+" ("+counts[t]+")";sel.appendChild(o);});
}
function renderLectures(){
  const sel=$("lecSel"); sel.innerHTML="";
  const none=document.createElement("option"); none.value=""; none.textContent="— محاضرة —"; sel.appendChild(none);
  const counts={}; DATA.questions.forEach(q=>{if(q.lecture)counts[q.lecture]=(counts[q.lecture]||0)+1;});
  DATA.lectures.forEach(l=>{const o=document.createElement("option");o.value=l.id;o.textContent="محاضرة "+l.order+": "+l.title_ar+" ("+(counts[l.id]||0)+")";sel.appendChild(o);});
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
    area.innerHTML='<div class="card muted">مفيش أسئلة في الاختيار ده.</div>';
    return;
  }
  if(state.cur>=state.order.length) state.cur=0;
  const id=state.order[state.cur]; const q=DATA.questions.find(x=>x.id===id);
  if(!q){ state.order=state.order.filter(x=>x!==id); draw(); return; }
  const answered=!!state.answers[id];
  const ans=state.answers[id];
  const mode=q.options?"mcq":(q.compileError?"choice":(q.exception?"exc":"output"));
  const pos=state.order.indexOf(id)+1;
  let html='<div class="card"><div class="tags"><span class="tag">سؤال '+pos+' من '+state.order.length+'</span><span class="tag">'+esc(q.topicLabel)+'</span>'+(q.theory?'<span class="tag nazri">نظري</span>':"")+(q.title?'<span class="tag">'+esc(q.title)+'</span>':"")+'</div>';
  if(q.code) html+='<pre class="code"><code>'+highlight(q.code)+'</code></pre>';
  if(mode==="mcq"){
    html+='<div class="opts">';
    q.options.forEach((t,i)=>{
      html+='<div class="opt'+(ans&&String(ans.pick)===String(i)?" sel":"")+'" data-idx="'+i+'">'+esc(t)+'</div>';
    });
    html+='</div>';
  } else if(mode==="choice"){
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
    html+='<div class="muted">لو اخترت "بيرمي Exception" اسم الـ Exception هيظهر في الإجابة تحت.</div>';
  } else {
    html+='<div class="muted">اكتب الناتج اللي هيطبعه البرنامج (stdout). لو بيقع بـ Runtime Exception اختار الزرار.</div>';
    html+='<textarea id="ansBox" dir="ltr" placeholder="الناتج هنا..."></textarea>';
    html+='<div class="opts" style="flex-direction:row;flex-wrap:wrap">';
    html+='<div class="opt" data-pick="exc">بيرمي Runtime Exception</div>';
    html+='<div class="opt" data-pick="compile">Compile Error</div>';
    html+='<div class="opt" id="submitOut" style="background:var(--accent);color:#082f49;font-weight:700">شيك</div>';
    html+='</div>';
  }
  html+='<div style="display:flex;gap:8px;margin-top:10px"><button class="primary" id="nextBtn"'+(answered?"":" disabled")+'>التالي</button></div>';
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
      const pick=o.dataset.idx!==undefined?o.dataset.idx:o.dataset.pick;
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
  $("scoreLabel").textContent=total?`${right}/${total} صح` : "";
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
    $("explainCard").innerHTML=renderMd(lec.content)+'<div style="margin-top:14px;text-align:center"><button class="primary" id="startLectureBtn">ابدأ الأسئلة</button></div>';
    $("startLectureBtn").onclick=start;
    wrap.style.display="";
    wrap.scrollIntoView({behavior:"smooth",block:"start"});
  };
  $("shuffleBtn").onclick=()=>{const qs=filtered();state.order=shuffle(qs.map(q=>q.id));state.cur=0;state.phase="ask";save();draw();};
  $("reviewBtn").onclick=()=>{state.reviewOnly=true;const wrong=DATA.questions.filter(q=>state.answers[q.id]&&!state.answers[q.id].correct);if(!wrong.length){alert("مفيش إجابات غلط للمراجعة!");return;}state.order=wrong.map(q=>q.id);state.cur=0;save();draw();};
  $("resetBtn").onclick=()=>{if(confirm("تمسح كل التقدم؟")){localStorage.removeItem(KEY);state={answers:{},order:[],reviewOnly:false};start();}};
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
