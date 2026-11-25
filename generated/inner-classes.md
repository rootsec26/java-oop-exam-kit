# Inner Classes و Enums

## 1. الـ Inner Class شايلة مرجع للـ Outer

```java
class Outer {
    int v = 5;

    class Inner {
        void show() {
            System.out.println(v);
        }
    }

    Inner make() {
        return new Inner();
    }
}

public class Main {
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.make().show();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
5
```

الـ non-static inner class بتحتفظ بـ reference للـ outer object، فبتقدر توصل `v` مباشرة. إنشائها لازم `outer.new Inner()` أو من جوه Outer زي `make()` هنا.
</details>

## 2. الـ Static Nested Class مفيهاش Outer instance

```java
class Outer {
    int v = 5;

    static class Nested {
        void show() {
            System.out.println(v);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        new Outer.Nested().show();
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`Nested` static يعني مفيهاش reference لـ Outer object، فمش هتقدر توصل `v` instance variable. javac بيفشل بـ "non-static variable v cannot be referenced from a static context".
</details>

## 3. Anonymous Class

```java
interface I {
    void m();
}

public class Main {
    public static void main(String[] args) {
        I i = new I() {
            public void m() {
                System.out.println("anon");
            }
        };
        i.m();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
anon
```

`new I() { ... }` بتعمل class من غير اسم implements الـ interface على طول. `i.m()` بتستدعي النسخة اللي اتكتبت جوه الـ anonymous class.
</details>

## 4. أساسيات الـ Enum

```java
enum Color {
    RED, GREEN, BLUE
}

public class Main {
    public static void main(String[] args) {
        for (Color c : Color.values()) {
            System.out.println(c.ordinal() + ":" + c.name());
        }
        System.out.println(Color.valueOf("GREEN"));
        System.out.println(Color.RED == Color.valueOf("RED"));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
0:RED
1:GREEN
2:BLUE
GREEN
true
```

`values()` بترجع كل الـ constants بالترتيب، `ordinal()` بيرجع الموقع (يبدأ من 0)، و`valueOf` بيدور بالاسم. الـ enum constants objects singleton فـ `==` شغالة معاها.
</details>

## 5. Enum مع Constructor و Fields

```java
enum Level {
    LOW(1), MEDIUM(5), HIGH(10);

    final int power;

    Level(int power) {
        this.power = power;
    }

    int getPower() {
        return power;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(Level.HIGH.getPower());
        System.out.println(Level.LOW == Level.valueOf("LOW"));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
10
true
```

الـ enum يقدر يكون ليه constructor وfields — كل constant بينادي الـ constructor بالقيمة اللي جنبه. `Level.HIGH` عنده power=10 و`getPower()` بترجعها.
</details>

## 6. Local Class جوه Static Method

```java
class Outer {
    static void make() {
        class Local {
            void m() {
                System.out.println("local");
            }
        }
        new Local().m();
    }
}

public class Main {
    public static void main(String[] args) {
        Outer.make();
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
local
```

الـ local class متعرفة جوه method بتشتغل عادي — بتتعمل compile كـ inner class خاصة بالـ method. هنا `make()` static والـ class محلي جواها فمفيش مشكلة.
</details>

## 7. الـ Inner Classes لازم تلتقط effectively final بس

```java
interface R {
    void run();
}

public class Main {
    public static void main(String[] args) {
        int x = 5;
        x = 10;
        R r = new R() {
            public void run() {
                System.out.println(x);
            }
        };
        r.run();
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


الـ anonymous class بتلتقط الـ local variables اللي بتستخدمها — ولازم تكون final أو effectively final. `x` اتغيرت بعد ما اتعملت فـ javac بيرفض.
</details>
