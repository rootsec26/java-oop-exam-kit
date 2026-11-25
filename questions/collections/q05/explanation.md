# remove(int) مش remove(Object)
`l.remove(1)` بينادي `remove(int index)` بيمسح العنصر في الـ index 1 ("b") → `[a, c]`. `l.remove("a")` بينادي `remove(Object)` بيمسح بالقيمة → `[c]`. الـ overload بيختار حسب نوع الـ argument.
