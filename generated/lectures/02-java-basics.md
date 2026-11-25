# أساسيات جافا — المتغيرات والأنواع والعمليات

دي المحاضرة التانية: أول برنامج حقيقي فيه متغيرات وعمليات حسابية. الفكرة كلها إنك بتخزن بيانات في **variables**، وبتتعامل معاها بـ **operators**، والجافا بتفرض عليك قواعد صارمة في الأنواع عشان تحميك من أخطاء كتير — بس نفس القواعد دي هي اللي بتهيّئ معظم فخاخ الامتحان.

## المتغيرات Variables

المتغير هو مكان في الذاكرة ليه اسم ونوع. بتعرّف المتغير بنوعه وبعدين تقدر تدي له قيمة أو تغيّرها:

```java run
int x = 5;
double radius = 2.5;
char grade = 'A';
boolean done = false;
x = x + 1;
System.out.println(x);
System.out.println(radius);
System.out.println(grade);
System.out.println(done);
```

```output
6
2.5
A
false
```

- الإعلان (declaration) بيحدد النوع والاسم: `int x;`
- الإسناد (assignment) بيحط قيمة: `x = 10;`
- تقدر تعلن وتعمل initialize في سطر واحد: `int x = 1;`
- المتغير اللي جوه block (بين `{ }`) مش شايفه بره الـ block — استخدامه بره = Compile Error.
- المتغير مش بيتعمله initialize لوحده — استخدامه قبل ما تاخد قيمة = Compile Error.

## الثوابت Constants

كلمة `final` معناها إن القيمة متتغيرش أبداً. أي محاولة إعادة إسناد = Compile Error:

```java run
final double PI = 3.14159;
final int SIZE = 3;
System.out.println(PI * SIZE);
```

```output
9.424769999999999
```

## الأنواع الرقمية Numeric Types

دي أهم جدول في المحاضرة — احفظه:

| النوع | الحجم | المدى |
|---|---|---|
| `byte` | 8 bit | -128 إلى 127 |
| `short` | 16 bit | -32768 إلى 32767 |
| `int` | 32 bit | -2147483648 إلى 2147483647 |
| `long` | 64 bit | رقم ضخم جداً، لازم اللاحقة `L` |
| `float` | 32 bit | عدد عشري بدقة أقل، لازم اللاحقة `f` |
| `double` | 64 bit | العدد العشري الافتراضي في جافا |
| `char` | 16 bit | رمز Unicode واحد |
| `boolean` | — | `true` أو `false` بس |

## الليترالات Literals

الـ literal هو قيمة ثابتة مكتوبة جوه الكود زي `34` أو `5.0`. القواعد:

- أي رقم صحيح من غير لاحقة بيتعامل كـ `int`. لو كبير أوي على int لازم `L` في الآخر: `long big = 10000000000L;` — من غير L = Compile Error.
- أي رقم عشري من غير لاحقة بيتعامل كـ `double`. لو عايزه `float` لازم `f` في الآخر: `float f = 100.2f;` — `float f = 100.2;` من غير f = Compile Error لأن 100.2 double.
- تقدر تستخدم scientific notation: `1.23456e2` يعني 123.456، و `1.23456e-2` يعني 0.0123456.

```java run
double d = 1.23456e2;
float f = 100.2f;
long big = 1234567890123L;
System.out.println(d);
System.out.println(f);
System.out.println(big);
```

```output
123.456
100.2
1234567890123
```

## العمليات الحسابية Operators

| Operator | المعنى | مثال | ناتج |
|---|---|---|---|
| `+` | جمع | `34 + 1` | `35` |
| `-` | طرح | `34.0 - 0.1` | `33.9` |
| `*` | ضرب | `300 * 30` | `9000` |
| `/` | قسمة | `1.0 / 2.0` | `0.5` |
| `%` | باقي القسمة | `20 % 3` | `2` |

**أهم قاعدة:** القسمة بين عددين صحيح int بتدي int — الكسر بيترمي:

```java run
System.out.println(5 / 2);
System.out.println(5.0 / 2);
System.out.println(5 % 2);
System.out.println(-7 % 3);
```

```output
2
2.5
1
-1
```

لاحظ إن `%` بياخد إشارة المقسوم (dividend): `-7 % 3` = `-1` و `7 % -3` = `1`. ولو قسمت int على صفر `1 / 0` بيحصل **ArithmeticException** — exception حقيقي بيقع وقت التشغيل.

