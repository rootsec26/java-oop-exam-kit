# List.of بيرجع List immutable
`List.of()` بتعمل immutable list — أي محاولة تعديل (`add`, `remove`, `set`) بترمي `UnsupportedOperationException`. لو محتاج تعديل استخدم `new ArrayList<>(List.of(...))`.
