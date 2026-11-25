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
