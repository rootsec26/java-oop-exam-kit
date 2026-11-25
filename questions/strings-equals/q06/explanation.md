# equals لازم تكون Symmetric
`a.equals(b)` بتشيك `b instanceof A` → true (لأن B extends A). `b.equals(a)` بتشيك `a instanceof B` → false. ده كسر لقاعدة الـ symmetry في equals contract — علامة إن `instanceof` لوحده مش كفاية مع الوراثة.
