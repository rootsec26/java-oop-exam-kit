# Access Modifiers و Packages

## 1. Private يعني نفس الـ Class بس

```java
class A {
    private int x = 5;
}

public class Main {
    public static void main(String[] args) {
        System.out.println(new A().x);
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`x` private في A، فمحدش بره A يقدر يوصلها — حتى مش.Main` اللي في نفس الملف. javac بيفشل بـ "x has private access".
</details>

## 2. Protected يعني Package + Subclasses

```java
class A {
    protected int x = 5;

    protected void m() {
        System.out.println("A.m");
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new A();
        System.out.println(a.x);
        a.m();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
5
A.m
```

`protected` بيسمح بالوصول من نفس الـ package (وده حالنا هنا لأن كل الكلاسات في نفس الملف)، وكمان من الـ subclasses حتى لو في package تانية. هنا الوصول شغال عادي.
</details>

## 3. Private Constructor مع Static Factory

```java
class A {
    private A() {
    }

    static A create() {
        return new A();
    }

    int v = 7;
}

public class Main {
    public static void main(String[] args) {
        A a = A.create();
        System.out.println(a.v);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
7
```

الـ private constructor بيمنع `new A()` من بره A، بس `create()` static method جوه A نفسها تقدر تناديه. النمط ده بيستخدم للتحكم في إنشاء الـ objects.
</details>

## 4. الـ Inner Class تقدر توصل private members بتاعة Outer

```java
class Outer {
    private int x = 5;

    class Inner {
        int get() {
            return x;
        }
    }

    int run() {
        return new Inner().get();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(new Outer().run());
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
5
```

في Java 11+ الـ nested classes والـ outer class بيكونوا "nestmates" — الـ Inner class تقدر تقرأ `x` حتى لو private لأنها منطقياً جزء من نفس الـ top-level class.
</details>

## 5. الوصول للـ static عن طريق instance

```java
class A {
    static int s = 3;
}

public class Main {
    public static void main(String[] args) {
        A a = new A();
        a.s = 10;
        System.out.println(A.s + " " + a.s);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
10 10
```

`s` static بس الكود `a.s = 10` بيترجم عادي — الـ compiler بيحولها لـ `A.s`. تحذير بس مش error، والاتنين `A.s` و`a.s` نفس المتغير فبيطبعوا نفس القيمة.
</details>

## 6. الـ Private Fields مبتتورثش

```java
class A {
    private int x = 5;
}

class B extends A {
    void show() {
        System.out.println(x);
    }
}

public class Main {
    public static void main(String[] args) {
        new B().show();
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`x` private في A فمش موجودة في B أصلاً — الوراثة مبتشملش الـ private members. فلما `B.show` بتحاول تقرأ `x` الـ compiler مش بيلاقيها في B ولا يقدر يوصلها في A.
</details>

## 7. ممنوع تضعّف الـ Access في الـ Override

```java
class A {
    public void m() {
        System.out.println("A.m");
    }
}

class B extends A {
    void m() {
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


`A.m` public و`B.m` package-private (بدون modifier) — الـ override لازم يكون بنفس الـ access أو أوسع، مش أضيق. javac بيرفض بـ "attempting to assign weaker access privileges".
</details>
