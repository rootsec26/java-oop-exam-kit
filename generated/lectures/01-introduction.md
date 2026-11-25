# مقدمة عن البرامج وجافا — المحاضرة 1

دي أول محاضرة: إزاي الكمبيوتر بيفهم الأوامر، وليه جافا اتعملت أصلاً، وإيه شكل أول برنامج جافا. المحاضرة دي نظرية في معظمها بس فيها anatomy كامل لأول برنامج — واللي هيتسأل منه في الامتحان نظري وعملي.

## إزاي الكمبيوتر بيفهمنا

الكمبيوتر مش بيفهم لغة البشر — بيفهم **machine language**: أوامر binary (صفر وواحد) مبنية جوه كل جهاز. تكتب برنامج بيها؟tedious ومش هتعرف تقراه.

**Assembly language** اتحلّت المشكلة جزئياً: أوامر أقرب للإنسان زي `ADDF3 R1, R2, R3`، بس لسه مش عملية — ولازم **assembler** يحوّلها لـ machine code قبل التشغيل.

**High-level languages** زي جافا و C++ إنجليزية شبه طبيعية: `area = 5 * 5 * 3.1415;` — سهلة التعلم والكتابة.

## compiler و interpreter

برنامج high-level اسمه **source program** والكمبيوتر مش فاهمه — محتاج ترجمة:

- **Compiler**: بيترجم السورس مرة واحدة لكود خاص بالجهاز (**object program**)، وبعدها **linker** بيربطه بمكتبات ويطلّع **executable**.
- **Interpreter**: بيترجم وينفّذ سطر سطر وقت التشغيل.
- جافا بتعمل الاتنين: `javac` بيترجم لـ **bytecode**، والـ **JVM** بيفسّر الـ bytecode وينفّذه.

## ليه جافا؟

جافا اتعملت عشان الـ Internet — "Java is the Internet programming language". نقاط قوتها ( characteristics ):

- **Simple**: أسهل من C++ (ناس بتسميها "C++--").
- **Object-Oriented**: مبنية على OOP من الأول.
- **Distributed**:Networking مدمج — برنامج على أكتر من جهاز.
- **Interpreted**: الـ JVM بيفسّر bytecode.
- **Robust**: الـ compiler بيمسك أخطاء كتير قبل التشغيل + runtime exception handling.
- **Secure**: آليات أمان بتحمي النظام.
- **Architecture-Neutral**: الـ bytecode مش خاص بجهاز معين.
- **Portable**: "Write once, run anywhere" — نفس الـ `.class` يشتغل على أي جهاز فيه JVM من غير إعادة ترجمة.
- **Multithreaded** و **Dynamic**: threads مدمجة، وكود جديد يتحمّل أثناء التشغيل.

## إصدارات JDK

| Edition | الاستخدام |
|---|---|
| J2SE | تطبيقات client-side و applets — الكورس ده بيستخدمها |
| J2EE | تطبيقات server-side زي servlets و JSP |
| J2ME | أجهزة محمولة زي الموبايلات |

## javac و java — دورة العمل

1. تكتب السورس `Welcome.java`
2. `javac Welcome.java` → بيطلّع `Welcome.class` (bytecode — مش تقراه بإيدك، ده للـ JVM)
3. `java Welcome` → الـ JVM يفسّر الـ bytecode وينفّذ

لو فيه syntax error الـ `javac` بيقف — مفيش class بيتعمل. ولو الـ class اتعملت بس فيه logic error، الـ `java` هيشتغل ويطلع ناتج غلط.

## أول برنامج — Anatomy

```java run
public class Welcome {
    public static void main(String[] args) {
        System.out.println("Welcome to Java!");
    }
}
```

```output
Welcome to Java!
```

تفكيك البرنامج:

