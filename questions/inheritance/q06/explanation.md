# ترتيب الـ Instance Initializer Blocks
الترتيب: `super()` → instance init block بتاع الأب → constructor بتاع الأب → instance init block بتاع الابن → constructor بتاع الابن. الـ init block بيشتغل بعد الـ super() وقبل باقي جسم الـ constructor.
