# مسألة: Point equals و hashCode

ابني كلاس `Point` يشتغل صح مع `equals` و `hashCode` و `HashSet`.

## المطلوب

- `class Point` فيها `private final int x` و `private final int y` و constructor `Point(int x, int y)`.
- `equals(Object o)` — بترجع true لو `o` Point ونفس `x` و `y`. استخدم `instanceof` و cast.
- `hashCode()` — لازم تكون متسقة مع equals (نقطتين متساويتين → نفس الـ hashCode). استخدم `Objects.hash(x, y)` أو دمج يدوي.
- `toString()` — أي format مقروء، مثلاً `"Point(3, 4)"`.

## نصيحة

- `equals` لازم يكون `public` وبتاخد `Object` مش `Point` — وإلا مش هتشتغل مع الـ collections.
- `Tests.java` بيجرب `HashSet` — لو `hashCode` مش متسقة هتلاقي duplicates.
