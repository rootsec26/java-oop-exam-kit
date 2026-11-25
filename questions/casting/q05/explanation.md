# الـ Cast لـ Interface بيترجم بس بيفشل runtime
الكود `(I) a` بيترجم عادي لأن أي class ممكن تكون هتعمل implements للـ interface يومًا — بس A مش هتعمل كده، فالـ runtime بيرمي `ClassCastException` على طول.
