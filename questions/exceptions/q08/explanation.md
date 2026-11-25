# Custom Checked Exception
`MyException` extends `Exception` فهي checked — لازم `risky()` تعلن `throws MyException` والـ caller يعمل catch. الـ catch بيمسكها بالاسم و`getMessage()` بترجع الرسالة اللي اتبعتت للـ super.
