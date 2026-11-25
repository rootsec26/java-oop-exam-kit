# وراثة و Constructor Chaining

## 1. ترتيب الـ Constructors في الوراثة

```java
class A {
    A() {
        System.out.println("A-ctor");
    }
}

class B extends A {
    B() {
        System.out.println("B-ctor");
    }
}

class C extends B {
    C() {
        System.out.println("C-ctor");
    }
}

public class Main {
    public static void main(String[] args) {
        new C();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
A-ctor
B-ctor
C-ctor
```

لما تعمل `new C()` الـ constructor بتاع C بينادي `super()` على طول قبل أي سطر، فالترتيب دايمًا من فوق لتحت: A وبعدين B وبعدين C.
</details>

## 2. Field Hiding مع Constructors

```java
class A {
    int x = 1;

    A() {
        x = 2;
        System.out.println("A x=" + x);
    }
}

class B extends A {
    int x = 10;

    B() {
        x = 20;
        System.out.println("B x=" + x);
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

**الناتج:**

```
A x=2
B x=20
```

الـ field `x` في B بيعمل hide للـ field في A — دول متغيرين مختلفين. جوه constructor بتاع A بيتكلم عن `x` بتاع A (بقيمة 2)، وجوه constructor بتاع B بيتكلم عن `x` بتاع B (بقيمة 20).
</details>

## 3. Constructor بينادي Method متعملها Override

```java
class A {
    A() {
        show();
    }

    void show() {
        System.out.println("A.show");
    }
}

class B extends A {
    B() {
        super();
    }

    void show() {
        System.out.println("B.show");
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

**الناتج:**

```
B.show
```

`show()` اتندهت من جوه constructor بتاع A بس الـ dynamic dispatch شغال: الكائن فعليًا من نوع B فالنسخة اللي بتتنفذ هي `B.show`. الحقول بس هي اللي بتتملّى بالترتيب، الـ methods بتتعملها dispatch عادي.
</details>

## 4. الفرق بين super و this

```java
class A {
    void hi() {
        System.out.println("A.hi");
    }
}

class B extends A {
    void hi() {
        System.out.println("B.hi");
    }

    void test() {
        super.hi();
        hi();
    }
}

public class Main {
    public static void main(String[] args) {
        new B().test();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
A.hi
B.hi
```

`super.hi()` بينادي نسخة الأب صراحةً حتى لو الـ method متعملها override، بينما `hi()` العادية بتستخدم الـ dynamic dispatch فبتنادي `B.hi`.
</details>

## 5. مفيش Default Constructor في الأب

```java
class A {
    A(int x) {
    }
}

class B extends A {
    B() {
        System.out.println("hi");
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


لما عرّفت `A(int x)` مفيش constructor فاضي اتعمل تلقائيًا في A، فالـ `super()` الضمني اللي في `B()` مش لاقي constructor يناديه — javac بيفشل.
</details>

## 6. ترتيب الـ Instance Initializer Blocks

```java
class A {
    {
        System.out.println("A-init");
    }

    A() {
        System.out.println("A-ctor");
    }
}

class B extends A {
    {
        System.out.println("B-init");
    }

    B() {
        System.out.println("B-ctor");
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

**الناتج:**

```
A-init
A-ctor
B-init
B-ctor
```

الترتيب: `super()` → instance init block بتاع الأب → constructor بتاع الأب → instance init block بتاع الابن → constructor بتاع الابن. الـ init block بيشتغل بعد الـ super() وقبل باقي جسم الـ constructor.
</details>

## 7. Static Fields بتتعملها Hiding مش Override

```java
class A {
    static int v = 1;
}

class B extends A {
    static int v = 2;
}

public class Main {
    public static void main(String[] args) {
        A a = new B();
        B b = new B();
        System.out.println(a.v + " " + b.v + " " + B.v + " " + A.v);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
1 2 2 1
```

`B.v` بيعمل hide لـ `A.v` — دول متغيرين منفصلين. الوصول للـ static field بيتحدد من الـ compile-time type: `a` معرّف كـ A فياخد `A.v` رغم إن الكائن B.
</details>
