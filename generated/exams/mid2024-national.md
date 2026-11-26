# Mid2024 National

## 1. Q8: Which of the following statements about arrays are true?

1. A, B, D. ✔
2. C, D.
3. A, C, D.
4. A, B, C, D.

```java
A. An array is a group of variables containing values that all have the same type.
B. Elements are located by index.
C. The length of an array c is determined by the expression c.length();.
D. The zeroth element of array c is specified by c[0].
```

<details>
<summary>الإجابة</summary>

**الإجابة:** A, B, D.


الـ array مجموعة متغيرات من نفس النوع والعناصر بتتحدد بـ index وأول عنصر هو c[0] — التلاتة دول صح. الغلط في C: الـ array عنده property اسمها length مش method، فـ c.length() بيعمل compile error.
</details>

## 2. Q9: Which method call converts the value in variable stringVariable to an integer?

1. Integer.parseInt(stringVariable) ✔
2. Convert.toInt(stringVariable)
3. Integer.toInt(stringVariable)
4. Convert.parseInt(stringVariable)

<details>
<summary>الإجابة</summary>

**الإجابة:** Integer.parseInt(stringVariable)


Integer.parseInt(stringVariable) هي الطريقة الصح لتحويل String لرقم int. الباقي إما methods مش موجودة أصلاً (toInt) أو class اسمه Convert مش موجود.
</details>

## 3. Q10: What is output by the following Java code segment?

1. This porridge is too hot.
2. This porridge is too cold.
3. This porridge is just right!
4. None of the above. ✔

```java
int temp = 180;
if (temp > 90)
{
     System.out.println("This porridge is too hot.");
     // cool down
     temp = temp - (temp > 150 ? 100 : 20);
}
else
{
          if (temp < 70)
              {
                  System.out.println("This porridge is too cold.");
                  // warm up
                  temp = temp + (temp < 50 ? 30 : 20);
              }
}
if (temp == 80)
   System.out.println("This porridge is just right!");
```

<details>
<summary>الإجابة</summary>

**الإجابة:** None of the above.


البرنامج بيطبع سطرين مش واحد: 'This porridge is too hot.' لأن temp=180 أكبر من 90، وبعدها temp بتقل لـ 80 فبيطبع 'This porridge is just right!' كمان. مفيش option فيها السطرين مع بعض — فالإجابة None of the above. (في الأصل كان فيه en dash بدل الناقص في temp – (...)، صلحتها لـ -.)
</details>

## 4. Q11: What does the expression x %= 10 do?

1. Adds 10 to the value of x, and stores the result in x.
2. Divides x by 10 and stores the remainder in x. ✔
3. Divides x by 10 and stores the integer result in x.
4. None of the above.

<details>
<summary>الإجابة</summary>

**الإجابة:** Divides x by 10 and stores the remainder in x.


x %= 10 معناها x = x % 10 — بيقسم x على 10 ويخزن الباقي (remainder) مش الناتج الصحيح. لو عايز ناتج القسمة truncating بتستخدم x /= 10.
</details>

## 5. Q12: What is output by the following Java code segment?

```java
public class Main {
    public static void main(String[] args) {
        int[] a;
        a = new int[10];

        for (int i = 0; i < a.length; i++)
           a[i] = i + 2;

        int result = 0;
        for (int i = 0; i < a.length; i++)
           result += a[i];

        System.out.printf("Result is:  ", result);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
Result is:
```

printf بيطبع الـ format string زي ما هي — 'Result is:  ' — والـ argument الزيادة (result) بيتجاهل لأن مفيش format specifier زي %d. الكود بيترجم ويشتغل عادي — مش compile error. (المسافات الزيادة في الآخر بتتشال في المقارنة.)
</details>

## 6. Q13: Which of the following initializer lists would correctly set the elements of array n?

1. int n[5] = {1; 2; 3; 4; 5};
2. int[] n = {1, 2, 3, 4, 5}; ✔
3. int n = new int(1, 2, 3, 4, 5);
4. array n[int] = {1, 2, 3, 4, 5};

<details>
<summary>الإجابة</summary>

**الإجابة:** int[] n = {1, 2, 3, 4, 5};


الطريقة الوحيدة الصحيحة هي int[] n = {1, 2, 3, 4, 5}; — باقي الخيارات syntax غلط: int n[5] مش Java، new int(...) مش للـ initializer list، وترتيب array n[int] معكوس.
</details>

