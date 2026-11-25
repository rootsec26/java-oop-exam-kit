# Downcasting الغلط بيرمي ClassCastException
الـ cast `(B) a` بيترجم عادي (downcast قانوني)، بس الـ runtime بيتحقق: الكائن `a` نوعه A مش B فبيرمي `ClassCastException` قبل ما توصل `b.m()`.
