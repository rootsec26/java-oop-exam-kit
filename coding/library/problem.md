# مسألة: Library System

ابني نظام مكتبة بسيط بـ `ArrayList` — إضافة كتب، بحث بالعنوان، وحذف.

## المطلوب

- `class Book` فيها `private final String title` و `private final String author` و constructor و `getTitle()` و `getAuthor()`.
- `class Library` فيها `private final List<Book> books = new ArrayList<>()` و methods:
  - `void addBook(Book book)`
  - `Book findByTitle(String title)` — بيرجع أول كتاب عنوانه يساوي الـ title (case-sensitive)، أو `null` لو مش موجود
  - `boolean removeBook(String title)` — بيمسح أول كتاب بنفس العنوان ويرجع true، أو false لو مش موجود
  - `int count()` — عدد الكتب

## نصيحة

- `findByTitle` و `removeBook` — فكر في `equals` على Strings للـ title.
- `removeBook` ممكن تستخدم `removeIf` أو iterator أو loop عادي — أي طريقة صح.
- `Tests.java` بيجرب كل العمليات بما فيها البحث عن كتاب مش موجود.
