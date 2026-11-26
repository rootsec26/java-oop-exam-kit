# Q20: Consider array items, which contains the values 0, 2, 4, 6 and 8. If method changeArray is called with the method call changeArray(items, items[2]), what values are stored in items after the method has finished executing?

items[2]=4 فـ passedArray[4]=12 → items تبقى {0,2,4,6,12}. تغيير value=5 بيأثر على النسخة المحلية من الـ parameter بس — الـ array نفسه متتغيرش غير في index 4.