- `public class Welcome` — **class**: قالب/blueprint للأوبجكتس. البرنامج بيتعرف بكلاس أو أكتر. الـ class public لازم اسم الملف = اسمها (`Welcome.java`).
- `public static void main(String[] args)` — **main method**: نقطة الدخول — الـ JVM بيدور عليها وينفّذ البرنامج من خلالها. `static` عشان تتنده من غير object، `void` لأنها مش بترجع قيمة.
- `{ }` — **block**: بيجمّع الكود جواها. في **class block** (جسم الكلاس كله) و **method block** (جسم الميثود).
- `System.out.println("...");` — **statement**: أمر واحد بينتهي بـ `;`. `println` **method** جاهزة في مكتبة جافا بتطبع سطر في الـ console.

## التعليقات Comments

3 أنواع — مش بتأثر على التنفيذ خالص:

- `//` line comment — لحد آخر السطر
- `/* ... */` paragraph comment — سطر أو أكتر
- `/** ... */` javadoc — لتوثيق الكلاسات والميثودز، بتتطلع HTML بـ `javadoc`

```java run
public class Welcome {
    public static void main(String[] args) {
        // سطر تعليق
        /* تعليق
           على كذا سطر */
        /** تعليق javadoc */
        System.out.println("Hello");
    }
}
```

```output
Hello
```

## Reserved Words و Modifiers

**Reserved words** كلمات ليها معنى خاص للـ compiler ومينفعش تتستخدم كأسماء — زي `class`, `public`, `static`, `void`. لو كتبت `int class = 5;` = Compile Error.

**Modifiers** كلمات محجوزة بتحدد خصائص البيانات والميثودز والكلاسات — زي `public` و `static` اللي في سطر `main`. `public` معناها الكلاس/الميثود/المتغير متاح لبرامج تانية، `private` العكس.

## أكتر من statement و method calls

أي عدد statements جوا الـ main block بينفذوا بالترتيب، وتقدر تنادي نفس الميثود بأكتر من argument:

```java run
public class Demo {
    public static void main(String[] args) {
        System.out.println("First");
        System.out.println("Second");
        {
            System.out.println("Inside block");
        }
        System.out.println("Last");
    }
}
```

```output
First
Second
Inside block
Last
```

الـ block المنفرد `{ }` جوا الميثود شغال عادي — بس أي متغير متعرف جواه مش بيبان برّاه.

## JOptionPane

جافا بتديك `JOptionPane.showMessageDialog` من مكتبة `javax.swing` عشان تطلع رسالة في dialog window بدل الـ console. وفيه طريقتين:

```java
JOptionPane.showMessageDialog(null, "Welcome to Java!", "Display Message", JOptionPane.INFORMATION_MESSAGE);
JOptionPane.showMessageDialog(null, "Welcome to Java!");
```

## الفخاخ اللي بتيجي في الامتحان

- الكلاس `public` لازم اسم الملف = اسم الكلاس — `public class Welcome` جوا `Main.java` = Compile Error. (الكلاس من غير `public` ممكن اسم مختلف، بس main لازم تكون في الكلاس اللي `java` بيناديه.)
- لازم `public static void main(String[] args)` بالظبط عشان الـ JVM يلاقيله — أي تغيير في الـ signature (زي `main(String args)` أو من غير `static`) = البرنامج بيترجم بس `java` بيقول "Main method not found".
- `javac` بيطلّع `.class` (bytecode) مش `.exe` — الـ bytecode مش machine code خاص بجهاز.
- `System.out` بحرف صغير — `system.out.println` = Compile Error (case-sensitive).
- من غير فاصلة منقوطة `;` في آخر الـ statement = Compile Error.
- التعليقات مش بتتنفذ — متتوقعش أي output منها.
- `//` بتخلص عند نهاية السطر — لو كتبت كود على نفس السطر بعد `//` هيتعامل كتعليق ومش هيترجم.
- reserved words مينفعش تتستخدم كأسماء متغيرات/كلاسات.
- الـ compiler بيترجم، الـ JVM بيفسّر — جافا مش "interpreted بس" ولا "compiled بس"، الاتنين مع بعض.
- الـ bytecode machine-independent — ده سر "write once, run anywhere".
- J2ME للموبايلات، J2EE للسيرفر، J2SE للديسكتوب — الامتحان بيسأل التمييز بينهم.

