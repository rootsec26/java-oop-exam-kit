# الـ Methods — المحاضرة 4

المحاضرة دي عن **method**: مجموعة statements مجمّعة مع بعض بتعمل عملية واحدة. الفكرة الأساسية إنك تكتب الكود مرة وتستخدمه في أي حتة — وده بيقلل التعقيد وبيخلي البرنامج أسهل في الفهم والصيانة.

## ليه Methods أصلاً

تخيل إنك عايز تجمع الأرقام من 1 لـ 10، ومن 20 لـ 30، ومن 35 لـ 45. من غير methods هتكرر نفس الـ for loop تلات مرات — كود مكرر ومرهق:

```java run
public class SumDemo {
    public static void main(String[] args) {
        System.out.println("Sum from 1 to 10 is " + sum(1, 10));
        System.out.println("Sum from 20 to 30 is " + sum(20, 30));
        System.out.println("Sum from 35 to 45 is " + sum(35, 45));
    }

    public static int sum(int i1, int i2) {
        int sum = 0;
        for (int i = i1; i <= i2; i++) {
            sum += i;
        }
        return sum;
    }
}
```

```output
Sum from 1 to 10 is 55
Sum from 20 to 30 is 275
Sum from 35 to 45 is 440
```

كتابة `sum` مرة واحدة وفهمناها مرة واحدة — وده جوهر الـ abstraction.

## تشريح الـ Method

```java
public static int max(int num1, int num2) {
    int result;
    if (num1 > num2)
        result = num1;
    else
        result = num2;
    return result;
}
```

- **method header**: السطر اللي بيفتكر التعريف — فيه modifier و return type و name و parameter list.
- **modifier**: زي `public` و `static` — بتحدد خصائص الميثود.
- **return value type**: نوع القيمة اللي بترجعها — `int` هنا، أو `void` لو مش بترجع حاجة.
- **method name**: اسم الميثود.
- **formal parameters**: المتغيرات اللي في القوسين — `num1` و `num2` هنا.
- **parameter list**: القوسين ومحتواهم.
- **method body**: الـ block `{ }` اللي فيه الـ statements.
- **return value**: القيمة اللي بترجعها عبر `return`.

**method signature** = اسم الميثود + parameter list **بس** — نوع الرجوع (`int`) مش جزء من الـ signature! عشان كده مفيش methodين بنفس الاسم ونفس الباراميترز بس return type مختلف — ده Compile Error.

لما تنادي الميثود بتبعت قيم اسمها **actual parameters** أو **arguments**: `int z = max(x, y);`

## void مقابل value-returning

- ميثود بترجع قيمة: لازم فيها `return value;` في كل الطرق الممكنة — الـ compiler بيفحص إن في return reachable دايماً.
- ميثود `void`: بتعمل حاجات (زي الطباعة) ومفيش `return` بقيمة — ممكن `return;` فاضية لو حابب تخرج بدري.

**الفخ الأشهر:** لو كتبت if/else-if ونسيت else أخير، الـ compiler بيعتبر إن ممكن الميثود توصل للنهاية من غير return = Compile Error "missing return statement" — حتى لو منطقياً كل الحالات متغطية.

ولو عندك ميثود void ومستخدمها كأنها بترجع قيمة (`int x = print();`) = Compile Error. وممكن تنادي ميثود من كلاس تاني بـ `ClassName.methodName`:

```java run
class Util {
    static int doubleIt(int x) {
        return x * 2;
    }
}

public class MethodDemo {
    public static void main(String[] args) {
        System.out.println(Util.doubleIt(21));
        greet();
    }

    static void greet() {
        System.out.println("hi");
    }
}
```

```output
42
hi
```

## الـ Call Stack

لما `main` ينادي `max`، جافا بتحجز **frame** جديد فوق الـ stack لكل call — الـ frame بيخزن الـ parameters والـ local variables بتاعة النداء ده. `main` frame بيفضل تحت طول ما الميثود شغالة، ولما الـ method تخلص الـ frame **بتتشال** (pop) والـ return value بيروح للمتغير اللي استدعاها. عشان كده recursion لانهائية = `StackOverflowError` — الـ stack بيتملى frames.

نقطة مهمة: **arguments بتتنفذ قيمها قبل ما الميثود تتنادى** — لو عندك `f(g(1), g(2))` الـ `g` بتتنفذ الأول (بالترتيب من الشمال)، وبعدين `f`:

```java run
public class OrderDemo {
    public static void main(String[] args) {
        System.out.println(f(g(1), g(2)));
    }

    static int g(int x) {
        System.out.println("g" + x);
        return x;
    }

    static int f(int a, int b) {
        return a * 10 + b;
    }
}
```

```output
g1
g2
12
```

## Pass by Value

جافا بتبعت **نسخة من القيمة** مش المتغير نفسه. أي تغيير جوه الميثود على الـ parameter مش بيأثر على المتغير الأصلي في الـ caller:

