class A {
    private void m() {
        System.out.println("A.m");
    }

    void call() {
        m();
    }
}

class B extends A {
    void m() {
        System.out.println("B.m");
    }

    void callB() {
        m();
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new B();
        a.call();
        new B().callB();
    }
}
