# Casting و instanceof

## 1. Upcasting و Downcasting

```java
class A {
}

class B extends A {
    void m() {
        System.out.println("B.m");
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new B();
        B b = (B) a;
        b.m();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
B.m
```

`A a = new B()` upcasting تلقائي وآمن. `(B) a` downcasting رجّع النوع الفرعي — شغال هنا لأن الكائن runtime بتاعه B فعلًا. `b.m()` بتتنفذ عادي.
</details>

## 2. Downcasting الغلط بيرمي ClassCastException

```java
class A {
}

class B extends A {
    void m() {
        System.out.println("B.m");
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new A();
        B b = (B) a;
        b.m();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `java.lang.ClassCastException`


الـ cast `(B) a` بيترجم عادي (downcast قانوني)، بس الـ runtime بيتحقق: الكائن `a` نوعه A مش B فبيرمي `ClassCastException` قبل ما توصل `b.m()`.
</details>

## 3. instanceof قبل الـ Cast

```java
public class Main {
    public static void main(String[] args) {
        Object o = "hello";
        if (o instanceof String) {
            String s = (String) o;
            System.out.println(s.length());
        } else {
            System.out.println("not string");
        }
        Object n = 42;
        System.out.println(n instanceof String);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
5
false
```

`instanceof` بتشيك الـ runtime type — `o` فعلًا String فالـ cast آمن و`length()` بتطبع 5. `42` مش String فـ `instanceof` بترجع false من غير ما يعمل cast خالص.
</details>

## 4. Cast بين نوعين مالهمش علاقة

```java
class A {
}

class B {
}

public class Main {
    public static void main(String[] args) {
        A a = new A();
        B b = (B) a;
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`A` و`B` classes منفصلين — مفيش inheritance بينهم. `(B) a` cast مش ممكن أبدًا لأن مفيش object يقدر يكون الاتنين، فالـ compiler بيرفض بـ "inconvertible types".
</details>

## 5. الـ Cast لـ Interface بيترجم بس بيفشل runtime

```java
class A {
}

interface I {
    void m();
}

public class Main {
    public static void main(String[] args) {
        A a = new A();
        I i = (I) a;
        i.m();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `java.lang.ClassCastException`


الكود `(I) a` بيترجم عادي لأن أي class ممكن تكون هتعمل implements للـ interface يومًا — بس A مش هتعمل كده، فالـ runtime بيرمي `ClassCastException` على طول.
</details>

## 6. instanceof مع null

```java
public class Main {
    public static void main(String[] args) {
        Object o = null;
        System.out.println(o instanceof String);
        System.out.println(o instanceof Object);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
false
false
```

`null instanceof أي حاجة` بترجع false دايمًا — null مش object من أي نوع. حتى `instanceof Object` false لأنها مش instance حقيقية.
</details>

## 7. Type Erasure بيخلي الـ Cast للـ Generics مش آمن

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List raw = new ArrayList();
        raw.add("hello");
        List<Integer> nums = (List<Integer>) raw;
        int n = nums.get(0);
        System.out.println(n);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `java.lang.ClassCastException`


الـ cast `(List<Integer>) raw` بيترجم بس مع unchecked warning — الـ generics مش موجودة في الـ runtime. لما `get(0)` بيرجع String والـ assignment لـ `int n` بيحاول unbox String → `ClassCastException`.
</details>
