# Fail-Fast Iterators
الـ for-each بيستخدم iterator بيتحقق إن الـ list متغيرتش أثناء الـ iteration. `l.add("c")` جوه اللوب بيغير الـ modCount فـ `next()` بيرمي `ConcurrentModificationException` في اللفة التانية.
