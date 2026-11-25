# المساهمة

## تضيف سؤال جديد؟

1. اعمل فولدر جديد تحت `questions/<topic>/q<NN>/` (رقم مش مستخدم في نفس الموضوع).
2. اكتب:
   - `Main.java` — الكود **من غير أي comments** (الـ comments ممكن تسرّب الإجابة).
   - `expected.txt` — الـ stdout بالظبط، أو `COMPILE_ERROR` لو مش بيترجم، أو أول سطر `EXCEPTION=java.lang.X` لو بيقع بـ runtime exception.
   - `explanation.md` — شرح مصري في 1-3 جمل. ممكن تبدأ بسطر `# عنوان`.
3. شغّل `python tools/verify.py` — لازم يعدي. لو فشل، صلّح `expected.txt` أو `explanation.md` حسب سلوك Java **الحقيقي** — متظبطش السؤال على إجابة غلط.

## تضيف مسألة coding؟

اعمل فولدر في `coding/<name>/` فيه `problem.md` (مصري)، `Starter.java` (فيه TODOs)، `Solution.java` (كامل)، و `Tests.java` (assertions عادية بتطبع PASS/FAIL). `verify.py` بيشغّل الـ Tests ولازم كلها PASS.

## تضيف محاضرة جديدة؟

1. حط الـ PDF في `source/` (المجلد ده في `.gitignore` — منترفعش على git).
2. اعمل `lectures/NN-slug/` فيه:
   - `meta.json` — `{"title_ar": "...", "title_en": "...", "order": N}`
   - `lecture.md` — شرح مصري. القواعد:
     - كل مثال كود بلوك ```` ```java run ```` متبوع مباشرة بلوك ```` ```output ```` فيه الـ stdout بالظبط.
     - لو البلوك مفيهوش `class` بيتلفّ أوتوماتيك جوه `main` — ابعت snippets عادية أو برامج كاملة.
     - **ممنوع comments جوا أمثلة الكود**، والنصوص متتنسخش verbatim من السلايدات.
     - اقفل الصفحة بـ"ملخص سريع" (8-12 نقطة).
3. أسئلة المحاضرة في `questions/lecNN-slug/qNN/` — نفس فورمات أسئلة المواضيع. سؤال نظري (اختيارات) يحط `options.json` بدل `Main.java`+`expected.txt` بصيغة `{"options": [...], "answer": <index>}`.
4. `verify.py` بيفحص أمثلة `lecture.md` كمان — لازم كلها تعدي.

## قبل الـ PR

```bash
python tools/verify.py   # لازم 100%
python tools/build.py    # لازم يعيد توليد generated/ و docs/ من غير diffs
```
