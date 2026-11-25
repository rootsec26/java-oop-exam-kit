# String و equals و hashCode

## 1. String Pool vs new String

```java
public class Main {
    public static void main(String[] args) {
        String a = "hi";
        String b = "hi";
        String c = new String("hi");
        System.out.println(a == b);
        System.out.println(a == c);
        System.out.println(a.equals(c));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
true
false
true
```

الـ literals "hi" بيشاوروا على نفس الـ object في الـ String pool فـ `==` بتدي true. `new String` بيعمل object جديد فالـ `==` بتدي false رغم إن `equals` بتقول إن المحتوى واحد.
</details>

## 2. Integer Cache و Autoboxing

```java
public class Main {
    public static void main(String[] args) {
        Integer a = 127;
        Integer b = 127;
        Integer c = 128;
        Integer d = 128;
        int e = 128;
        System.out.println(a == b);
        System.out.println(c == d);
        System.out.println(c == e);
        System.out.println(c.equals(d));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
true
false
true
true
```

القيم من -128 لـ 127 بتتخزن في cache فالـ `==` بتشتغل معاها (true). 128 بره الـ cache فبتاخد objects مختلفة (false). `c == e` بينجح لأن `e` int بيunbox للـ Integer فالمقارنة بالقيمة.
</details>

## 3. String immutable و StringBuilder mutable

```java
public class Main {
    public static void main(String[] args) {
        String s = "a";
        s.concat("b");
        System.out.println(s);
        StringBuilder sb = new StringBuilder("a");
        sb.append("b");
        System.out.println(sb.toString());
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
a
ab
```

`concat` بيرجع String جديد ومش بيغير `s` — لازم `s = s.concat("b")`. الـ StringBuilder بيغير نفسه في مكانه فـ `append` بيأثر على طول.
</details>

## 4. equals من غير hashCode مش كفاية

```java
import java.util.HashSet;

class P {
    int x;

    P(int x) {
        this.x = x;
    }

    public boolean equals(Object o) {
        return o instanceof P && ((P) o).x == x;
    }
}

public class Main {
    public static void main(String[] args) {
        HashSet<P> set = new HashSet<>();
        set.add(new P(1));
        set.add(new P(1));
        set.add(new P(2));
        System.out.println(set.size());
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
3
```

الـ HashSet بيستخدم `hashCode()` الأول عشان يحدد الـ bucket — وبما إن P معملتش `hashCode()` فالـ objects بتاخد hash مختلف حتى لو `equals` بتقول true. النتيجة: التلاتة بيتحفظوا كعناصر منفصلة.
</details>

## 5. Java Pass-by-Value

```java
public class Main {
    static void change(String s) {
        s = "changed";
    }

    public static void main(String[] args) {
        String s = "orig";
        change(s);
        System.out.println(s);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
orig
```

الـ parameter `s` جوه `change` هو نسخة من الـ reference — إعادة تعيينه مش بتأثر على الـ variable في `main`. عشان تغير String لازم ترجع قيمة جديدة.
</details>

## 6. equals لازم تكون Symmetric

```java
class A {
    public boolean equals(Object o) {
        return o instanceof A;
    }
}

class B extends A {
    public boolean equals(Object o) {
        return o instanceof B;
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new A();
        B b = new B();
        System.out.println(a.equals(b));
        System.out.println(b.equals(a));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
true
false
```

`a.equals(b)` بتشيك `b instanceof A` → true (لأن B extends A). `b.equals(a)` بتشيك `a instanceof B` → false. ده كسر لقاعدة الـ symmetry في equals contract — علامة إن `instanceof` لوحده مش كفاية مع الوراثة.
</details>

## 7. Compile-Time Constants بتتعملها Pooling

```java
public class Main {
    public static void main(String[] args) {
        String a = "ab";
        String b = "a" + "b";
        String c = new String("ab");
        String d = "a" + new String("b");
        System.out.println(a == b);
        System.out.println(a == c);
        System.out.println(a == d);
        System.out.println(a.equals(d));
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
true
false
false
true
```

`"a" + "b"` كلهم literals فـ javac بيحسبهم compile-time constant وبيرجع نفس الـ pooled object (true). `new String("ab")` و`"a" + new String("b")` بيتعملهم runtime objects جديدة فالـ `==` false رغم إن `equals` true.
</details>

## 8. String Concat مع null

```java
public class Main {
    public static void main(String[] args) {
        String s = null;
        System.out.println("x" + s);
        System.out.println(s + "x");
        System.out.println(s == null);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
xnull
nullx
true
```

`"x" + null` مش NullPointerException — الـ compiler بيحوّل الـ null لـ "null" كنص. `s == null` بيطبع true عادي لأن المقارنة بالمرجع مش بتلمس القيمة.
</details>