```java run
class Swap {
    static void swap(int a, int b) {
        int t = a;
        a = b;
        b = t;
    }
}

public class PassDemo {
    public static void main(String[] args) {
        int x = 1, y = 2;
        Swap.swap(x, y);
        System.out.println(x + " " + y);
    }
}
```

```output
1 2
```

`x` و `y` فضلوا زي ما هما — `swap` بدّل نسخ `a` و `b` بس. (خارج نطاق السلايدات: ده بيحصل مع الكائنات كمان — الميثود تقدر تغير **محتوى** object مُرّر، بس مش تقدر تعيد إسناد المرجع نفسه جوه الميثود.)

## Overloading — نفس الاسم أكتر من مرة

تقدر تعرّف كذا method بنفس الاسم بشرط إن الـ parameter lists مختلفة (عدد أو أنواع مختلفة). الـ compiler بيختار **أنسب** overload وقت الترجمة:

```java run
public class OverloadDemo {
    public static void main(String[] args) {
        System.out.println(max(2, 3));
        System.out.println(max(2.5, 3));
        System.out.println(max(2, 3.5));
    }

    static int max(int a, int b) {
        return a > b ? a : b;
    }

    static double max(double a, double b) {
        return a > b ? a : b;
    }
}
```

```output
3
3.0
3.5
```

القواعد: لو في overload مطابق بالظبط بيتختار، لو مفيش بيدور على widening (int→long→float→double). لو لقى أكتر من اختيار متعادل = **ambiguous invocation** = Compile Error. وoverloading على الـ return type بس مستحيل — مش جزء من الـ signature.

## Scope بتاع Local Variables

- الـ local variable بيتعرف من سطر إعلانه لحد آخر الـ block اللي فيه.
- لازم يتعرّف **قبل** ما يتستخدم.
- ممكن نفس الاسم في blockين **مش متداخلين** (زي `i` في for loopين ورا بعض) — عادي.
- نفس الاسم في block **متداخل** = Compile Error.
- الـ variable اللي في `for (int i...)` الـ scope بتاعها الـ loop كله — استخدامها بعد الـ loop = Compile Error.
- إعادة تعريف الـ parameter كـ local جوه الميثود = Compile Error.

```java run
public class ScopeDemo {
    public static void main(String[] args) {
        int s = 0;
        for (int i = 0; i < 2; i++) {
            s += i;
        }
        for (int i = 0; i < 3; i++) {
            s += i * 10;
        }
        System.out.println(s);
    }
}
```

```output
31
```

## Method Abstraction

الـ method body زي **black box**: بتستخدمه من غير ما تعرف التفاصيل جواه. الفوايد:

- **Reuse**: تكتبه مرة وتندهه من أي حتة أو أي كلاس.
- **Information hiding**: المستخدم مش محتاج يعرف إزاي جواه اشتغل.
- **تقليل التعقيد**: البرنامج بيتقسم لمشاكل صغيرة كل واحدة في method.

## الـ Math Class

`java.lang.Math` كلاس جاهز مليان methods — مش محتاج تعمل `new Math()`، بتناديها `Math.methodName`:

- ثوابت: `Math.PI` و `Math.E`
- Trigonometric: `sin, cos, tan, asin, acos, atan` — **الرadian مش الدرجة!** `toRadians(90)` بيحوّل.
- Exponent: `exp, log (طبيعي), log10, pow, sqrt`
- Rounding: `ceil` لفوق، `floor` لتحت، `rint` لأقرب (اللي في النص بيروح للزوجي)، `round` لأقرب صحيح.
- `min, max, abs, random` — `random()` بترجع double في `[0.0, 1.0)`.

```java run
public class MathDemo {
    public static void main(String[] args) {
        System.out.println(Math.PI);
        System.out.println(Math.E);
        System.out.println(Math.sin(Math.PI / 6));
        System.out.println(Math.cos(Math.PI / 2));
        System.out.println(Math.toRadians(90));
        System.out.println(Math.pow(2, 3));
        System.out.println(Math.sqrt(4));
        System.out.println(Math.exp(1));
        System.out.println(Math.log(Math.E));
        System.out.println(Math.log10(1000));
        System.out.println(Math.max(2, 3));
        System.out.println(Math.max(2.5, 3));
        System.out.println(Math.min(-0.0, 0.0));
        System.out.println(Math.abs(-2.1));
        System.out.println(Math.abs(Integer.MIN_VALUE));
    }
}
```

```output
3.141592653589793
2.718281828459045
0.49999999999999994
6.123233995736766E-17
1.5707963267948966
8.0
2.0
2.718281828459045
1.0
3.0
3
3.0
-0.0
2.1
-2147483648
```

**انتبه:** `Math.sin(Math.PI/6)` مش بتطبع `0.5` بالظبط — بتطبع `0.49999999999999994`، و `Math.cos(Math.PI/2)` مش `0` — بتطبع `6.123233995736766E-17`. دي نفس مشكلة دقة الـ double — السلايد بتقول 0.5 و 0 بس الحقيقة غير كده.

