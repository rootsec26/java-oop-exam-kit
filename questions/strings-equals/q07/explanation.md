# Compile-Time Constants بتتعملها Pooling
`"a" + "b"` كلهم literals فـ javac بيحسبهم compile-time constant وبيرجع نفس الـ pooled object (true). `new String("ab")` و`"a" + new String("b")` بيتعملهم runtime objects جديدة فالـ `==` false رغم إن `equals` true.
