# ترتيب قفل الـ Resources
الـ try-with-resources بيقفل الـ resources بترتيب عكسي من إنشائها — `b` اتقفل قبل `a`. الـ close() بينادي حتى لو الـ try خلص عادي أو حصل exception.
