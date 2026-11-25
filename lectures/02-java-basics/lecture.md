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