Rounding methods بالظبط:

```java run
public class RoundDemo {
    public static void main(String[] args) {
        System.out.println(Math.ceil(2.1));
        System.out.println(Math.ceil(-2.1));
        System.out.println(Math.floor(2.1));
        System.out.println(Math.floor(-2.1));
        System.out.println(Math.rint(2.5));
        System.out.println(Math.rint(-2.5));
        System.out.println(Math.round(2.6));
        System.out.println(Math.round(-2.6));
        System.out.println(Math.round(2.6f));
        System.out.println(Math.round(-2.5f));
    }
}
```

```output
3.0
-2.0
2.0
-3.0
2.0
-2.0
3
-3
3
-2
```

`ceil/floor/rint` بيرجعوا **double**، `round` بيرجع **int** لـ float و **long** لـ double — يعني `int x = Math.round(2.6)` Compile Error لازم cast أو long.

## Math.random

`Math.random()` بترجع double عشوائي في `[0.0, 1.0)` — يعني ممكن تطلع 0.0 بس **مش** 1.0. عشان تحولها لنطاق معين:

- `(int)(Math.random() * 10)` → int عشوائي من 0 لـ 9
- `50 + (int)(Math.random() * 50)` → من 50 لـ 99
- الحرف العشوائي الصغير: `(char)('a' + Math.random() * ('z' - 'a' + 1))`

```java run
public class RandomDemo {
    public static void main(String[] args) {
        boolean ok = true;
        for (int i = 0; i < 1000; i++) {
            int r = (int)(Math.random() * 10);
            if (r < 0 || r > 9) ok = false;
        }
        System.out.println(ok);
        boolean ok2 = true;
        for (int i = 0; i < 1000; i++) {
            char c = (char)('a' + Math.random() * ('z' - 'a' + 1));
            if (c < 'a' || c > 'z') ok2 = false;
        }
        System.out.println(ok2);
    }
}
```

```output
true
true
```

مش هتقدر تطبع قيمة `Math.random()` في question لأن مفيش output ثابت — الأسئلة بتختبر حدود النطاق في loop.

## Stepwise Refinement

لما البرنامج كبير، بتقسّمه لـ sub-problems (divide and conquer):

- **Top-down**: تبدأ من فوق لـ تحت — تنفذ `main` الأول وتسيب الـ methods التانية **stubs** (نسخة بسيطة ناقصة مؤقتاً) وتكمّل واحد واحد.
- **Bottom-up**: تبدأ من تحت لـ فوق — تنفذ الـ methods الصغيرة الأول وتكتب test program لكل واحدة.

مثال PrintCalendar اتقسم لـ: `readInput`, `printMonth`, `printMonthTitle`, `printMonthBody`, `getStartDay`, `getTotalNumOfDays`, `getNumOfDaysInMonth`, `getMonthName`, `isLeapYear`. كل واحدة method لوحدها — كده تقدر تجرب كل جزء لوحده وتلاقي الـ bug بسهولة.

## الفخاخ اللي بتيجي في الامتحان

- **Signature ≠ return type**: ميثودين بنفس الاسم والباراميترز بس return type مختلف = "method already defined" Compile Error.
- **Missing return**: if/else-if من غير else أخير في ميثود بترجع قيمة = Compile Error حتى لو منطقياً مظبوط.
- `void` method مستخدمة كقيمة = Compile Error (`int x = print();`).
- ميثود instance (مش static) متنادت من `main` static من غير object = Compile Error.
- عدد أو نوع arguments غلط (String بدل int، أو argument ناقص) = Compile Error.
- `max(2.5, 3)` مع `max(int,int)` بس = Compile Error (double مش بيتحول لـ int). بس `f(5)` مع `f(double)` بس = شغالة (int→double widening).
- **Ambiguous invocation**: `max(int,double)` و `max(double,int)` مع `max(1,2)` = Compile Error.
- Pass by value: `swap(a,b)` مش بيغيّر المتغيرات الأصلية — ده سؤال output كلاسيكي.
- Array element بتتغير جوا الميثود (المرجع بيتبعت) لكن إعادة إسناد الـ array parameter مش بتأثر بره.
- Argument evaluation order: `f(g(1), g(2))` بتنفذ `g1` ثم `g2` ثم `f` — ترتيب الطباعة سؤال output مباشر.
- `Math.round(2.6)` بيرجع **long** — `int x = Math.round(2.6)` Compile Error، `Math.round(2.6f)` بيرجع int شغال.
- `Math.ceil/floor/rint` بيرجعوا double (`3.0`) مش int (`3`).
- `Math.sin(PI/6)` ≠ `0.5` بالظبط — `0.49999999999999994`. متقارنش بـ `==`.
- `Math.abs(Integer.MIN_VALUE)` لسه سالب — مفيش int موجب يقابله.
- `Math.min(-0.0, 0.0)` = `-0.0` و `Math.max` = `0.0` — صفر بإشارتين مختلفتين!
- Scope: `i` بتاع for مش بتشتغل بعد الـ loop؛ نفس الاسم في block متداخل = Compile Error (حتى لو السلايد بتقول "no errors" — هي فعلاً Compile Error).
- recursion لانهائية = `StackOverflowError`.
- `Math.random()` `[0.0, 1.0)` — 0 ممكن، 1 مستحيل.

