# الـ Static Nested Class مفيهاش Outer instance
`Nested` static يعني مفيهاش reference لـ Outer object، فمش هتقدر توصل `v` instance variable. javac بيفشل بـ "non-static variable v cannot be referenced from a static context".
