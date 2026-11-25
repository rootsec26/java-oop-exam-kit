# مسألة: Shape Hierarchy

ابني hierarchy للـ shapes باستخدام abstract class و polymorphism.

## المطلوب

- `abstract class Shape` فيها `abstract double area()`.
- `class Circle extends Shape` — constructor بياخد `radius` و `area()` بترجع `Math.PI * r * r`.
- `class Rectangle extends Shape` — constructor بياخد `width` و `height` و `area()` بترجع `width * height`.

## نصيحة

- `Starter.java` فيه الـ skeleton — كمّل الـ TODOs بس.
- `Tests.java` بتشيك المساحات الكلية والـ polymorphic dispatch — شغّلها بنفسك قبل ما تسلّم.