## دقة الأرقام العشرية — الفخ الأكبر

الأرقام العشرية متخزنة تقريباً مش بالظبط. عشان كده:

```java run
System.out.println(1.0 - 0.9);
System.out.println(0.1 + 0.2);
System.out.println(1.0 - 0.1 - 0.1 - 0.1 - 0.1 - 0.1);
```

```output
0.09999999999999998
0.30000000000000004
0.5000000000000001
```

يعني **مقارنة doubles بـ `==` خطيرة** — `0.1 + 0.2 == 0.3` بيطلع `false` رغم إنهم المفروض يساووا. الأعداد الصحيحة int بتتخزن بالظبط 100%.

## ترتيب العمليات

الضرب والقسمة و `%` قبل الجمع والطرح، والأقواس بتكسب كل حاجة، والعمليات بتتنفذ من الشمال لليمين لو نفس الأولوية:

```java run
System.out.println(2 + 3 * 4);
System.out.println((2 + 3) * 4);
System.out.println(10 - 4 - 3);
System.out.println(20 / 5 / 2);
System.out.println(2 + 3 * 4 % 5);
```

```output
14
20
3
2
4
```

## العمليات المختصرة ++ و --

| Operator | الوصف |
|---|---|
| `i++` | بيرجع القيمة **القديمة** وبعدين يزيد 1 |
| `++i` | بيزيد 1 وبعدين بيرجع القيمة **الجديدة** |
| `i--` / `--i` | نفس الفكرة للنقص |

```java run
int i = 10;
int n = 10 * i++;
System.out.println(n);
System.out.println(i);
int m = 10 * ++i;
System.out.println(m);
System.out.println(i);
```

```output
100
11
120
12
```

وفي `i = i++` القيمة القديمة بترجع وتتكتب تاني فوق التزايد — فـ `i` بيفضل زي ما هو. متستخدمش `++` على نفس المتغير مرتين في تعبير واحد زي `int k = ++i + i` — نتيجته `12` لما `i` كان 5، وده من أصعب الحاجات في الامتحان.

العمليات المختصرة للتعيين: `+=` `-=` `*=` `/=` `%=` — مثال `i += 8` يعني `i = i + 8`. ودي ليها سحر تاني: لو `b` نوعه `byte`، `b += 5` بتشتغل عادي بينما `b = b + 5` = Compile Error.

## تحويل الأنواع Type Conversion

لما العملية فيها نوعين مختلفين، جافا بتحوّل الأصغر لنوع الأكبر تلقائياً — السلسلة من الأصغر للأكبر:

```
byte → short → int → long → float → double
                    ↘ char
```

يعني `int` في عملية مع `double` بتتحول لـ `double`، و `long` مع `float` بتتحول لـ `float` (مش long! لأن float أعلى في السلسلة). القواعد بالترتيب: double يكسب، بعده float، بعده long، ولو الاتنين int يبقوا int.

التحويل الضمني (widening) آمن ومجاني: `double d = 3;` شغالة. التحويل الصريح (narrowing) لازم cast بالقوسين وبيضيّع الكسر: `(int)3.9` = `3` و `(int)-3.9` = `-3` (بيشيل الكسر مش بيقرّب).

```java run
System.out.println((int)3.9);
System.out.println((int)-3.9);
System.out.println(3 / 2);
System.out.println(3 / 2.0);
double d = 3;
System.out.println(d);
```

```output
3
-3
1
1.5
3.0
```

## char و Unicode و Escape Sequences

`char` بيخزن رمز Unicode واحد (16-bit). تقدر تكتبه بـ character literal `'A'` أو unicode escape `'A'` (نفس الحرف A). الـ escape sequences للرموز الخاصة:

| Escape | المعنى | Unicode |
|---|---|---|
| `\n` | سطر جديد | `\u000A` |
| `\t` | tab | `\u0009` |
| `\b` | backspace | `\u0008` |
| `\r` | carriage return | `\u000D` |
| `\\` | backslash | `\u005C` |
| `\'` | single quote | `\u0027` |
| `\"` | double quote | `\u0022` |

`char` بيتعامل كرقم في العمليات: `'a'` قيمتها 97. `'a' + 1` بيطلع `int` قيمته 98، و `(char)('a' + 1)` بيرجع `'b'`. و `++` شغالة على char برضه: `char ch = 'a'; ++ch;` → `'b'`. و `char c = 97;` يعطي `'a'`، و `int i = 'a';` يعطي `97`.

