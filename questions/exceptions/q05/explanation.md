# الـ Override مينفعش يوسّع الـ throws
`B.m` بيعمل override لـ `A.m` اللي معلنة `throws IOException` — بس B بتعلن `throws Exception` الأوسع. ده مش قانوني: الـ override لازم يعلن نفس الـ exceptions أو أقل/أضيق.
