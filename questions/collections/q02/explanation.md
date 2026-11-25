# contains و remove بيعتمدوا على equals
P معملتش `equals` فبتستخدم `Object.equals` (identity). `contains(new P(1))` بتقارن بالمراجع مش بالقيمة → false. `remove(p1)` بتلاقي نفس الـ object فبتمسحه → true والحجم بينزل لـ 1.