## ملخص سريع

- Method = مجموعة statements بتعمل عملية — signature = name + parameter list (مش return type).
- Formal parameters في التعريف، actual arguments (قيم) عند النداء.
- value-returning لازم return في كل المسارات؛ void مفيش return بقيمة.
- الـ call stack: frame لكل call بتتشال عند الرجوع — recursion لانهائية = StackOverflowError.
- جافا pass by value — تغيير الـ parameter مش بيأثر على الأصل.
- Overloading: نفس الاسم parameter list مختلف — ambiguous = Compile Error.
- Scope الـ local variable: من إعلانه لنهاية blockه — إعادة تعريف في nested block = Compile Error.
- Method abstraction: reuse + information hiding + تقليل التعقيد.
- `Math.*` static methods: PI/E، trig بالـ radian، pow/sqrt/exp/log، ceil/floor/rint/round، min/max/abs/random.
- `Math.random()` ∈ [0.0, 1.0) — حوّلها لنطاق بالضرب والجمع.
- Stepwise refinement: top-down بـ stubs أو bottom-up بـ tests.

## الأسئلة

### سؤال 1: ميثود sum بتلغي تكرار الـ loop

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(sum(1, 10));
        System.out.println(sum(20, 30));
    }

    static int sum(int i1, int i2) {
        int sum = 0;
        for (int i = i1; i <= i2; i++) {
            sum += i;
        }
        return sum;
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
55
275
```

الميثود بتاخد حدودين وترجع المجموع — نفس الكود اتكتب مرة واتنده مرتين بقيم مختلفة. ده الـ reuse الأساسي.
</details>

### سؤال 2: max method بترجع قيمة

```java
public class Main {
    public static void main(String[] args) {
        int a = 5, b = 2;
        System.out.println(max(a, b));
        System.out.println(max(9, 4));
    }

    static int max(int num1, int num2) {
        int result;
        if (num1 > num2) {
            result = num1;
        } else {
            result = num2;
        }
        return result;
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
5
9
```

`max` بتاخد رقمين وبترجع الأكبر — `max(5,2)` = 5 و `max(9,4)` = 9. الـ return value بيتسند لطباعة println مباشرة.
</details>

### سؤال 3: نداء ميثود من كلاس تاني

```java
class Util {
    static int doubleIt(int x) {
        return x * 2;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(Util.doubleIt(21));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
42
```

المثود static في كلاس Util — بيناديها من Main بـ `ClassName.methodName`. ملاحظة: الكلاسين في نفس الملف ينفعوا بس واحد بس public.
</details>

### سؤال 4: ميثود void مع loop

```java
public class Main {
    public static void main(String[] args) {
        nPrintln("Welcome", 3);
    }

    static void nPrintln(String message, int n) {
        for (int i = 0; i < n; i++) {
            System.out.println(message);
        }
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
Welcome
Welcome
Welcome
```

الميثود void مش بترجع قيمة — بتعمل action (طباعة) وبس. الـ argument `3` بيحدد عدد التكرارات.
</details>

### سؤال 5: pass by value: swap

```java
class Swap {
    static void swap(int a, int b) {
        int t = a;
        a = b;
        b = t;
    }
}

public class Main {
    public static void main(String[] args) {
        int x = 1, y = 2;
        Swap.swap(x, y);
        System.out.println(x + " " + y);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
1 2
```

جافا pass by value — `swap` بدّل القيم المنسوخة في `a` و `b` بس، مش المتغيرين `x` و `y` الأصليين. يفضلوا 1 و 2.
</details>

### سؤال 6: overload resolution: int

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(f(5));
        System.out.println(f(5L));
        System.out.println(f(5.0f));
        System.out.println(f(5.0));
    }

    static int f(int x) { return 1; }
    static long f(long x) { return 2; }
    static double f(double x) { return 3; }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
1
2
3.0
3.0
```

الـ compiler بيختار أقرب نوع: `5` int بالظبط → int، `5L` long → long، `5.0f` float بيتحول double (مفيش long)، `5.0` double → double.
</details>

### سؤال 7: overload: char argument

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(f('a'));
        System.out.println(f(5));
    }

    static int f(int x) { return 10 + x; }
    static double f(double x) { return 20 + x; }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
107
15
```

`'a'` = 97 و char بيتحول لـ int أسهل من double — فاختار `f(int)` = 10+97=107. و `5` int برضه → 15.
</details>

### سؤال 8: int argument مع f(double) بس

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(f(5));
    }

    static double f(double x) { return x + 0.5; }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
5.5
```

مفيش `f(int)` — الـ `5` بيتحول تلقائياً لـ double (widening) وينادي `f(double)` = 5.5. int→double دايماً شغال.
</details>

### سؤال 9: max(2.5, 3) مع max(int,int) بس

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(max(2.5, 3));
    }

    static int max(int a, int b) {
        return a > b ? a : b;
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`2.5` double مش بيتحول لـ int — narrowing مش بيحصل أوتوماتيك في الـ method arguments. لازم `max(double,double)` overload أو cast.
</details>

### سؤال 10: double method بترجع int expression

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(f(3));
    }

    static double f(int x) { return x + 0.5; }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3.5
```

الميثود معلنة `double` بس بترجع `x + 0.5` — ده double أصلاً. لو رجّعت int expression زي `return x;` جافا بتحوله double أوتوماتيك (widening).
</details>

### سؤال 11: ambiguous invocation

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(max(1, 2));
    }

    static double max(int a, double b) { return a > b ? a : b; }
    static double max(double a, int b) { return a > b ? a : b; }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`max(1,2)` ينفع مع الاتنين overloads بنفس القوة — `1`→int للـ num1 و`2`→int للـ num2 في الاتنين. مفيش most specific = ambiguous invocation.
</details>

### سؤال 12: نفس الـ signature return مختلف

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(f(2));
    }

    static int f(int x) { return x; }
    static double f(int x) { return x * 1.5; }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


الـ signature = name + parameter list بس — return type مش جزء منها. ميثودين `f(int)` = duplicate method = Compile Error.
</details>

### سؤال 13: missing return في else-if

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(sign(3));
    }

    static int sign(int n) {
        if (n > 0) return 1;
        else if (n == 0) return 0;
        else if (n < 0) return -1;
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


الـ compiler مش متأكد إن في return reachable — لو شال الـ else-if الأخير حط `else return -1;` هيتصلح. دي أشهر غلطة في المحاضرة.
</details>

### سؤال 14: void method كقيمة

```java
public class Main {
    public static void main(String[] args) {
        int x = print();
    }

    static void print() { System.out.println("x"); }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`print()` return type بتاعها void — مينفعش تتحط في متغير int. 'void' type not allowed here.
</details>

### سؤال 15: instance method من static main

```java
public class Main {
    public static void main(String[] args) {
        foo();
    }

    void foo() { System.out.println("x"); }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`foo` instance method (مش static) — `main` static فمفيش object تنادي عليه. لازم `static void foo()` أو `new Main().foo()`.
</details>

### سؤال 16: argument type غلط

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(f("5"));
    }

    static int f(int x) { return x; }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`"5"` String مش بيتحول لـ int — `incompatible types: String cannot be converted to int`. String مش رقم حتى لو جواها أرقام.
</details>

### سؤال 17: عدد arguments ناقص

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(f());
    }

    static int f(int a) { return a; }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`f` محتاجة argument واحد — نداء `f()` = wrong number of arguments = Compile Error.
</details>

### سؤال 18: int method = double return

```java
public class Main {
    public static void main(String[] args) {
        int y = doubleM(3);
        System.out.println(y);
    }

    static double doubleM(int x) { return x * 2; }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`doubleM` بترجع double و`int y` مش بيستحمل double — narrowing محتاج cast `(int)doubleM(3)`.
</details>

### سؤال 19: int method ياخد double argument

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(intM(3.7));
    }

    static int intM(double x) { return (int)x; }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3
```

`3.7` double بيتحول للـ parameter `double` عادي، والـ `(int)x` جوه الميثود بيقص الكسر → 3. الـ cast جوه مش بره.
</details>

### سؤال 20: Math.round return type

```java
public class Main {
    public static void main(String[] args) {
        long r = Math.round(2.6);
        System.out.println(r);
        System.out.println(Math.round(2.6f));
        System.out.println(Math.round(-2.5));
        System.out.println(Math.round(-2.5f));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3
3
-2
-2
```

`Math.round(double)` بيرجع long و`Math.round(float)` بيرجع int — عشان كده `long r` استحملها. `round(-2.5)` = floor(-2.0) = -2 — بتقرّب لفوق بعد +0.5.
</details>

### سؤال 21: int = Math.round(double)

```java
public class Main {
    public static void main(String[] args) {
        int r = Math.round(2.6);
        System.out.println(r);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`Math.round(2.6)` argument double → return long — وlong مش بيتحول لـ int أوتوماتيك. `Math.round(2.6f)` كان هيرجع int ويشتغل.
</details>

### سؤال 22: Math.pow و sqrt

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(Math.pow(2, 3));
        System.out.println(Math.sqrt(4));
        System.out.println(Math.sqrt(10.5));
        System.out.println(Math.sqrt(4) == 2);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
8.0
2.0
3.24037034920393
true
```

`pow` و `sqrt` بيرجعوا double — `Math.pow(2,3)` = 8.0 مش 8. `Math.sqrt(4)` = 2.0 و `== 2` بيقارن double مع int → true.
</details>

### سؤال 23: Math.max/min/abs

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(Math.max(2, 3));
        System.out.println(Math.max(2.5, 3));
        System.out.println(Math.min(-0.0, 0.0));
        System.out.println(Math.max(-0.0, 0.0));
        System.out.println(Math.abs(-2));
        System.out.println(Math.abs(-2.1));
        System.out.println(Math.abs(Integer.MIN_VALUE));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3
3.0
-0.0
0.0
2
2.1
-2147483648
```

`max(2,3)` int → 3 و `max(2.5,3)` double → 3.0. `-0.0` و `0.0` مختلفين في Java! و `abs(MIN_VALUE)` لسه سالب — مفيش int موجب يكفيه.
</details>

### سؤال 24: Math.sin/cos حقيقية

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(Math.sin(Math.PI / 6));
        System.out.println(Math.cos(Math.PI / 2));
        System.out.println(Math.cos(Math.PI / 6));
        System.out.println(Math.sin(Math.PI / 2));
        System.out.println(Math.toRadians(90));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
0.49999999999999994
6.123233995736766E-17
0.8660254037844387
1.0
1.5707963267948966
```

السلايد بتقول sin(PI/6)=0.5 و cos(PI/2)=0 — الحقيقة: تقريب double بيطلع `0.49999999999999994` و `6.123233995736766E-17`. `toRadians(90)` = PI/2 ≈ 1.5707963267948966.
</details>

### سؤال 25: Math.exp/log/log10

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(Math.exp(1));
        System.out.println(Math.log(Math.E));
        System.out.println(Math.log10(1000));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
2.718281828459045
1.0
3.0
```

`exp(1)` = e ≈ 2.718281828459045، `log` طبيعي (ln) فـ log(E)=1.0، `log10(1000)` = 3.0.
</details>

### سؤال 26: ceil/floor/rint/round

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(Math.ceil(2.1));
        System.out.println(Math.ceil(-2.1));
        System.out.println(Math.floor(-2.1));
        System.out.println(Math.rint(2.5));
        System.out.println(Math.rint(3.5));
        System.out.println(Math.rint(-2.5));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3.0
-2.0
-3.0
2.0
4.0
-2.0
```

`ceil` لفوق دايماً: ceil(-2.1) = -2.0. `floor` لتحت: floor(-2.1) = -3.0. `rint` لأقرب **زوجي** في النص: rint(2.5)=2.0, rint(3.5)=4.0.
</details>

### سؤال 27: Math.round

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(Math.round(2.6));
        System.out.println(Math.round(-2.6));
        System.out.println(Math.round(2.5f));
        System.out.println(Math.round(-2.5f));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3
-3
3
-2
```

`round(x)` = floor(x+0.5): round(-2.6) = floor(-2.1) = -3، round(2.5f) = floor(3.0) = 3، round(-2.5f) = floor(-2.0) = -2..round(double) بيرجع long وround(float) بيرجع int.
</details>

### سؤال 28: random في نطاق 0-9

```java
public class Main {
    public static void main(String[] args) {
        boolean ok = true;
        for (int i = 0; i < 1000; i++) {
            int r = (int)(Math.random() * 10);
            if (r < 0 || r > 9) ok = false;
        }
        System.out.println(ok);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
true
```

`Math.random()` ∈ [0.0,1.0) — ضرب في 10 وقص يعطي دايماً 0..9. اللوب 1000 مرة للتأكد — مفيش output عشوائي لأننا بنطبع boolean مش الرقم.
</details>

### سؤال 29: random في نطاق 50-99

```java
public class Main {
    public static void main(String[] args) {
        boolean ok = true;
        for (int i = 0; i < 1000; i++) {
            int r = 50 + (int)(Math.random() * 50);
            if (r < 50 || r > 99) ok = false;
        }
        System.out.println(ok);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
true
```

`50 + (int)(Math.random()*50)` — العشوائي 0..49 يتزود 50 → دايماً 50..99. الـ +1 في النهاية مش محتاج لأن الضرب نفسه بيقص.
</details>

### سؤال 30: random حرف صغير

```java
public class Main {
    public static void main(String[] args) {
        boolean ok = true;
        for (int i = 0; i < 1000; i++) {
            char c = (char)('a' + Math.random() * ('z' - 'a' + 1));
            if (c < 'a' || c > 'z') ok = false;
        }
        System.out.println(ok);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
true
```

`('z'-'a'+1)` = 26 حرف — `'a' + Math.random()*26` بيطلع رقم بين 97 و 122 → cast لـ char يديله a-z دايماً.
</details>

### سؤال 31: ترتيب تنفيذ الـ arguments

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(f(g(1), g(2)));
    }

    static int g(int x) {
        System.out.println("g" + x);
        return x;
    }

    static int f(int a, int b) {
        return a * 10 + b;
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
g1
g2
12
```

الـ arguments بتتنفذ **قبل** النداء وبالترتيب من الشمال: g(1) تطبع g1 وترجع 1، g(2) تطبع g2 وترجع 2، وبعدين f(1,2) = 12.
</details>

### سؤال 32: i++ جوه argument

```java
public class Main {
    public static void main(String[] args) {
        int i = 1;
        System.out.println(max(i++, i));
        System.out.println(i);
    }

    static int max(int a, int b) { return a > b ? a : b; }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
2
2
```

`i++` بيرجع القيمة القديمة 1 وبعدين i بتبقى 2 — فالـ argument التاني `i` بيقرأ 2. max(1,2)=2 و i=2 بعد كده.
</details>

### سؤال 33: pass by value مع return

```java
public class Main {
    public static void main(String[] args) {
        int x = 5;
        inc(x);
        System.out.println(x);
        x += inc2(x);
        System.out.println(x);
    }

    static void inc(int n) { n = n + 1; }
    static int inc2(int n) { return n + 10; }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
5
20
```

`inc(x)` غيرت النسخة `n` بس — x فضل 5. `inc2(x)` رجّعت 15 و `x += 15` = 20.
</details>

### سؤال 34: array element vs reassign

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2};
        change(arr);
        System.out.println(arr[0]);
    }

    static void change(int[] x) {
        x[0] = 99;
        x = new int[]{7, 8};
        x[0] = 7;
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
99
```

`x[0]=99` غيرت المحتوى فالـ caller شافه. بس `x = new int[]{7,8}` غيّرت المرجع المحلي `x` بس — arr الأصلي مش اتأثر.
</details>

### سؤال 35: نفس اسم i في for loopين

```java
public class Main {
    public static void main(String[] args) {
        int s = 0;
        for (int i = 0; i < 2; i++) { s += i; }
        for (int i = 0; i < 3; i++) { s += i * 10; }
        System.out.println(s);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
31
```

الـ `i` في كل for ليها scope جوه الـ loop بتاعها بس — إعادة تعريفها في loop تاني **مش** خطأ لأن الـ blocks مش متداخلة.
</details>

### سؤال 36: loop variable بعد الـ loop

```java
public class Main {
    public static void main(String[] args) {
        for (int i = 1; i <= 2; i++) {
            System.out.print(i);
        }
        System.out.println(i);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`i` متعرفة في for-header — scope بتاعتها الـ loop كله بس. استخدامها في سطر `println(i)` بعد القوس = cannot find symbol.
</details>

### سؤال 37: variable جوه if بره

```java
public class Main {
    public static void main(String[] args) {
        if (true) {
            int x = 7;
        }
        System.out.println(x);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`x` scope بتاعها الـ if block — برّاه مش مرئية. نفس قاعدة أي block `{ }`.
</details>

### سؤال 38: redeclaration في nested block

```java
public class Main {
    public static void main(String[] args) {
        int i = 1;
        for (int i = 1; i < 10; i++) {
            i += 1;
        }
        System.out.println(i);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`i` موجودة في main scope والـ for-header جواه = nested blocks — إعادة تعريف = Compile Error. (السلايد علّمته no errors بالغلط — هو فعلاً Compile Error.)
</details>

### سؤال 39: parameter redefined كـ local

```java
public class Main {
    public static void main(String[] args) {
        foo(5);
    }

    static void foo(int p) {
        int p = 3;
        System.out.println(p);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`p` parameter والـ local `int p` في نفس الـ method body = duplicate variable — مينفعش تعيد تعريف parameter.
</details>

### سؤال 40: use before declaration

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(x);
        int x = 5;
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


المتغير لازم يتعرّف **قبل** الاستخدام — `println(x)` قبل `int x = 5` = cannot find symbol / illegal forward reference.
</details>

### سؤال 41: recursion printing

```java
public class Main {
    public static void main(String[] args) {
        rec(3);
    }

    static void rec(int n) {
        if (n > 0) {
            System.out.println(n);
            rec(n - 1);
        }
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3
2
1
```

كل call بيطبع n وينادي rec(n-1) — الـ call stack بيتملى frames لحد n=0 والـ frames بتتشال واحد واحد.
</details>

### سؤال 42: recursion لانهائية

```java
public class Main {
    public static void main(String[] args) {
        rec(1);
    }

    static void rec(int n) {
        rec(n + 1);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `java.lang.StackOverflowError`


`rec` بتنادي نفسها من غير شرط توقف — كل call بيضيف frame على الـ stack لحد ما الذاكرة تخلص = StackOverflowError.
</details>

### سؤال 43: char argument لـ int parameter

```java
public class Main {
    public static void main(String[] args) {
        System.out.println('a' + 1);
        System.out.println((char)('a' + 1));
        System.out.println(show('b'));
    }

    static int show(char c) { return c + 1; }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
98
b
99
```

`'a' + 1` = 98 كـ int، `(char)` بيرجّع 'b'. `show('b')` — char بيتحول لـ int parameter، و`c + 1` = 99 int.
</details>

### سؤال 44: gcd و isPrime

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(gcd(48, 18));
        System.out.println(isPrime(7));
        System.out.println(isPrime(9));
    }

    static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
6
true
false
```

`gcd(48,18)` = 6 بـ Euclidean algorithm. `isPrime(7)` = true (مفيش قاسم)، `isPrime(9)` = false (3×3).
</details>

### سؤال 45: ميثود بعد main — الترتيب مش مهم

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(doubleIt(10));
    }

    static int doubleIt(int x) {
        return x * 2;
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
20
```

جافا بتدور على الميثود في الكلاس كله مش بس اللي قبل `main` — الترتيب في الملف مش مهم.
</details>

### سؤال 46: overload بعدد parameters مختلف

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(f(1, 2));
        System.out.println(f(1));
    }

    static int f(int a, int b) { return a + b; }
    static int f(int a) { return a * 10; }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3
10
```

`f(1,2)` نداء للـ overload اللي بياخد 2 arguments → 3. `f(1)` للـ overload اللي بياخد واحد → 10. عدد الـ parameters بيفرّق الـ signature.
</details>

### سؤال 47: return; فاضية في value method

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(f(5));
    }

    static int f(int x) {
        if (x > 0) return x;
        return;
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`return;` من غير قيمة مش صالحة في ميثود بترجع int — لازم `return <value>;` دايماً. ('return' with no value is only for void methods.)
</details>

### سؤال 48: نظري: formal vs actual

1. formal = القيم عند النداء، actual = المتغيرات في التعريف
2. formal = المتغيرات في الـ header، actual = القيم عند النداء ✔
3. الاتنين نفس الحاجة
4. actual = اسم الميثود

<details>
<summary>الإجابة</summary>

**الإجابة:** formal = المتغيرات في الـ header، actual = القيم عند النداء


الـ formal parameters هي المتغيرات المعرّفة في method header (زي `num1`, `num2`)، والـ actual parameters/arguments هي القيم اللي بتتبعت عند النداء (زي `x`, `y`).Formal بتتكتب مرة في التعريف وactual بتتبعت كل مرة.
</details>

### سؤال 49: نظري: إيه الـ signature

1. name + return type + params
2. name + parameter list بس ✔
3. modifier + name
4. return type + name

<details>
<summary>الإجابة</summary>

**الإجابة:** name + parameter list بس


الـ method signature = اسم الميثود + parameter list (الأنواع والعدد). return type **مش** جزء من الـ signature — عشان كده مفيش overloading على return type بس.
</details>

### سؤال 50: نظري: void معناها

1. بترجع 0
2. بترجع null
3. مش بترجع قيمة — actions بس ✔
4. بترجع boolean

<details>
<summary>الإجابة</summary>

**الإجابة:** مش بترجع قيمة — actions بس


الميثود `void` مش بترجع قيمة — بتعمل actions بس (زي الطباعة). مينفعش تستخدمها في expression أو تسند ناتجها لمتغير.
</details>

### سؤال 51: نظري: فوائد الـ methods

1. أسرع تنفيذ دايماً
2. reuse + information hiding + تقليل التعقيد ✔
3. أمان أكتر من الأمان نفسه
4. مفيش فوائد — دي preference بس

<details>
<summary>الإجابة</summary>

**الإجابة:** reuse + information hiding + تقليل التعقيد


الـ method abstraction بيديك: reuse (تكتب مرة وتستخدم في أي حتة)، information hiding (الـ black box — المستخدم مش محتاج يعرف التفاصيل)، وتقليل التعقيد (تقسيم البرنامج لأجزاء صغيرة).
</details>

### سؤال 52: نظري: stub

1. نسخة كاملة من الميثود
2. نسخة ناقصة مؤقتة لاختبار النداء ✔
3. ميثود private
4. static method

<details>
<summary>الإجابة</summary>

**الإجابة:** نسخة ناقصة مؤقتة لاختبار النداء


الـ stub = نسخة بسيطة ناقصة مؤقتاً من method لسه متنفذتش — بتستخدمها في top-down approach عشان تقدر تختبر الـ caller قبل ما تخلص التفاصيل.
</details>

### سؤال 53: نظري: الـ call stack

1. بيخزن أسماء الميثودز بس
2. frame لكل call فيها params + locals ✔
3. مفيش call stack في جافا
4. بيخزن الـ return values بس

<details>
<summary>الإجابة</summary>

**الإجابة:** frame لكل call فيها params + locals


الـ call stack بيخزن frame لكل method call — كل frame فيه الـ parameters والـ local variables بتاعة النداء ده. لما الميثود تخلص الـ frame بتتشال (pop) والـ return value بيروح للـ caller.
</details>
