public class Tests {
    static int failures = 0;

    static void check(boolean cond, String name) {
        if (cond) {
            System.out.println("PASS " + name);
        } else {
            failures++;
            System.out.println("FAIL " + name);
        }
    }

    static void checkClose(double actual, double expected, String name) {
        check(Math.abs(actual - expected) < 1e-9, name + " (got " + actual + ")");
    }

    public static void main(String[] args) {
        Employee emp = new Employee("Sara", 5000);
        Manager mgr = new Manager("Omar", 8000, 2000);

        checkClose(emp.getSalary(), 5000, "employee salary");
        checkClose(mgr.getSalary(), 10000, "manager salary includes bonus");

        Employee[] staff = {emp, mgr, new Employee("Laila", 3000)};
        checkClose(Payroll.payroll(staff), 18000, "payroll total");

        checkClose(Payroll.payroll(new Employee[0]), 0, "empty payroll");

        if (failures > 0) {
            System.out.println(failures + " test(s) failed");
            System.exit(1);
        }
        System.out.println("ALL TESTS PASSED");
    }
}
