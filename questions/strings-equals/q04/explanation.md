# equals من غير hashCode مش كفاية
الـ HashSet بيستخدم `hashCode()` الأول عشان يحدد الـ bucket — وبما إن P معملتش `hashCode()` فالـ objects بتاخد hash مختلف حتى لو `equals` بتقول true. النتيجة: التلاتة بيتحفظوا كعناصر منفصلة.