## 7. Q14: The preferred way to traverse a two-dimensional array is to use

1. three nested for statements.
2. a for statement.
3. a do while statement.
4. two nested for statements. ✔

<details>
<summary>الإجابة</summary>

**الإجابة:** two nested for statements.


الطريقة المفضلة لعمل traversal لـ 2D array هي two nested for loops — واحد للـ rows وواحد للـ columns جواه.
</details>

## 8. Q15: Which of the following is not a type of repetition statement in Java?

1. while statement.
2. for statement.
3. loop statement. ✔
4. do…while statement.

<details>
<summary>الإجابة</summary>

**الإجابة:** loop statement.


الـ repetition statements في Java هي while و for و do…while بس. 'loop statement' مش نوع statement موجود في اللغة.
</details>

## 9. Q16: What is the result value of c at the end of the following code segment?

```java
public class Main {
    public static void main(String[] args) {
        int c = 8;
        c++;
        ++c;
        c %= 5;
        System.out.println(c);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
0
```

c=8 → c++ تخليه 9 → ++c تخليه 10 → c%=5 معناه c = 10 % 5 = 0 (الباقي).
</details>

## 10. Q17: The body of a while loop is always executed at least once.

1. False ✔
2. True

<details>
<summary>الإجابة</summary>

**الإجابة:** False


الـ while loop بيتشيك على الشرط قبل التنفيذ — لو الشرط false من الأول الجسم مش بيتنفذ ولا مرة. التنفيذ مرة واحدة على الأقل ده وصف الـ do…while loop.
</details>

## 11. Q18: Which expression is equivalent to if (!(grade == sentinelValue))?

1. if (grade == sentinelValue)
2. if (grade != sentinelValue) ✔
3. if (!(grade == sentinelValue))
4. if (grade !== sentinelValue)

<details>
<summary>الإجابة</summary>

**الإجابة:** if (grade != sentinelValue)


!(grade == sentinelValue) معناها نفي المقارنة — أي grade != sentinelValue. لاحظ إن != هو الـ operator بتاع Java (مش !== بتاع JavaScript).
</details>

## 12. Q19: In a class containing methods with the same name, the methods are distinguished by ________.

1. (a) and (b) ✔
2. c) Return type
3. b) Types of arguments
4. a) Number of arguments
5. (b) and (c)

<details>
<summary>الإجابة</summary>

**الإجابة:** (a) and (b)


الـ overloaded methods بتتميز بعدد الـ arguments وأنواعهم مع بعض — مش بالـ return type. جربنا: نفس الاسم بـ parameters مختلفة بيترجم عادي، ونفس الـ parameters بـ return type مختلف بيعمل compile error.
</details>

## 13. Q20: Consider array items, which contains the values 0, 2, 4, 6 and 8. If method changeArray is called with the method call changeArray(items, items[2]), what values are stored in items after the method has finished executing?

1. 0, 2, 12, 6, 8.
2. 0, 2, 4, 6, 12. ✔
3. 0, 2, 4, 6, 5.
4. 0, 2, 5, 6, 12.

```java
public static void changeArray(int[] passedArray, int value)
{
   passedArray[value] = 12;
   value = 5;
}
```

<details>
<summary>الإجابة</summary>

**الإجابة:** 0, 2, 4, 6, 12.


items[2]=4 فـ passedArray[4]=12 → items تبقى {0,2,4,6,12}. تغيير value=5 بيأثر على النسخة المحلية من الـ parameter بس — الـ array نفسه متتغيرش غير في index 4.
</details>

## 14. Q21: The right way to define a function in java is.

1. (methodName)
2. methodName[]
3. methodName
4. methodName() ✔

<details>
<summary>الإجابة</summary>

**الإجابة:** methodName()


التعريف الصح للـ method هو methodName() مع return type و parameters — ملحوظة: الإجابة دي ناقصة شوية عشان التعريف الكامل محتاج return type كمان، بس هي الأقرب من الخيارات.
</details>

## 15. Q22: Which of the following is a double-selection control statement?

1. if…else ✔
2. do…while
3. if
4. for

<details>
<summary>الإجابة</summary>

**الإجابة:** if…else


