# مسألة: NumberUtils

اعمل كلاس `NumberUtils` فيه تلات methods static للأعداد الصحيحة الموجبة.

## المطلوب

- `static int gcd(int a, int b)` — القاسم المشترك الأكبر بتاع `a` و `b` بخوارزمية Euclid. لازم يشتغل مع `a=0` أو `b=0` (gcd(0, 5) = 5).
- `static boolean isPrime(int n)` — بترجع true لو `n` أولي. الأعداد الأصغر من 2 مش أولية. optimizations اختيارية (i*i <= n).
- `static String toHex(int n)` — بيحوّل عدد **موجب** للـ hexadecimal lowercase (0-9 و a-f). `toHex(255)` = `"ff"`، `toHex(0)` = `"0"`، `toHex(16)` = `"10"`. **ممنوع** تستخدم `Integer.toHexString` — المطلوب تفكيرك في الخوارزمية (قسمة متكررة على 16).

## نصايح

- `gcd` سهل بـ while loop و `%` — راقب حالة `b == 0`.
- `isPrime`: جرّب القواسم من 2 لـ `i*i <= n` — أسرع بكتير من اللوب للحد `n`.
- `toHex`: اقسم على 16 والباقي هو الـ digit — بالترتيب العكسي (remainder الأخير هو أول حرف). فكر في StringBuilder أو recursion. انتبه لـ `n=0` — المفروض ترجع `"0"`.