```java run
char ch = 'a';
System.out.println(++ch);
System.out.println('a' + 1);
System.out.println((char)('a' + 1));
System.out.println('A');
System.out.println('\u0041');
System.out.println("Tab\there");
System.out.println("Back\\slash");
```

```output
b
98
b
A
A
Tab	here
Back\slash
```

## String والدمج Concatenation

`String` مش نوع primitive — هو **reference type** (كلاس جاهز في المكتبة). بتتعمل بـ double quotes `"Hello"` — الـ single quotes للـ char بس.

لما تحط `+` مع String في أي مكان في التعبير، كل حاجة بتتحول لنص وتتلزق:

```java run
String s = "Chapter" + 2;
String s1 = "Supplement" + 'B';
System.out.println(s);
System.out.println(s1);
System.out.println("1" + 2 + 3);
System.out.println(1 + 2 + "3");
String a = new String("Hi");
String b = new String("Hi");
System.out.println(a == b);
System.out.println(a.equals(b));
```

```output
Chapter2
SupplementB
123
33
false
true
```

لاحظ الترتيب مهم: `"1" + 2 + 3` = `"123"` لأن الدمج بدأ من الشمال، لكن `1 + 2 + "3"` = `"33"` لأن الجمع اتعمل الأول قبل ما يوصل للـ String. و `==` على Strings بتقارن المرجع مش المحتوى — استخدم `equals()`.

## أسلوب التسمية Naming Conventions

- أسماء المتغيرات والميثودز: camelCase — `radius`، `computeArea`
- أسماء الكلاسات: PascalCase — `ComputeArea`
- الثوابت: CAPITAL_SNAKE — `PI`، `MAX_VALUE`
- الـ identifier لازم يبدأ بحرف أو `_` أو `$`، ميبدأش برقم، وممنوع يكون reserved word أو `true`/`false`/`null`.

## أنواع الأخطاء Errors

| النوع | إمتى | مثال |
|---|---|---|
| Syntax Error | الـ compiler | من غير فاصلة منقوطة `;` |
| Runtime Error | والبرنامج شغال | `1 / 0` → ArithmeticException |
| Logic Error | البرنامج بيطبع ناتج غلط | شرط غلط في `if` |

الـ debugging: تتبع البرنامج بإيدك، أو حط `println` تشوف القيم، أو استخدم debugger ( breakpoint، تتبع خطوة خطوة). ملاحظة: `1.0 / 0` مش بيقع — بيطبع `Infinity`، و `0.0 / 0` بيطبع `NaN`، لأن القسمة العشرية بتتعامل مع اللانهاية بطريقة خاصة.

## قراءة الإدخال Input

جافا بتديك طريقتين للإدخال: كونسول بـ `Scanner` أو dialog بـ `JOptionPane`. الـ Scanner بيتعمل كده:

```java run
import java.util.Scanner;
Scanner input = new Scanner(System.in);
System.out.println("Scanner ready");
```

```output
Scanner ready
```

وميثودزه `nextInt()` و `nextDouble()` إلخ بترجع int أو double على طول. وأهم نقطة للامتحان: اللي بيرجع من `JOptionPane.showInputDialog` هو **String دايماً**، فلازم تحوله بـ `Integer.parseInt("42")` أو `Double.parseDouble("2.5")` — و `parseInt("abc")` بيقع بـ `NumberFormatException`.

## الفخاخ اللي بتيجي في الامتحان