الـ double-selection control statement هو if…else — بيختار بين branchين. if لوحدها single-selection، و do…while و for repetition statements.
</details>

## 16. Q23: How many times is the body of the loop below executed?

```java
public class Main {
    public static void main(String[] args) {
        int counter = 1;
        int times = 0;
        while (counter > 20)
        {
           counter = counter - 1;
           times++;
        }
        System.out.println(times);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
0
```

counter=1 والشرط counter > 20 false من أول مرة → الجسم مش بيتنفذ ولا مرة. ضفنا counter (times) في الـ Main.java عشان نعدّ التنفيذات فعليًا.
</details>

## 17. Q24: What is output by the following Java code segment?

```java
public class Main {
    public static void main(String[] args) {
        int temp = 200;
        if (temp < 90)   System.out.println(temp - 90);
        if (temp > 70)   System.out.println(temp - 70);
        if (temp == 80)   System.out.println(temp - 80);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
130
```

temp=200: مش أصغر من 90، بس أكبر من 70 فيطبع 200-70=130، ومش بيساوي 80 — الناتج سطر واحد: 130.
</details>

## 18. Q25: Assume array items contains the integer values 0, 2, 4, 6 and 8. Which of the following uses the enhanced for loop to display each value in array items?

1. for (int i : items) System.out.printf("%d%n", i); ✔
2. for (int i = 0 : items.length) System.out.printf("%d%n", items[i]);
3. for (int i : items) System.out.printf("%d%n", items[i]);
4. for (int i = 0; i < items.length; i++) System.out.printf("%d%n", items[i]);

<details>
<summary>الإجابة</summary>

**الإجابة:** for (int i : items) System.out.printf("%d%n", i);


الـ enhanced for الصح هو for (int i : items) — بيجيب كل قيمة على طول فـ printf i بيطبع القيم. الخيار التالت كمان enhanced for بس بيطبع items[i] حيث i قيمة مش index فبيقع بـ ArrayIndexOutOfBoundsException. ملاحظة: الورقة مكتوب فيها prinf غلط في كل الخيارات — الصح printf.
</details>

## 19. Q26: For the array int[][] items = {{2, 4}, {6, 8}, {10, 12}};, what is the value returned by items[1][0]?

```java
public class Main {
    public static void main(String[] args) {
        int[][] items = {{2, 4}, {6, 8}, {10, 12}};
        System.out.println(items[1][0]);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
6
```

items[1] هو الصف التاني {6, 8}، وأول عنصر فيه items[1][0] = 6.
</details>

## 20. Q27: Which of the following for-loop headers results in equivalent numbers of iterations:

1. A and B.
2. C and D. ✔
3. None of the loops have equivalent iterations
4. A and B have equivalent iterations and C and D have equivalent iterations.

```java
A.   for (int q = 1; q <= 100; q++)
B.   for (int q = 100; q >= 0; q--)
C.   for (int q = 99; q > 0; q -= 9)
D.   for (int q = 990; q > 0; q -= 90)
```

<details>
<summary>الإجابة</summary>

**الإجابة:** C and D.


A بيشتغل 100 مرة (1 لـ 100)، B بيشتغل 101 مرة (100 لـ 0)، C بيشتغل 11 مرة (99 لـ 9)، D بيشتغل 11 مرة (990 لـ 90). يبقى C و D متكافئين في عدد التكرارات.
</details>

## 21. Q28: The empty statement is denoted by what symbol?

1. Colon :
2. Parentheses ()
3. Braces {}
4. Semicolon ; ✔

<details>
<summary>الإجابة</summary>

**الإجابة:** Semicolon ;


الـ empty statement في Java هو semicolon لوحده ; — statement فاضي قانوني.
</details>

## 22. Q29: Using a condition for a while statement that is initially true is a logical error.

1. True
2. False ✔

<details>
<summary>الإجابة</summary>

**الإجابة:** False


شرط يفضل true (زي while(true)) مش logical error — ده infinite loop بيعلّق البرنامج بس مش غلطة منطقية في الكود نفسه.
</details>

## 23. Q30: What is the output of the next code

1. end of loop ✔
2. Error
3. 20 16 12 end of loop
4. 12 16 20 end of loop

```java
int num = 20, max = 10;
while (num <= max){      System.out.print( " "+num+" " );    num -= 4;}
System.out.println( " end of loop");
```

