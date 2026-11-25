# Cheatsheet — Java OOP

## الترتيب والـ Initialization
- إنشاء object: static init للكلاس → super constructor → instance init blocks → constructor body (نفس الترتيب في الوراثة: الأب الأول).
- `super()` لازم أول سطر في الـ constructor؛ `this()` برضه. مينفعش الاتنين مع بعض.
- method بتتنده من constructor بتعمل **dynamic dispatch** — ممكن تنده override في subclass قبل ما حقول الـ subclass تتملى.

## Overriding vs Overloading
- Overload: نفس الاسم signature مختلف → الاختيار **compile-time** حسب نوع الـ reference.
- Override: نفس الـ signature → الاختيار **runtime** حسب نوع الـ object.
- static methods و fields: **hiding** مش override — الاختيار compile-time.
- private methods مش بتتورث → مش override.
- الـ override ممنوع: access أضيق، static↔instance، throws أوسع. `@Override` بيأكد ده.

## static / final / this / super
- static field مشترك لكل الـ instances؛ static block بيشتغل مرة عند تحميل الكلاس (الأب قبل الابن).
- `final` على class = ممنوع extends؛ على method = ممنوع override؛ على field = لازم يتسند في declaration أو constructor ومرة واحدة.
- `super.x` بيوصل field الأب حتى لو متعمله hide بـ `this.x`.

## Abstract / Interface
- abstract class ليها constructors و fields و methods عادية؛ مينفعش `new` ليها مباشرة.
- interface fields = `public static final`؛ methods = `public` ضمنيًا.
- `default` methods بتتورث؛ `static` methods في interface **مش بتتورث** — بتنادى `Interface.m()` بس.
- class بيعمل implements لـ interface اتنين فيهم نفس الـ default method → لازم يعمل override (diamond problem).

## Access Modifiers
- private: نفس الـ class بس. default (بدون modifier): نفس الـ package. protected: package + subclasses. public: الكل.
- private members **مش بتتورث** — subclass مش بيشوفها.
- override لازم نفس الـ access أو أوسع — مش أضيق.
- nested classes والـ outer بتعتبر nestmates → private access بينهم شغال.

## Exceptions
- checked (IOException, Exception) لازم `throws` أو catch؛ unchecked (RuntimeException) لأ.
- ترتيب الـ catch: **الأضيق الأول** — subclass قبل superclass وإلا compile error.
- `finally` بيشتغل دايمًا — حتى مع return، و`return` جوه finally **بيستبدل** أي return تاني.
- try-with-resources بيقفل بـ **عكس ترتيب** الإنشاء.
- override مينفعش يوسّع `throws`.
- exception مش متلقطة → البرنامج بيقع والـ exception بتظهر في stderr.

## String / equals / hashCode
- `==` على Strings بيقارن المرجع؛ `equals` بيقارن المحتوى. literals متشابهة → نفس الـ pooled object.
- `new String("x")` ≠ pooled. concat بـ literal+literal = compile-time constant (pooled)؛ concat runtime = object جديد.
- String immutable — `concat`/`+` بيرجعوا جديد؛ `StringBuilder` بيتغير في مكانه.
- `"x" + null` → `"xnull"` مش exception.
- Integer cache: -128 لـ 127 → `==` شغالة؛ بره الـ cache لأ. `Integer == int` بيعمل unbox → مقارنة بالقيمة.
- لو عملت `equals` لازم `hashCode` متسقة — وإلا HashSet/HashMap هيعتبروهم مختلفين.
- Java pass-by-value — تغيير reference جوه method مش بيأثر بره.

## Casting / instanceof
- upcast آمن دايمًا؛ downcast بيترجم بس ممكن `ClassCastException` runtime.
- cast بين classes مالهمش علاقة = compile error؛ cast لـ interface بيترجم دايمًا.
- `null instanceof X` → false دايمًا.
- Generics بتتمسح (erasure) — `(List<Integer>) rawList` unchecked وممكن يفشل runtime.

## Inner Classes / Enums
- non-static inner class ليها outer reference → تقدر توصل outer fields؛ static nested لأ.
- local variables جوه inner/anonymous class لازم تكون **effectively final**.
- enum constants singleton → `==` شغالة. `values()`، `ordinal()` (من 0)، `valueOf(name)`.
- enum يقدر يكون ليه constructor و fields — كل constant بيناديه بالقيمة جنبه.

## Collections
- `ArrayList` = insertion order + duplicates مسموحة.
- `contains`/`remove`/`indexOf` بيعتمدوا على `equals` — object من غير equals بيتقارن بالمرجع.
- `list.remove(1)` = بالـ index؛ `list.remove("a")` = بالقيمة — انتبه للـ overload!
- for-each على collection متعدلة جوه اللوب → `ConcurrentModificationException`.
- `List.of()` immutable → أي تعديل `UnsupportedOperationException`.
- `List<int>` compile error — generics reference types بس.
