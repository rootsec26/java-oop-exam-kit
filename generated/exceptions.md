# Exceptions

## 1. ترتيب قفل الـ Resources

```java
class R implements AutoCloseable {
    private final String name;

    R(String name) {
        this.name = name;
    }

    public void close() {
        System.out.println("close-" + name);
    }
}

public class Main {
    public static void main(String[] args) {
        try (R a = new R("a"); R b = new R("b")) {
            System.out.println("body");
        }
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
body
close-b
close-a
```

الـ try-with-resources بيقفل الـ resources بترتيب عكسي من إنشائها — `b` اتقفل قبل `a`. الـ close() بينادي حتى لو الـ try خلص عادي أو حصل exception.
</details>

## 2. الـ Return في Finally بيعمل Override

```java
public class Main {
    static int m() {
        try {
            throw new RuntimeException("boom");
        } catch (Exception e) {
            System.out.println("caught");
            return 1;
        } finally {
            System.out.println("finally");
            return 3;
        }
    }

    public static void main(String[] args) {
        System.out.println(m());
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
caught
finally
3
```

الـ `return 3` جوه finally بيشتغل آخر حاجة وبيستبدل أي return تاني — حتى اللي في الـ catch. فالنتيجة 3 مش 1، والـ return بتاع الـ catch بيتلغى.
</details>

## 3. ترتيب الـ Catch مهم —Subclass الأول

```java
public class Main {
    public static void main(String[] args) {
        try {
            System.out.println("try");
        } catch (Exception e) {
            System.out.println("catch-ex");
        } catch (RuntimeException e) {
            System.out.println("catch-runtime");
        } finally {
            System.out.println("finally");
        }
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`RuntimeException` extends `Exception`، فـ `catch (Exception)` قبلها بيلتقط كل حاجة والـ catch التانية مش هتوصلها أبدًا — javac بيرفض "exception RuntimeException has already been caught".
</details>

## 4. Checked Exceptions لازم throws

```java
public class Main {
    static void m() {
        throw new Exception("checked");
    }

    public static void main(String[] args) {
        m();
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`Exception` checked exception — لازم الـ method يعلن `throws Exception` أو يعمل catch ليها. `m()` مش معلنة عن حاجة فـ javac بيفشل بـ "unreported exception".
</details>

## 5. الـ Override مينفعش يوسّع الـ throws

```java
class A {
    void m() throws java.io.IOException {
        System.out.println("A.m");
    }
}

class B extends A {
    void m() throws Exception {
        System.out.println("B.m");
    }
}

public class Main {
    public static void main(String[] args) {
        new B();
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`B.m` بيعمل override لـ `A.m` اللي معلنة `throws IOException` — بس B بتعلن `throws Exception` الأوسع. ده مش قانوني: الـ override لازم يعلن نفس الـ exceptions أو أقل/أضيق.
</details>

## 6. الـ Finally بيشتغل حتى مع Return

```java
public class Main {
    static int m() {
        try {
            System.out.println("try");
            return 1;
        } finally {
            System.out.println("finally");
        }
    }

    public static void main(String[] args) {
        System.out.println(m());
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
try
finally
1
```

الـ `return 1` مش بيخرج فورًا — الـ finally block بيشتغل الأول وبعدين الـ return بيكمل. عشان كده "finally" بتتطبع قبل ما الـ method ترجع.
</details>

## 7. الـ Catch المش متطابق مش بيمسك الـ Exception

```java
public class Main {
    static void m() {
        try {
            int[] a = new int[1];
            a[2] = 5;
        } catch (NullPointerException e) {
            System.out.println("npe");
        }
    }

    public static void main(String[] args) {
        m();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `java.lang.ArrayIndexOutOfBoundsException`


`a[2] = 5` على array طولها 1 بيرمي `ArrayIndexOutOfBoundsException` مش `NullPointerException` — الـ catch الوحيدة مش بتلقطه فبيطلع من الـ method ويقع الـ program.
</details>

## 8. Custom Checked Exception

```java
class MyException extends Exception {
    MyException(String msg) {
        super(msg);
    }
}

public class Main {
    static void risky() throws MyException {
        System.out.println("before");
        throw new MyException("custom");
    }

    public static void main(String[] args) {
        try {
            risky();
        } catch (MyException e) {
            System.out.println("caught: " + e.getMessage());
        } finally {
            System.out.println("done");
        }
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
before
caught: custom
done
```

`MyException` extends `Exception` فهي checked — لازم `risky()` تعلن `throws MyException` والـ caller يعمل catch. الـ catch بيمسكها بالاسم و`getMessage()` بترجع الرسالة اللي اتبعتت للـ super.
</details>