<details>
<summary>الإجابة</summary>

**الإجابة:** end of loop


num=20 و max=10 → الشرط num <= max false من الأول → اللوب مش بيشتغل خالص واللي بيتطبع هو ' end of loop' بس. ملاحظة: الناتج الحقيقي فيه leading space ومفيش option مطابق حرفيًا — أقرب إجابة 'end of loop' (أول option).
</details>

## 24. Q31: Which of the following is not a primitive type?

1. float
2. String ✔
3. int
4. char

<details>
<summary>الإجابة</summary>

**الإجابة:** String


الـ primitive types في Java هي byte و short و int و long و float و double و char و boolean. String class عادي مش primitive.
</details>

## 25. Q32: Consider the array: s[0] = 7, s[1] = 0, s[2] = -12, s[3] = 9, s[4] = 10, s[5] = 3, s[6] = 6. The value of s[s[6] - s[5]] is

```java
public class Main {
    public static void main(String[] args) {
        int[] s = {7, 0, -12, 9, 10, 3, 6};
        System.out.println(s[s[6] - s[5]]);
    }
}
```

<details>
<summary>الإجابة</summary>

**الناتج:**

```
9
```

s[6] - s[5] = 6 - 3 = 3، يبقى s[3] = 9.
</details>

## 26. Q33: Which is a correct static method call of Math class method sqrt?

1. Math.sqrt(900); ✔
2. sqrt(900);
3. Math math = new Math();      math.sqrt(900);
4. math.sqrt(900);

<details>
<summary>الإجابة</summary>

**الإجابة:** Math.sqrt(900);


sqrt static method في Math — الاستدعاء الصح هو Math.sqrt(900). new Math() مش ممكن لأن الـ constructor private، و sqrt(900) من غير اسم الـ class مش بتتعرف.
</details>

## 27. Q34: The previous statement is equivalent to the next one.

1. False
2. True ✔

```java
int total = 0;
for (int i = 0; i <= 20; i += 2)
      total += i;

int total = 0;
for (int i = 0; i <= 20; total += i, i += 2);
```

<details>
<summary>الإجابة</summary>

**الإجابة:** True


الاتنين بيجمعوا نفس القيم i = 0, 2, ..., 20 — في اللوب التاني الـ update بيعمل total += i قبل i += 2 فالنتيجة واحدة (110 للاتنين). الإجابة True — اللي معلمها False كان غلط. (الورقة مفيهاش body للوب التاني — ضفنا ; فاضي صراحة.)
</details>

## 28. Q35: Which statement below initializes array items to contain 3 rows and 2 columns?

1. int[][] items = {{2, 4}, {6, 8}, {10, 12}}; ✔
2. int[][] items = {{2, 6, 10}, {4, 8, 12}};
3. int[][] items = {2, 4}, {6, 8}, {10, 12};
4. int[][] items = {2, 6, 10}, {4, 8, 12};

<details>
<summary>الإجابة</summary>

**الإجابة:** int[][] items = {{2, 4}, {6, 8}, {10, 12}};


{{2, 4}, {6, 8}, {10, 12}} دي 3 صفوف × عمودين — items.length=3 و items[0].length=2. التاني 2×3 معكوس، والتالت والرابع syntax غلط.
</details>

## 29. Q36: Which of the following statements is false?

1. 1
2. 3
3. 2
4. 4 ✔

```java
1.     A primitive-type variable can store exactly one value of its declared type at a time.
2.     Primitive-type instance variables are initialized by default.
3.     Variables of types byte, char, short, int, long, float and double are initialized to 0.
4.     Variables of type boolean are initialized to true.
```

<details>
<summary>الإجابة</summary>

**الإجابة:** 4


boolean default value هو false مش true — فالجملة 4 هي الغلط. الباقي صح: الـ primitives بتتاخد default values (char بيتعمله init بـ null character قيمتها 0).
</details>

## 30. Q37: Which operator can be used in string concatenation?

1. *
2. ++
3. =+
4. += ✔

<details>
<summary>الإجابة</summary>

**الإجابة:** +=


s += "b" بيضيف النص للنص (string concatenation). =+ و * و ++ مش operators صالحة مع String — جربنا كل واحد فيهم.
</details>

