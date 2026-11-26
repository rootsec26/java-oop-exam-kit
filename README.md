# ⚡ Java OOP Exam Kit

كيت امتحان Java OOP للطلبة Egyptians — كل سؤال هنا **ملف Java حقيقي مترجم ومتأكد منه فعليًا**، مش مكتوب من الذاكرة.

## إزاي تستخدمه

- **كويز تفاعلي**: افتح `docs/index.html` في المتصفح (شغال offline، مفيش servers). فيه فلتر بالموضوع، خلط، تتبع للنتيجة في `localStorage`، ووضع "راجع الغلط".
- **قراية**: كل موضوع ليه ملف markdown في `generated/` — الكود والإجابة جوه `<details>`.

## التأكد من الإجابات

كل إجابة متأكد منها بتشغيل `javac` و `java` فعليًا:

```bash
python tools/verify.py
```

لازم يكون عندك JDK (17+) في الـ PATH. السكريبت بيطبع جدول PASS/FAIL وبيطلع بكود خطأ لو في أي إجابة غلط — وCI بيمنع أي merge فيه إجابة مش متأكد منها.

## المواضيع

| الموضوع | العدد |
|---|---|
| [وراثة و Constructor Chaining](generated/inheritance.md) | 7 |
| [Polymorphism](generated/polymorphism.md) | 7 |
| [static و final و this و super](generated/static-final-this-super.md) | 7 |
| [Abstract Classes و Interfaces](generated/abstract-interface.md) | 7 |
| [Access Modifiers و Packages](generated/access-modifiers.md) | 7 |
| [Exceptions](generated/exceptions.md) | 8 |
| [String و equals و hashCode](generated/strings-equals.md) | 8 |
| [Casting و instanceof](generated/casting.md) | 7 |
| [Inner Classes و Enums](generated/inner-classes.md) | 7 |
| [Collections](generated/collections.md) | 8 |

**المجموع: 73 سؤال** + 6 مسائل coding في `coding/` (كل واحدة فيها `problem.md` و `Starter.java` و `Solution.java` و `Tests.java`).

## المحاضرات

| المحاضرة | العدد |
|---|---|
<!-- LECTURES:START -->
| [محاضرة 1: مدخل إلى البرامج وجافا (Introduction to Programs and Java)](generated/lectures/01-introduction.md) | 16 |
| [محاضرة 2: أساسيات جافا — المتغيرات والأنواع والعمليات (Java Basics — Variables, Types, Operators)](generated/lectures/02-java-basics.md) | 46 |
| [محاضرة 4: الـ Methods (Methods)](generated/lectures/04-methods.md) | 53 |

**مجموع أسئلة المحاضرات: 115**
<!-- LECTURES:END -->

## امتحانات سابقة

| الامتحان | العدد |
|---|---|
<!-- EXAMS:START -->
| [Mid2024 National](generated/exams/mid2024-national.md) | 37 |

**مجموع أسئلة الامتحانات: 37**
<!-- EXAMS:END -->

## تساهم؟

شوف [CONTRIBUTING.md](CONTRIBUTING.md) — 3 خطوات: اعمل فولدر للسؤال، اكتب `Main.java` و `expected.txt`، وشغّل `verify.py`.

## ملاحظات

- ملفات `questions/*/Main.java` **ممنوع فيها comments** — عشان متسربش الإجابة.
- `expected.txt` فيها الـ stdout بالظبط، أو `COMPILE_ERROR` لو الكود مش بيترجم، أو أول سطر `EXCEPTION=<class>` لو بيقع بـ runtime exception.
