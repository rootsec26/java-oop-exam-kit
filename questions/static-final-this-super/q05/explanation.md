# ترتيب تحميل الكلاسات والـ Initialization
أول `println("main")` بيشتغل عادي. لما `new B()` يحتاج تحميل B، الـ JVM بيحمل ويعمل initialize للـ superclass A الأول: static blocks بتاعة A وبعدين B. بعد كده الـ instance init والـ constructors بالترتيب A ثم B.