## ملخص سريع

- Machine language = binary، Assembly = أوامر للمجمّع، High-level = إنجليزي شبه طبيعي.
- Compiler بيترجم مرة واحدة لـ object/executable؛ Interpreter بيفسّر سطر سطر.
- جافا: `javac` → bytecode، `java` + JVM → تنفيذ.
- Bytecode machine-independent → portable → "write once, run anywhere".
- الـ OS برنامج بيدير الهاردوير والتطبيقات مش بتشتغل من غيره.
- Java characteristics: Simple, Object-Oriented, Distributed, Interpreted, Robust, Secure, Architecture-Neutral, Portable, Multithreaded, Dynamic.
- JDK editions: J2SE (desktop)، J2EE (server)، J2ME (mobile).
- `public class` لازم يطابق اسم الملف.
- `main` لازم `public static void main(String[] args)` عشان البرنامج يشتغل.
- Statement بينتهي بـ `;`؛ `{ }` block؛ الكلاس template للأوبجكتس.
- 3 أنواع comments: `//`، `/* */`، `/** */` (javadoc).
- Reserved words و modifiers كلمات محجوزة للـ compiler.

## الأسئلة

### سؤال 1: أول برنامج Welcome

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Welcome to Java!");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
Welcome to Java!
```

أبسط برنامج جافا: الكلاس Main فيه main method بتطبع رسالة بـ println — لازم `public static void main(String[] args)` عشان الـ JVM يشتغل.
</details>

### سؤال 2: من غير فاصلة منقوطة

```java
public class Main {
    public static void main(String[] args) {

        System.out.println("Hello")
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


كل statement في جافا لازم تنتهي بـ semicolon `;` — من غيرها الـ compiler مش فاهم فين الأمر خلص = syntax error.
</details>

### سؤال 3: حساسية حالة الأحرف

```java
public class Main {
    public static void main(String[] args) {

        system.out.println("Hello");
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


جافا case-sensitive — `system` بحرف صغير مش نفس `System`، فالـ compiler مش لاقي الرمز = cannot find symbol.
</details>

### سؤال 4: اسم الكلاس ≠ اسم الملف

```java
public class Welcome {
    public static void main(String[] args) {
        System.out.println("hi");
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


الكلاس `public` لازم اسم الملف يكون `Welcome.java` مش `Main.java` — javac بيرفض: class Welcome is public, should be declared in a file named Welcome.java.
</details>

### سؤال 5: reserved word كاسم متغير

```java
public class Main {
    public static void main(String[] args) {

        int public = 5;
        System.out.println(public);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`public` كلمة محجوزة للـ compiler (modifier) — مينفعش تتستخدم كاسم متغير. نفس القاعدة على class و static و void وغيرهم.
</details>

### سؤال 6: أنواع التعليقات التلاتة

```java
public class Main {
    public static void main(String[] args) {
        // line comment
        /* paragraph
           comment */
        /** javadoc comment */
        System.out.println("Hello");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
Hello
```

التلاتة أنواع تعليقات بتتجاهل تماماً — `//` لسطر واحد، `/* */` لعدة أسطر، `/** */` لـ javadoc. مفيش ولا سطر comment بيطبع.
</details>

### سؤال 7: statements و blocks بالترتيب

```java
public class Main {
    public static void main(String[] args) {

        System.out.println("First");
        System.out.println("Second");
        {
            System.out.println("Inside block");
        }
        System.out.println("Last");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
First
Second
Inside block
Last
```

الـ statements بتتنفذ بالترتيب اللي مكتوبة بيه. الـ block المنفرد `{ }` شغال جوا الميثود — بس أي متغير جواه مش بيبان برّاه.
</details>

### سؤال 8: من غير main method

```java
public class Main {
    public static void helper() {
        System.out.println("hi");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `MainMethodNotFound`


البرنامج بيترجم عادي لأن مفيش syntax error، بس `java Main` مش بيلاقي `public static void main` فيشتغل — الـ JVM بيقول Main method not found.
</details>

### سؤال 9: main signature غلط

```java
public class Main {
    public static void main(String args) {
        System.out.println("hi");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `MainMethodNotFound`


الـ JVM بيدور على `main(String[])` بالظبط — `main(String args)` ميثود عادية مش entry point، فبيترجم عادي بس `java` بيقول Main method not found.
</details>

### سؤال 10: قوس ناقص

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("hi");
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


قوس `{` مفتوح وماتقفلش — الـ compiler بيوصل لآخر الملف ومش لاقي القوس الناقص = reached end of file while parsing.
</details>

### سؤال 11: classname في كلاس تاني

```java
class Helper {
    static void greet() {
        System.out.println("from helper");
    }
}

public class Main {
    public static void main(String[] args) {
        Helper.greet();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
from helper
```

ممكن كذا class في نفس الملف — بس واحد بس public واسمه = اسم الملف. `Helper` من غير public فمفيش مشكلة، و`Helper.greet()` بينادي ميثود static على الكلاس مباشرة.
</details>

### سؤال 12: سطرين println

```java
public class Main {
    public static void main(String[] args) {

        System.out.print("A");
        System.out.println("B");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
AB
```

`print` بتطبع من غير سطر جديد و`println` بتطبع وتحط newline — فالناتج `AB` على نفس السطر.
</details>

### سؤال 13: نظري: إيه اللي بيطلّع object program

1. compiler ✔
2. interpreter
3. linker
4. JVM

<details>
<summary>الإجابة</summary>

**الإجابة:** compiler


الـ compiler هو اللي بيترجم الـ source program لـ object program (machine language). الـ interpreter بيتعامل مع bytecode في جافا — والـ linker بيربط الـ object files بالمكتبات قبل التنفيذ.
</details>

### سؤال 14: نظري: إيه الـ bytecode

1. machine code خاص بجهاز واحد
2. كود وسطي للـ JVM يشتغل على أي جهاز ✔
3. سورس كود قابل للترجمة
4. ملف تنفيذي نهائي

<details>
<summary>الإجابة</summary>

**الإجابة:** كود وسطي للـ JVM يشتغل على أي جهاز


الـ bytecode كود خاص بالـ JVM مش بجهاز معين — عشان كده نفس ملف `.class` يشتغل على Windows أو Mac أو Linux من غير إعادة ترجمة، بشرط وجود JVM.
</details>

### سؤال 15: نظري: أنهي edition للموبايلات

1. J2SE
2. J2EE
3. J2ME ✔
4. Java ME for Servers

<details>
<summary>الإجابة</summary>

**الإجابة:** J2ME


J2ME (Java Micro Edition) اتعملت للتطبيقات على الأجهزة المحمولة زي الموبايلات والـ PDAs. J2SE للديسكتوب و J2EE للسيرفر — والكورس بيستخدم J2SE.
</details>

### سؤال 16: نظري: write once run anywhere

1. لازم تعيد الترجمة على كل جهاز
2. نفس الـ bytecode يشتغل على أي JVM من غير إعادة ترجمة ✔
3. جافا بتشتغل بس على Windows
4. البرنامج بيتكتب بلغة واحدة لكل جهاز

<details>
<summary>الإجابة</summary>

**الإجابة:** نفس الـ bytecode يشتغل على أي JVM من غير إعادة ترجمة


العبارة معناها إنك بتكتب البرنامج مرة واحدة والـ bytecode الناتج يشتغل على أي جهاز فيه JVM — من غير ما تعيد الترجمة لكل platform زي ما بيحصل مع لغات compiled تانية.
</details>
