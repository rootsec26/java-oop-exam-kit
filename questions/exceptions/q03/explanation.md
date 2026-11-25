# ترتيب الـ Catch مهم —Subclass الأول
`RuntimeException` extends `Exception`، فـ `catch (Exception)` قبلها بيلتقط كل حاجة والـ catch التانية مش هتوصلها أبدًا — javac بيرفض "exception RuntimeException has already been caught".
