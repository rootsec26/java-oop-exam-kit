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
        BankAccount acc = new BankAccount(100);
        checkClose(acc.getBalance(), 100, "initial balance");

        acc.deposit(50);
        checkClose(acc.getBalance(), 150, "after deposit");

        try {
            acc.withdraw(30);
            checkClose(acc.getBalance(), 120, "after withdraw");
        } catch (InsufficientFundsException e) {
            check(false, "withdraw 30 should not throw");
        }

        boolean threw = false;
        try {
            acc.withdraw(500);
        } catch (InsufficientFundsException e) {
            threw = true;
            check("Insufficient funds".equals(e.getMessage()), "exception message");
        }
        check(threw, "overdraft throws InsufficientFundsException");
        checkClose(acc.getBalance(), 120, "balance unchanged after failed withdraw");

        if (failures > 0) {
            System.out.println(failures + " test(s) failed");
            System.exit(1);
        }
        System.out.println("ALL TESTS PASSED");
    }
}
