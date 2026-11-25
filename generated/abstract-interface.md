# Abstract Classes و Interfaces

## 1. الـ Abstract Class ليها Constructor

```java
abstract class A {
    A() {
        System.out.println("A-ctor");
    }

    abstract void m();
}

class B extends A {
    B() {
        System.out.println("B-ctor");
    }

    void m() {
        System.out.println("B.m");
    }
}

public class Main {
    public static void main(String[] args) {
        new B().m();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
A-ctor
B-ctor
B.m
```

رغم إن A abstract ومينفعش تعملها instantiate، الـ constructor بتاعها بينادى عادي لما تعمل `new B()` عن طريق `super()`. بعدين `m()` بتتنفذ على النسخة بتاعة B.
</details>

## 2. Interface Fields بتكون final تلقائيًا

```java
interface I {
    int X = 5;
}

class T implements I {
    void change() {
        X = 10;
    }
}

public class Main {
    public static void main(String[] args) {
        new T().change();
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


أي field جوه interface هو `public static final` ضمنيًا. `X = 10` محاولة تغيير final variable فـ javac بيفشل — ومينفعش تعمل implements من غير ما تتعامل معاها كـ constant.
</details>

## 3. حل الـ Diamond Problem يدويًا

```java
interface A {
    default void m() {
        System.out.println("A.m");
    }
}

interface B {
    default void m() {
        System.out.println("B.m");
    }
}

class C implements A, B {
    public void m() {
        System.out.println("C.m");
    }
}

public class Main {
    public static void main(String[] args) {
        new C().m();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
C.m
```

لما class بيعمل implements لـ interface اتنين فيهم `default m()` نفس الاسم، لازم يعمل override بنفسه عشان يحل التضارب. `C.m` هنا هي اللي بتتنفذ — ولو شالها كان هيبقى compile error.
</details>

## 4. Diamond Problem من غير حل

```java
interface A {
    default void m() {
        System.out.println("A.m");
    }
}

interface B {
    default void m() {
        System.out.println("B.m");
    }
}

class C implements A, B {
}

public class Main {
    public static void main(String[] args) {
        new C().m();
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`A` و`B` فيهم default methods بنفس الاسم و`C` مش حاسمة بينهم — الـ compiler مش بيعرف أنهي `m()` تنفذ، فبيرمي compile error لازم `C` تعمل override.
</details>

## 5. Static و Default Methods في Interface

```java
interface I {
    static void m() {
        System.out.println("I.m");
    }

    default void d() {
        System.out.println("I.d");
    }
}

class T implements I {
}

public class Main {
    public static void main(String[] args) {
        I.m();
        T t = new T();
        t.d();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
I.m
I.d
```

`static` methods في interface بتنادى باسم الـ interface بس ومبتتورثش للـ classes اللي بتعمل implements — عشان كده `I.m()` شغالة و`t.m()` كانت هتفشل. الـ `default` methods بتتورث عادي وبتتنفذ على أي instance.
</details>

## 6. Interface Methods public ضمنيًا

```java
interface I {
    void m();
}

class T implements I {
    void m() {
        System.out.println("T.m");
    }
}

public class Main {
    public static void main(String[] args) {
        new T().m();
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


أي method في interface هو `public` تلقائيًا، فالـ implementation لازم يكون `public` برضه. `void m()` من غير modifier صلاحيتها أضعف (package-private) فـ javac بيرفض.
</details>

## 7. Interface Extends Interface

```java
interface A {
    default void m() {
        System.out.println("A.m");
    }
}

interface B extends A {
}

class C implements B {
}

public class Main {
    public static void main(String[] args) {
        new C().m();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
A.m
```

`B extends A` بيرث الـ default method `m()`، و`C implements B` بياخدها هي كمان بالتوريث غير المباشر. `new C().m()` بتلاقي `A.m` فبتتنفذ عادي.
</details>
