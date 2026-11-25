# مسألة: BankAccount

ابني كلاس حساب بنكي مع custom exception.

## المطلوب

- `class InsufficientFundsException extends Exception` — constructor بياخد `String message` و بينادي `super(message)`.
- `class BankAccount` فيها:
  - `private double balance`
  - `BankAccount(double initialBalance)`
  - `void deposit(double amount)` — بتزود الرصيد (افترض amount موجب)
  - `void withdraw(double amount) throws InsufficientFundsException` — بتنقص الرصيد، ولو `amount > balance` بترمي `InsufficientFundsException("Insufficient funds")`
  - `double getBalance()`

## نصيحة

- `InsufficientFundsException` checked exception — لازم تعلن `throws` في `withdraw` وأي حد بيناديها يعمل `try/catch`.
- `Tests.java` بيجرب السحب العادي والسحب اللي أكبر من الرصيد — شغّله قبل التسليم.
