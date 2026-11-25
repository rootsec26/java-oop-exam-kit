# Integer Cache و Autoboxing
القيم من -128 لـ 127 بتتخزن في cache فالـ `==` بتشتغل معاها (true). 128 بره الـ cache فبتاخد objects مختلفة (false). `c == e` بينجح لأن `e` int بيunbox للـ Integer فالمقارنة بالقيمة.
