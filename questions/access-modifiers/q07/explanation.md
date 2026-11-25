# ممنوع تضعّف الـ Access في الـ Override
`A.m` public و`B.m` package-private (بدون modifier) — الـ override لازم يكون بنفس الـ access أو أوسع، مش أضيق. javac بيرفض بـ "attempting to assign weaker access privileges".
