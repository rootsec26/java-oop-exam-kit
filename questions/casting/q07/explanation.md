# Type Erasure بيخلي الـ Cast للـ Generics مش آمن
الـ cast `(List<Integer>) raw` بيترجم بس مع unchecked warning — الـ generics مش موجودة في الـ runtime. لما `get(0)` بيرجع String والـ assignment لـ `int n` بيحاول unbox String → `ClassCastException`.
