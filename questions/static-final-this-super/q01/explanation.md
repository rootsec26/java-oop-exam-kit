# ترتيب الـ Static Initialization
أول `new T()` بيحمل الكلاس: الـ static block يشتغل، وسطر `static T t = new T()` بينشئ object فبيشغل inst-init والـ constructor. بعدين الـ `new T()` التانية في main بتشغل inst-init والـ constructor تاني.