- `5 / 2` = `2` مش `2.5` — القسمة int بترمي الكسر. ولو عايز كسر حط `.` في أي رقم: `5 / 2.0`.
- `int x = 5 / 2.0` = **Compile Error** لأن ناتج القسمة double ومش بيتحول لـ int من غير cast.
- `-7 % 3` = `-1` — إشارة `%` بتتبع المقسوم مش المقسوم عليه.
- `1.0 - 0.9` ≠ `0.1` — متقارنش doubles بـ `==`.
- `float f = 100.2` = **Compile Error** — لازم `f` في الآخر. و `long x = 9999999999` برضه Compile Error — لازم `L`.
- `byte b = 1000` = Compile Error، و `byte b = 10; b = b + 5;` برضه Compile Error لأن ناتج الجمع int — بس `b += 5` شغالة.
- `int k = ++i + i` و `i = i++` — دي أسئلة output مباشرة في الامتحان.
- `'a' + 1` = `98` (int مش char!)، لازم `(char)` لو عايز char.
- `"1" + 2 + 3` ≠ `1 + 2 + "3"` — ترتيب الدمج بيحدد الناتج.
- `char c = 'a' + 1` **مش** Compile Error لأنها constant expression — بس `char c = 'a' + x` (x متغير) = Compile Error.
- `1 / 0` ArithmeticException لكن `1.0 / 0` = `Infinity` — الفرق int/double بيغيّر كل حاجة.
- `Integer.MAX_VALUE + 1` بيلف للناقص — integer overflow.
- متستخدمش `int x;` قبل ما تديها قيمة، ومتستخدمهاش بره الـ block بتاعها — الاتنين Compile Error.
- `(int)3.9` = `3` و `(int)-3.9` = `-3` — الـ cast بيقص الكسر مش بيقرّب.
- فلوسك: `amount * 100` ممكن يطلع `1155.9999...` في حالات تانية — `(int)` بيقص، فلو حابب السنتات صح راح `Math.round`.

## ملخص سريع

- `int` القسمة بترمي الكسر؛ أي رقم فيه `.` أو `e` = double؛ `float` محتاج `f` و `long` محتاج `L`.
- `%` باقي قسمة إشارته بتتبع المقسوم: `-7 % 3 = -1`.
- الأرقام العشرية تقريبية: `0.1 + 0.2 == 0.30000000000000004`.
- `++i` بيرجع الجديد، `i++` بيرجع القديم — و`i = i++` مبيغيرش i.
- `+=` ورفقاتها بتعمل implicit narrowing فبتشتغل مع byte/short.
- التحويل التلقائي من الأصغر للأكبر: byte→short→int→long→float→double.
- `(int)` cast بيقص الكسر: `(int)-3.9 = -3`.
- `'a'` = 97، `char` بيتعامل كرقم و`++` شغالة عليه.
- `+` مع String في أي مكان بيحوّل الباقي لنص — والترتيب من الشمال لليمين.
- `String` reference type — `==` بتقارن المرجع، استخدم `equals()`.
- `final` = ثابت، إعادة الإسناد Compile Error.
- متغير غير مهيأ أو مستخدم بره blockه = Compile Error.
- `1 / 0` exception لكن `1.0 / 0` = `Infinity`.
- أخطاء: syntax (compiler)، runtime (بيقع)، logic (ناتج غلط).

## الأسئلة

### سؤال 1: قسمة صحيحة وباقي القسمة

```java
public class Main {
    public static void main(String[] args) {

        int a = 17, b = 5;
        System.out.println(a / b);
        System.out.println(a % b);
        System.out.println(5 / 2);
        System.out.println(5.0 / 2);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3
2
2
2.5
```

القسمة بين int و int بتدي int والكسر بيترمي. `5 / 2` = 2 لكن `5.0 / 2` = 2.5 لأن واحد من الرقمين double.
</details>

### سؤال 2: باقي القسمة مع أرقام سالبة

```java
public class Main {
    public static void main(String[] args) {

        System.out.println(-7 % 3);
        System.out.println(7 % -3);
        System.out.println(-7 % -3);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
-1
1
-1
```

نتيجة `%` في جافا بتاخد إشارة المقسوم (الرقم اللي على الشمال) مش المقسوم عليه.
</details>

### سؤال 3: دقة الأرقام العشرية

```java
public class Main {
    public static void main(String[] args) {

        System.out.println(1.0 - 0.9);
        System.out.println(0.1 + 0.2);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
0.09999999999999998
0.30000000000000004
```

الأرقام العشرية double متخزنة تقريباً — `0.1 + 0.2` مش بتساوي `0.3` بالظبط. عشان كده `==` على doubles خطيرة.
</details>

### سؤال 4: ليترالات وأسس علمية

```java
public class Main {
    public static void main(String[] args) {

        double d = 1.23456e2;
        float f = 100.2f;
        long big = 1234567890123L;
        System.out.println(d);
        System.out.println(f);
        System.out.println(big);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
123.456
100.2
1234567890123
```

`e2` معناها ×100، واللاحقة `f` بتخلي الرقم float واللاحقة `L` بتخلي الرقم long.
</details>

### سؤال 5: أولوية العمليات

