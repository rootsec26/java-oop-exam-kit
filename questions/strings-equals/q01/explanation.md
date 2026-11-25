# String Pool vs new String
الـ literals "hi" بيشاوروا على نفس الـ object في الـ String pool فـ `==` بتدي true. `new String` بيعمل object جديد فالـ `==` بتدي false رغم إن `equals` بتقول إن المحتوى واحد.
