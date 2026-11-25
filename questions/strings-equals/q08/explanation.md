# String Concat مع null
`"x" + null` مش NullPointerException — الـ compiler بيحوّل الـ null لـ "null" كنص. `s == null` بيطبع true عادي لأن المقارنة بالمرجع مش بتلمس القيمة.
