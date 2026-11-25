# Static Fields بتتعملها Hiding مش Override
`B.v` بيعمل hide لـ `A.v` — دول متغيرين منفصلين. الوصول للـ static field بيتحدد من الـ compile-time type: `a` معرّف كـ A فياخد `A.v` رغم إن الكائن B.
