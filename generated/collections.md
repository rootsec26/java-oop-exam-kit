# Collections

## 1. ArrayList بتخزن بالترتيب وبتسمح بالتكرار

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> l = new ArrayList<>();
        l.add("b");
        l.add("a");
        l.add("b");
        System.out.println(l);
        System.out.println(l.size());
        System.out.println(l.get(1));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
[b, a, b]
3
a
```

`ArrayList` بيحافظ على insertion order وبيسمح بعناصر مكررة — عشان كده `[b, a, b]` فيها 3 عناصر. `toString()` بتاعها بيطبع بالـ brackets والفواصل.
</details>

## 2. contains و remove بيعتمدوا على equals

```java
import java.util.ArrayList;
import java.util.List;

class P {
    int x;

    P(int x) {
        this.x = x;
    }
}

public class Main {
    public static void main(String[] args) {
        List<P> l = new ArrayList<>();
        P p1 = new P(1);
        l.add(p1);
        l.add(new P(1));
        System.out.println(l.contains(new P(1)));
        System.out.println(l.remove(p1));
        System.out.println(l.size());
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
false
true
1
```

P معملتش `equals` فبتستخدم `Object.equals` (identity). `contains(new P(1))` بتقارن بالمراجع مش بالقيمة → false. `remove(p1)` بتلاقي نفس الـ object فبتمسحه → true والحجم بينزل لـ 1.
</details>

## 3. equals و hashCode بيخلو contains و remove يشتغلوا بالقيمة

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

class P {
    int x;

    P(int x) {
        this.x = x;
    }

    public boolean equals(Object o) {
        return o instanceof P && ((P) o).x == x;
    }

    public int hashCode() {
        return Objects.hash(x);
    }
}

public class Main {
    public static void main(String[] args) {
        List<P> l = new ArrayList<>();
        l.add(new P(1));
        System.out.println(l.contains(new P(1)));
        System.out.println(l.remove(new P(1)));
        System.out.println(l.size());
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
true
true
0
```

مع `equals` و`hashCode` متعريفين على `x`، الـ `new P(1)` الجديدة بتساوي القديمة — `contains` بتلاقيها (true) و`remove` بتشيلها (true) فالقائمة بتفضل فاضية.
</details>

## 4. Autoboxing + Polymorphism مع Generics

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Number> l = new ArrayList<>();
        l.add(1);
        l.add(2.5);
        l.add(3L);
        l.add(4);
        for (Number n : l) {
            System.out.println(n.getClass().getSimpleName() + ":" + n);
        }
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
Integer:1
Double:2.5
Long:3
Integer:4
```

`List<Number>` بيقبل Integer وDouble وLong لأنهم subclasses بتاعة Number — الـ autoboxing بيحول الـ primitives للـ wrapper classes. `getClass()` بيكشف النوع الحقيقي لكل عنصر.
</details>

## 5. remove(int) مش remove(Object)

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> l = new ArrayList<>();
        l.add("a");
        l.add("b");
        l.add("c");
        l.remove(1);
        System.out.println(l);
        l.remove("a");
        System.out.println(l);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
[a, c]
[c]
```

`l.remove(1)` بينادي `remove(int index)` بيمسح العنصر في الـ index 1 ("b") → `[a, c]`. `l.remove("a")` بينادي `remove(Object)` بيمسح بالقيمة → `[c]`. الـ overload بيختار حسب نوع الـ argument.
</details>

## 6. Fail-Fast Iterators

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> l = new ArrayList<>();
        l.add("a");
        l.add("b");
        for (String s : l) {
            if (s.equals("a")) {
                l.add("c");
            }
        }
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `java.util.ConcurrentModificationException`


الـ for-each بيستخدم iterator بيتحقق إن الـ list متغيرتش أثناء الـ iteration. `l.add("c")` جوه اللوب بيغير الـ modCount فـ `next()` بيرمي `ConcurrentModificationException` في اللفة التانية.
</details>

## 7. List.of بيرجع List immutable

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> l = List.of("a", "b");
        l.add("c");
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
(مفيش output)
```

بيرمي `java.lang.UnsupportedOperationException`


`List.of()` بتعمل immutable list — أي محاولة تعديل (`add`, `remove`, `set`) بترمي `UnsupportedOperationException`. لو محتاج تعديل استخدم `new ArrayList<>(List.of(...))`.
</details>

## 8. الـ Generics مبتاخدش Primitives

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<int> l = new ArrayList<>();
    }
}
```

<details>
<summary>الإجابة</summary>

**COMPILE_ERROR** — الكود ده مش بيترجم.


`List<int>` مش قانوني — الـ type arguments لازم تكون reference types. استخدم `List<Integer>` والـ autoboxing هيشتغل معاك تلقائيًا.
</details>
