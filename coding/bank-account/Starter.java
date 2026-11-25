class InsufficientFundsException extends Exception {
    InsufficientFundsException(String message) {
        // TODO: call super(message)
    }
}

class BankAccount {
    private double balance;

    BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }

    void deposit(double amount) {
        // TODO: add amount to balance
    }

    void withdraw(double amount) throws InsufficientFundsException {
        // TODO: subtract amount, or throw InsufficientFundsException
    }

    double getBalance() {
        // TODO: return balance
        return 0;
    }
}
