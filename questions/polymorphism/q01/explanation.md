# Overloading مش Polymorphism
`B.m(String)` ده overload جديد مش override، فالـ compiler بيختار الـ method من الـ compile-time type. `a` معرّف كـ A فبيلاقي بس `m(Object)`، بينما `new B()` بيشوف النسختين فيختار `m(String)` كأقرب match.
