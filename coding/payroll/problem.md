# مسألة: Employee / Manager Payroll

ابني نظام مرتبات بـ polymorphism — كل نوع employee ليه طريقة حساب مختلفة للـ salary.

## المطلوب

- `class Employee` فيها `protected String name` و `protected double baseSalary` و constructor بياخدهم، و `double getSalary()` بترجع `baseSalary`.
- `class Manager extends Employee` فيها `private double bonus` زيادة على الـ base، و `getSalary()` بترجع `baseSalary + bonus`.
- `static double payroll(Employee[] employees)` — بترجع مجموع `getSalary()` لكل الموظفين.

## نصيحة

- حط `payroll` جوه class `Payroll` لو حابب، أو اعملها static في أي حتة — المهم الـ Tests تلاقيها.
- الـ polymorphism هنا إن `payroll` بتتعامل مع الكل كـ `Employee` بس كل واحد بيرجع مرتبه الصح.
