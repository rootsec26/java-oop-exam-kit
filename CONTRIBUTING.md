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

## قبل الـ PR

```bash
python tools/verify.py   # لازم 100%
python tools/build.py    # لازم يعيد توليد generated/ و docs/ من غير diffs
```
