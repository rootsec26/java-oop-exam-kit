# static و final و this و super

## 1. ترتيب الـ Static Initialization

```java
class T {
    static {
        System.out.println("static-block");
    }

    {
        System.out.println("inst-init");
    }

    T() {
        System.out.println("ctor");
    }

    static T t = new T();
}

public class Main {
    public static void main(String[] args) {
        new T();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
static-block
inst-init
ctor
inst-init
ctor
```

أول `new T()` بيحمل الكلاس: الـ static block يشتغل، وسطر `static T t = new T()` بينشئ object فبيشغل inst-init والـ constructor. بعدين الـ `new T()` التانية في main بتشغل inst-init والـ constructor تاني.
</details>

## 2. Constructor Chaining بـ this()

```java
class T {
    T() {
        this(1);
        System.out.println("noarg");
    }

    T(int x) {
        System.out.println("arg" + x);
    }
}

public class Main {
    public static void main(String[] args) {
        new T();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
arg1
noarg
```

`this(1)` لازم يكون أول سطر في الـ constructor وبيبعت التنفيذ لـ `T(int)` الأول. لما `T(int)` يخلص، execution بيرجع يكمل باقي جسم `T()`.
</details>

## 3. الـ Final Method مينفعش تتعملها Override

```java
class A {
    final void m() {
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


`final` على method معناها ممنوع أي subclass يعمل override ليها. `B.m` نفس الـ signature فده override غير قانوني وjavac بيفشل.
</details>

## 4. static مشترك بين كل الـ Instances

```java
class Counter {
    static int count = 0;
    final int id;

    Counter() {
        count++;
        this.id = count;
    }

    void show() {
        System.out.println(this.id + " static=" + Counter.count);
    }
}

public class Main {
    public static void main(String[] args) {
        new Counter().show();
        new Counter().show();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
1 static=1
2 static=2
```

`count` static يعني نسخة واحدة للكل الـ objects، فبتزيد مع كل constructor call. `id` final instance variable بتتاخد قيمتها مرة واحدة في الـ constructor ومش بتتغير بعدها.
</details>

## 5. ترتيب تحميل الكلاسات والـ Initialization

```java
class A {
    static {
        System.out.println("A-static");
    }

    {
        System.out.println("A-init");
    }

    A() {
        System.out.println("A-ctor");
    }
}

class B extends A {
    static {
        System.out.println("B-static");
    }

    {
        System.out.println("B-init");
    }

    B() {
        System.out.println("B-ctor");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("main");
        new B();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
main
A-static
B-static
A-init
A-ctor
B-init
B-ctor
```

أول `println("main")` بيشتغل عادي. لما `new B()` يحتاج تحميل B، الـ JVM بيحمل ويعمل initialize للـ superclass A الأول: static blocks بتاعة A وبعدين B. بعد كده الـ instance init والـ constructors بالترتيب A ثم B.
</details>

## 6. this.v مقابل super.v

```java
class A {
    int v = 1;
}

class B extends A {
    int v = 2;

    void show() {
        System.out.println(v + " " + this.v + " " + super.v);
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

**الناتج:**

```
2 2 1
```

`v` و`this.v` بيشاوروا على `B.v` (اللي عمل hide لـ `A.v`)، بينما `super.v` بيوصل صراحة لنسخة الأب. الثلاثة outputs: 2، 2، 1.
</details>

## 7. الـ Final Class مينفعش تتورث

```java
final class A {
}

class B extends A {
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


`final` على class معناها ممنوع أي class تعمل `extends` ليها. `B extends A` هنا غير قانوني وjavac بيفشل.
</details>
