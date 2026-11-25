# char = char + متغير

`'a' + x` نوعه int ومش constant expression عشان كده مفيش narrowing تلقائي — لازم `(char)('a' + x)`.
