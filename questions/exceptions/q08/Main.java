class MyException extends Exception {
    MyException(String msg) {
        super(msg);
    }
}

public class Main {
    static void risky() throws MyException {
        System.out.println("before");
        throw new MyException("custom");
    }

    public static void main(String[] args) {
        try {
            risky();
        } catch (MyException e) {
            System.out.println("caught: " + e.getMessage());
        } finally {
            System.out.println("done");
        }
    }
}
