# مسألة: CalendarUtils

اعمل كلاس `CalendarUtils` بـ static methods للتقويم — نفس فكرة `PrintCalendar` من المحاضرة. كل الحسابات بتبدأ من **1 يناير 1800** (اللي كان يوم أربعاء = Wednesday).

## المطلوب

- `static boolean isLeapYear(int year)` — سنة كبيسة لو مقسومة على 4، **إلا** لو مقسومة على 100 ومش على 400. يعني 2000 كبيسة، 1900 و 1800 مش كبيسين.
- `static int getNumOfDaysInMonth(int year, int month)` — عدد أيام الشهر (month من 1 لـ 12): يناير 31، فبراير 28 أو 29، أبريل 30... إلخ.
- `static int getTotalNumOfDays(int year, int month)` — عدد الأيام من 1/1/1800 **لحد** (مش شامل) أول يوم في الشهر/السنة دي. يعني `getTotalNumOfDays(1800, 1)` = 0، و `getTotalNumOfDays(1800, 2)` = 31.
- `static int getStartDay(int year, int month)` — يوم الأسبوع بتاع أول يوم في الشهر، **0 = الأحد** لحد **6 = السبت**. `getStartDay(1800, 1)` = 3 (أربعاء). المعادلة: `(3 + getTotalNumOfDays(year, month)) % 7`.
- `static String getMonthName(int month)` — اسم الشهر بالإنجليزي: `"January"` لـ 1 لحد `"December"` لـ 12.

## نصايح

- `isLeapYear`: `year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)`.
- `getNumOfDaysInMonth`: array أو switch بالأطوال {31,28/29,31,30,...}.
- `getTotalNumOfDays`: لوب على السنين من 1800 لـ year-1 تجمع أيام كل سنة (365 أو 366)، وبعدين لوب على الشهور من 1 لـ month-1 في السنة دي.
- `getStartDay`: 1/1/1800 كان أربعاء — لو `totalNumOfDays` هو عدد الأيام بعده، فـ `(3 + total) % 7` بيديك اليوم.