```java
public class Main {
    public static void main(String[] args) {

        System.out.println(2 + 3 * 4);
        System.out.println((2 + 3) * 4);
        System.out.println(10 - 4 - 3);
        System.out.println(20 / 5 / 2);
        System.out.println(2 + 3 * 4 % 5);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
14
20
3
2
4
```

الضرب والقسمة و`%` قبل الجمع والطرح، والأقواس بتكسب. `10 - 4 - 3` بتتنفذ من الشمال = `(10-4)-3` = 3.
</details>

### سؤال 6: العمليات المختصرة

```java
public class Main {
    public static void main(String[] args) {

        int i = 10;
        i += 5;
        i *= 2;
        i -= 3;
        i /= 4;
        i %= 5;
        System.out.println(i);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
1
```

نتبع الخطوات: 10+5=15، ×2=30، −3=27، ÷4=6 (قسمة صحيحة)، %5=1.
</details>

### سؤال 7: الزيادة بعد القيمة i++

```java
public class Main {
    public static void main(String[] args) {

        int i = 10;
        int n = 10 * i++;
        System.out.println(n);
        System.out.println(i);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
100
11
```

`i++` بيرجع القيمة القديمة 10 في التعبير (10×10=100) وبعدين بيزود i لـ 11.
</details>

### سؤال 8: الزيادة قبل القيمة ++i

```java
public class Main {
    public static void main(String[] args) {

        int i = 10;
        int n = 10 * ++i;
        System.out.println(n);
        System.out.println(i);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
110
11
```

`++i` بيزود i لـ 11 الأول وبعدين بيرجع القيمة الجديدة — 10×11=110.
</details>

### سؤال 9: فخ i = i++

```java
public class Main {
    public static void main(String[] args) {

        int i = 5;
        i = i++;
        System.out.println(i);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
5
```

`i++` بيرجع القيمة القديمة 5 وبيسجل إن i هتبقى 6، بس الإسناد بيكتب الـ 5 القديمة فوقها — i بيفضل 5.
</details>

### سؤال 10: تعبير فيه ++i و i

```java
public class Main {
    public static void main(String[] args) {

        int i = 5;
        int k = ++i + i;
        System.out.println(k);
        System.out.println(i);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
12
6
```

`++i` بيخلي i=6 ويرجع 6، وبعدين التاني `i` في التعبير بيقرأ 6 — المجموع 12. استخدام ++ على نفس المتغير مرتين في تعبير = فخ.
</details>

### سؤال 11: ++ على متغير char

```java
public class Main {
    public static void main(String[] args) {

        char ch = 'a';
        ch++;
        char c2 = 'a';
        System.out.println(ch);
        System.out.println(ch == c2);
        System.out.println(++ch);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
b
false
c
```

`ch++` حوّل 'a' لـ 'b' فرجع false في المقارنة مع 'a'، و`++ch` كمان حوّل 'b' لـ 'c'. char بيتعامل كرقم Unicode.
</details>

### سؤال 12: حسابات char و التحويل

```java
public class Main {
    public static void main(String[] args) {

        System.out.println('a' + 1);
        System.out.println((char)('a' + 1));
        System.out.println("" + 'a' + 1);
        System.out.println('a' + 'b' + "c");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
98
b
a1
195c
```

`'a' + 1` = 98 كـ int مش char. `"" + 'a'` بيبدأ دمج String فبقى 'a' نص. `'a' + 'b'` = 195 (97+98) وبعدين اتلحق بـ "c".
</details>

### سؤال 13: ترتيب دمج Strings والأرقام

```java
public class Main {
    public static void main(String[] args) {

        System.out.println("1" + 2 + 3);
        System.out.println(1 + 2 + "3");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
123
33
```

الدمج بيتنفذ من الشمال لليمين: `"1" + 2` بيبقى نص "12" وبعدين +3 = "123". أما `1 + 2` اتجمع رقماً =3 وبعدين اتلحق بـ "3".
</details>

### سؤال 14: == مقابل equals على String

```java
public class Main {
    public static void main(String[] args) {

        String a = new String("Hi");
        String b = new String("Hi");
        System.out.println(a == b);
        System.out.println(a.equals(b));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
false
true
```

`==` بتقارن مرجع الكائنين (مكانهم في الذاكرة) فـ false رغم إن المحتوى واحد. `equals` بتقارن المحتوى فـ true.
</details>

