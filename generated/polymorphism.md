# Polymorphism

## 1. Overloading مش Polymorphism

```java
class A {
    void m(Object o) {
        System.out.println("Object");
    }
}

class B extends A {
    void m(String s) {
        System.out.println("String");
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new B();
        a.m("x");
        new B().m("x");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
Object
String
```

`B.m(String)` ده overload جديد مش override، فالـ compiler بيختار الـ method من الـ compile-time type. `a` معرّف كـ A فبيلاقي بس `m(Object)`، بينما `new B()` بيشوف النسختين فيختار `m(String)` كأقرب match.
</details>

## 2. Static Methods بتتعملها Hiding

```java
class A {
    static void m() {
        System.out.println("A.m");
    }
}

class B extends A {
    static void m() {
        System.out.println("B.m");
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new B();
        B b = new B();
        a.m();
        b.m();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
A.m
B.m
```

الـ static methods مبتتعملهاش override — بيتعملها hiding والاختيار بيحصل وقت الـ compile. `a.m()` الـ compiler شايف `a` نوعه A فاختار `A.m` حتى لو الكائن runtime بتاعه B.
</details>

## 3. Override Annotation بتتحقق من Override حقيقي

```java
class A {
    void m() {
    }
}

class B extends A {
    @Override
    void n() {
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


`@Override` معناها إن الـ method المفروض تكون بتعمل override لـ method في superclass. `n()` مفيهاش أصل في A فالـ annotation بتفشل الـ compilation.
</details>

## 4. اختيار الـ Overload

```java
class T {
    void m(int x) {
        System.out.println("int");
    }

    void m(long x) {
        System.out.println("long");
    }

    void m(String s) {
        System.out.println("String");
    }

    void m(Object o) {
        System.out.println("Object");
    }
}

public class Main {
    public static void main(String[] args) {
        T t = new T();
        t.m(5);
        t.m(5L);
        t.m(null);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
int
long
String
```

`m(5)` بيختار `int` (أدق match بدون widening)، `m(5L)` بيختار `long`، و`m(null)` بيختار `String` لأنه أكثر نوع specific — الـ compiler بيختار أضيق نوع ممكن من غير ما يعمل boxing.
</details>

## 5. Dynamic Dispatch جوه Array

```java
class Shape {
    void area() {
        System.out.println("Shape");
    }
}

class Circle extends Shape {
    void area() {
        System.out.println("Circle");
    }
}

class Square extends Shape {
    void area() {
        System.out.println("Square");
    }
}

public class Main {
    public static void main(String[] args) {
        Shape[] shapes = {new Circle(), new Square(), new Shape()};
        for (Shape s : shapes) {
            s.area();
        }
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
Circle
Square
Shape
```

الـ array نوعه `Shape[]` بس كل عنصر runtime بتاعه نوع مختلف. النداء `s.area()` بيحصل runtime على حسب نوع الكائن الفعلي — ده الـ polymorphism الحقيقي.
</details>

## 6. Instance Method مينفعش تعمل Override لـ Static

```java
class A {
    static void m() {
    }
}

class B extends A {
    void m() {
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


`A.m` static و`B.m` instance بنفس الـ signature — ده مش override قانوني، javac بيرفض: "overridden method is static". لازم static يقابل static وinstance يقابل instance.
</details>

## 7. الـ Private Methods مبتتعملهاش Override

```java
class A {
    private void m() {
        System.out.println("A.m");
    }

    void call() {
        m();
    }
}

class B extends A {
    void m() {
        System.out.println("B.m");
    }

    void callB() {
        m();
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new B();
        a.call();
        new B().callB();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
A.m
B.m
```

`B.m` مش override لـ `A.m` لأنها private — private members مبتتورثش أصلاً، فهي مجرد method جديدة صدفةً بنفس الاسم. `call()` جوه A بينادي `A.m` دايمًا لأنها بتتشاف جوه A.
</details>
