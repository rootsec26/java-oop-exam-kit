# array element vs reassign

`x[0]=99` غيرت المحتوى فالـ caller شافه. بس `x = new int[]{7,8}` غيّرت المرجع المحلي `x` بس — arr الأصلي مش اتأثر.