### سؤال 15: متغيرات بأنواع مختلفة

```java
public class Main {
    public static void main(String[] args) {

        int x = 5;
        double radius = 2.5;
        char grade = 'A';
        boolean done = false;
        x = x + 1;
        System.out.println(x);
        System.out.println(radius);
        System.out.println(grade);
        System.out.println(done);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
6
2.5
A
false
```

المتغير بيتحفظ بنوعه: int بتطبع رقم صحيح، double برقم عشري، char برمز، boolean بـ true/false.
</details>

### سؤال 16: التحويل الضمني والصريح

```java
public class Main {
    public static void main(String[] args) {

        System.out.println((int)3.9);
        System.out.println((int)-3.9);
        System.out.println(3 / 2);
        System.out.println(3 / 2.0);
        double d = 3;
        System.out.println(d);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3
-3
1
1.5
3.0
```

الـ cast `(int)` بيقص الكسر في الاتجاه للصفر: 3.9→3 و -3.9→-3. `double d = 3` تحويل ضمني صحيح.
</details>

### سؤال 17: escape sequences و Unicode

```java
public class Main {
    public static void main(String[] args) {

        char ch = 'a';
        System.out.println(++ch);
        System.out.println('a' + 1);
        System.out.println('A');
        System.out.println('\u0041');
        System.out.println("Tab\there");
        System.out.println("Back\\slash");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
b
98
A
A
Tab	here
Back\slash
```

`\u0041` بيرمز لحرف A. `\t` tab و `\\` backslash واحد. unicode escape بيتكتب 4 hex digits بعد \u.
</details>

### سؤال 18: دمج Strings

```java
public class Main {
    public static void main(String[] args) {

        String s = "Chapter" + 2;
        String s1 = "Supplement" + 'B';
        System.out.println(s);
        System.out.println(s1);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
Chapter2
SupplementB
```

أي `+` فيها String بيحوّل الطرف التاني لنص ويلزقه — char 'B' اتحولت لـ "B".
</details>

### سؤال 19: parseInt و parseDouble

```java
public class Main {
    public static void main(String[] args) {

        System.out.println(Integer.parseInt("42") + 1);
        System.out.println(Double.parseDouble("2.5") * 2);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
43
5.0
```

`parseInt` و `parseDouble` بيحوّلوا String لرقم — لازم يكونوا أرقام صالحة وإلا NumberFormatException.
</details>

### سؤال 20: حساب الباقي بالفلوس ComputeChange

```java
public class Main {
    public static void main(String[] args) {

        double amount = 11.56;
        int remaining = (int)(amount * 100);
        int dollars = remaining / 100;
        remaining = remaining % 100;
        int quarters = remaining / 25;
        remaining = remaining % 25;
        int dimes = remaining / 10;
        remaining = remaining % 10;
        int nickels = remaining / 5;
        int pennies = remaining % 5;
        System.out.println(dollars);
        System.out.println(quarters);
        System.out.println(dimes);
        System.out.println(nickels);
        System.out.println(pennies);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
11
2
0
1
1
```

`11.56 * 100` = 1156.0000000000002 تقريباً و`(int)` قصّه لـ 1156. الباقي: 11 دولار، 2 ربع دولار (50 سنت)، 0 دايم، 1 نيكل، 1 بنس.
</details>

### سؤال 21: قواعد تحويل النوع في العمليات

```java
public class Main {
    public static void main(String[] args) {

        byte i = 100;
        long k = i * 3 + 4;
        double d = i * 3.1 + k / 2;
        System.out.println(k);
        System.out.println(d);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
304
462.0
```

`i * 3 + 4` كله int operations = 304. في `i * 3.1` الـ byte اتحول double، و`k / 2` قسمة long = 152.
</details>

### سؤال 22: مثال السلايدات عن دقة float

```java
public class Main {
    public static void main(String[] args) {

        System.out.println(1.0 - 0.1 - 0.1 - 0.1 - 0.1 - 0.1);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
0.5000000000000001
```

السلايد نفسها بتقول إن الناتج 0.5000000000000001 مش 0.5 — تقريب الأرقام العشرية بيأكل الدقة في كل عملية.
</details>

### سؤال 23: += بتعمل narrowing ضمني

```java
public class Main {
    public static void main(String[] args) {

        byte b = 100;
        b += 100;
        System.out.println(b);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
-56
```