## 31. Q38: What do the following statements do?

1. Create a double array containing 15 elements.
2. Create a double array containing 13 elements.
3. Create a double array containing 14 elements. ✔
4. Declare but do not create a double array.

```java
double[] array;
 array = new double[14];
```

<details>
<summary>الإجابة</summary>

**الإجابة:** Create a double array containing 14 elements.


double[] array; لوحدها declaration بس، لكن array = new double[14] بينشئ array حقيقي بطول 14 — فالكود بيعمل الاتنين: بيعلن وبينشئ array فيه 14 عنصر.
</details>

## 32. Q39: Overloaded methods always have the same _________.

1. number of parameters
2. order of the parameters
3. method name ✔
4. return type

<details>
<summary>الإجابة</summary>

**الإجابة:** method name


الـ overloaded methods لازم يكون ليها نفس الاسم وتختلف في الـ parameters — الاسم هو اللي بيتشارك بينهم. الـ return type مش بيميزهم (ونفس الـ signature بـ return مختلف مش بيترجم أصلاً).
</details>

## 33. Q40: The command java Welcome.java executes the Java class file Welcome.class

1. True
2. False ✔

<details>
<summary>الإجابة</summary>

**الإجابة:** False


في Java 11+ الأمر java Welcome.java بيستخدم الـ source launcher: بيترجم الملف في الذاكرة ويشغّله على طول — مش بيحتاج Welcome.class ومبيستخدموش (جربته: اشتغل من غير class file، ولما حطيت Welcome.class قديم بيطبع نسخة السورس مش الكلاس). كمان مش بيخلق .class file. فحرفيًا الجملة False — هي بتنفذ السورس مش ملف الكلاس.
</details>

## 34. Q41: For the code segment below, which of the following values for q will result in kiwi being included in the output?

1. 3.
2. 1.
3. Any integer less than 1 and greater than or equal to 4. ✔
4. 2.

```java
switch(q)
{
case 1:
System.out.println("apple");
break;
case 2:
System.out.println("orange");
break;
case 3:
System.out.println("banana");
break;
case 4:
System.out.println("pear");
case 5:
System.out.println("grapes");
default:
System.out.println("kiwi");
}
```

<details>
<summary>الإجابة</summary>

**الإجابة:** Any integer less than 1 and greater than or equal to 4.


case 4 مفيهاش break فبتكمل لـ case 5 وبعدين default → kiwi. كمان q=5 بيوصل default مباشرة. أي q مش 1 أو 2 أو 3 (يعني أصغر من 1 أو أكبر من أو يساوي 4) بيطبع kiwi — جربنا القيم -3, 0, 1, 2, 3, 4, 5, 6 فعليًا.
</details>

## 35. Q42: Declaring main as static allows the JVM to invoke main without creating an instance of the class.

1. True ✔
2. False

<details>
<summary>الإجابة</summary>

**الإجابة:** True


static معناها إن الـ method بتاعت الكلاس مش instance — الـ JVM يقدر ينادي main مباشرة من غير ما يعمل object من الـ class. صح.
</details>

## 36. Q43: An enumeration constant can be used in a switch statement in the expression after keyword case.

1. True ✔
2. False

<details>
<summary>الإجابة</summary>

**الإجابة:** True


في Java الـ enum constants بتتكتب في case labels من غير qualifier (case GREEN مش case Color.GREEN) — switch على enum قانوني وبيترجم عادي.
</details>

## 37. Q44: Which of the following methods are overloaded with respect to one another?

1. 1, 2 and 3 are overloaded.
2. 1 and 3 are overloaded; 2 and 4 are overloaded.
3. All four methods are overloaded. ✔
4. 1 and 2 are overloaded; 3 and 4 are overloaded

```java
1. public int max (int a, int b) { … }
2. public double max (double a, double b) { … }
3. public int max (int a, int b, int c) { … }
4. public double max (double a, double b, double c) { … }
```

<details>
<summary>الإجابة</summary>

**الإجابة:** All four methods are overloaded.


الأربع methods نفس الاسم max وكل واحدة بـ signature مختلف (عدد وأنواع الـ parameters مختلفة) → كلهم overloaded مع بعض. الـ return type لوحده مش بيعمل overloading — ونفس الـ signature بـ return type مختلف مش بيترجم أصلاً.
</details>
