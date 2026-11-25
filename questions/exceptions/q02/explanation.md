# الـ Return في Finally بيعمل Override
الـ `return 3` جوه finally بيشتغل آخر حاجة وبيستبدل أي return تاني — حتى اللي في الـ catch. فالنتيجة 3 مش 1، والـ return بتاع الـ catch بيتلغى.