`b += 100` جافا بتعمل cast ضمني فبتتخزن 200 في byte — و200 مش بيستحمل في byte (-128..127) فبيلف لـ -56.
</details>

### سؤال 24: integer overflow

```java
public class Main {
    public static void main(String[] args) {

        int m = Integer.MAX_VALUE;
        m = m + 1;
        System.out.println(m);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
-2147483648
```

`Integer.MAX_VALUE` = 2147483647 — الزيادة بـ 1 بتعمل overflow وبتلف لأول قيمة في المدى السالب.
</details>

### سؤال 25: قسمة على صفر: double

```java
public class Main {
    public static void main(String[] args) {

        System.out.println(1.0 / 0);
        System.out.println(0.0 / 0);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
Infinity
NaN
```

قسمة الأعداد العشرية على صفر مش بتقع — double بتتعامل مع اللانهاية: `1.0/0` = Infinity و `0.0/0` = NaN. الفرق عن int اللي بيقع بـ ArithmeticException.
</details>

### سؤال 26: char كرقم وكنص

```java
public class Main {
    public static void main(String[] args) {

        char c = 97;
        int i = 'a';
        System.out.println(c);
        System.out.println(i);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
a
97
```

`char c = 97` = 'a' لأن char بيتخزن كقيمة Unicode. `int i = 'a'` = 97 — التحويل بين char والأرقام تلقائي.
</details>

### سؤال 27: double من قسمة صحيحة

```java
public class Main {
    public static void main(String[] args) {

        double d = 3 / 2;
        System.out.println(d);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
1.0
```

العملية `3 / 2` بتحصل الأول كـ int = 1، وبعدها النتيجة 1 بتتحول لـ double = 1.0. عشان تطلع 1.5 لازم `3 / 2.0`.
</details>

### سؤال 28: معرّفات صحيحة

```java
public class Main {
    public static void main(String[] args) {

        int _x = 1;
        int $y = 2;
        int a1 = 3;
        System.out.println(_x + $y + a1);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
6
```

`_x` و `$y` و `a1` كلهم معرّفات صحيحة — الـ identifier ممكن يبدأ بحرف أو `_` أو `$` ويحتوي أرقام بعد كده.
</details>

### سؤال 29: byte كبير أوي

