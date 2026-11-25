# Interface Fields بتكون final تلقائيًا
أي field جوه interface هو `public static final` ضمنيًا. `X = 10` محاولة تغيير final variable فـ javac بيفشل — ومينفعش تعمل implements من غير ما تتعامل معاها كـ constant.
