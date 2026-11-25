# مسألة: Stack بـ Interface

ابني Stack بسيط باستخدام interface + implementation.

## المطلوب

- `interface IntStack` فيها:
  - `void push(int value)`
  - `int pop()` — بيرمي `java.util.EmptyStackException` لو الـ stack فاضي
  - `boolean isEmpty()`
  - `int size()`
- `class ArrayStack implements IntStack` — implementation بـ array ثابت الحجم (مثلاً 10 عناصر) و index للـ top.

## نصيحة

- `pop` لازم ترجع آخر عنصر اتعمله push (LIFO) — عكس الـ queue.
- `Tests.java` بيجرب الترتيب وبيشيك إن الـ pop على stack فاضي بيرمي الـ exception.