```java
public class Main {
    public static void main(String[] args) {

        byte b = 1000;
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`byte` مداه -128 إلى 127 — الليترال 1000 مش بيتحط في byte فيرمي Compile Error (incompatible types).
</details>

### سؤال 30: int x = 5 / 2.0

```java
public class Main {
    public static void main(String[] args) {

        int x = 5 / 2.0;
        System.out.println(x);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`5 / 2.0` ناتجها double 2.5 ومش ممكن تتحول لـ int من غير cast — Java مش بتضيّع الكسر لوحدها.
</details>

### سؤال 31: float من غير f

```java
public class Main {
    public static void main(String[] args) {

        float f = 100.2;
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


الليترال `100.2` double افتراضياً — عشان تحطه في float لازم `100.2f`. تحويل double لـ float narrowing = Compile Error.
</details>

### سؤال 32: long من غير L

```java
public class Main {
    public static void main(String[] args) {

        long x = 9999999999;
        System.out.println(x);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


الليترال `9999999999` أكبر من int فمحتاج `L` في الآخر — من غيرها javac بيعتبره int ويقول integer number too large.
</details>

### سؤال 33: byte = byte + int

```java
public class Main {
    public static void main(String[] args) {

        byte b = 10;
        b = b + 5;
        System.out.println(b);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`b + 5` نوعه int وint مش بيتحول لـ byte من غير cast. الحل: `b = (byte)(b + 5)` أو `b += 5` اللي بتعمل cast ضمني.
</details>

### سؤال 34: final وإعادة الإسناد

```java
public class Main {
    public static void main(String[] args) {

        final int x = 5;
        x = 6;
        System.out.println(x);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`final` معناها الثابت متتغيرش — أي assignment تاني ليها Compile Error.
</details>

### سؤال 35: متغير غير مهيأ

```java
public class Main {
    public static void main(String[] args) {

        int x;
        System.out.println(x);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


المتغير المحلي لازم ياخد قيمة قبل الاستخدام — `int x;` لوحدها مش كفاية، javac بيرفض.
</details>

### سؤال 36: متغير بره الـ block

```java
public class Main {
    public static void main(String[] args) {

        if (true) {
            int y = 5;
        }
        System.out.println(y);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`y` متعرف جوه الـ if block فمش مرئي برّاه — scope بتاع المتغير هو الـ block اللي اتعرف فيه.
</details>

### سؤال 37: تعبير مش statement

```java
public class Main {
    public static void main(String[] args) {

        int x = 1;
        x + 1;
        System.out.println(x);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


منذ Java 2 مش أي expression ينفع statement — المسموح: assignment، `op=`, `++/--` بس. `x + 1;` بيمسح نتيجته فـ Compile Error.
</details>

### سؤال 38: كلمة محجوزة كاسم

```java
public class Main {
    public static void main(String[] args) {

        int class = 3;
        System.out.println(class);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`class` كلمة محجوزة (reserved word) معناها خاص للمترجم — مينفعش تتستخدم كاسم متغير.
</details>

### سؤال 39: identifier بيبدأ برقم

```java
public class Main {
    public static void main(String[] args) {

        int 3abc = 1;
        System.out.println(3abc);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


الـ identifier مينفعش يبدأ برقم — لازم يبدأ بحرف أو `_` أو `$`.
</details>

### سؤال 40: char = char + متغير

```java
public class Main {
    public static void main(String[] args) {

        int x = 1;
        char c = 'a' + x;
        System.out.println(c);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`'a' + x` نوعه int ومش constant expression عشان كده مفيش narrowing تلقائي — لازم `(char)('a' + x)`.
</details>

### سؤال 41: قسمة int على صفر

```java
public class Main {
    public static void main(String[] args) {

        System.out.println(1 / 0);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `java.lang.ArithmeticException`


القسمة الصحيحة على صفر بترمي ArithmeticException وقت التشغيل. `/` على double مش بيعمل كده — `1.0/0` = Infinity.
</details>

### سؤال 42: parseInt على نص مش رقم

```java
public class Main {
    public static void main(String[] args) {

        System.out.println(Integer.parseInt("abc"));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `java.lang.NumberFormatException`


`parseInt` بيحاول يحوّل "abc" لرقم فبيفشل بـ NumberFormatException — لازم النص يكون رقم صالح.
</details>

### سؤال 43: تحويل الأنواع التلقائي

1. int بيتحول لـ double جوه العملية مع double ✔
2. double بيتحول لـ int أوتوماتيك
3. byte بيتحول لـ char دايماً
4. مفيش تحويل تلقائي خالص

<details>
<summary>الإجابة</summary>

**الإجابة:** int بيتحول لـ double جوه العملية مع double


جافا بتحوّل تلقائياً من النوع الأصغر للأكبر في سلسلة byte→short→int→long→float→double. لما `int` يقابل `double` في عملية، الـ int بيتحول لـ double — مش العكس أبداً.
</details>

### سؤال 44: تسمية المتغيرات

1. computeArea ✔
2. Compute_Area_2
3. compute-area
4. 2computeArea

<details>
<summary>الإجابة</summary>

**الإجابة:** computeArea


الـ naming conventions في جافا: variables و methods بـ camelCase زي `computeArea`، classes بـ PascalCase زي `ComputeArea`، و constants بـ CAPITAL_SNAKE زي `MAX_VALUE`.
</details>

### سؤال 45: أنواع الأخطاء

1. SyntaxError بيكتشفه الـ compiler ✔
2. RuntimeError بيكتشفه الـ compiler
3. LogicError بيوقف البرنامج دايماً
4. مفيش فرق بين syntax و runtime

<details>
<summary>الإجابة</summary>

**الإجابة:** SyntaxError بيكتشفه الـ compiler


Syntax errors بيكتشفها الـ compiler قبل التشغيل، runtime errors بتقع وقت التنفيذ زي القسمة على صفر، و logic errors أخطر نوع لأنها بتشتغل وبتطبع ناتج غلط من غير ما حد ياخد باله.
</details>

### سؤال 46: float literal

1. float f = 100.2f; ✔
2. float f = 100.2;
3. float f = (float)100.2d;
4. الاتنين B و C صح

<details>
<summary>الإجابة</summary>

**الإجابة:** float f = 100.2f;


الليترال العشري الافتراضي double — لو عايزه float لازم لاحقة `f` أو `F`. `float f = 100.2f` صح و `float f = 100.2F` صح برضه.
</details>
