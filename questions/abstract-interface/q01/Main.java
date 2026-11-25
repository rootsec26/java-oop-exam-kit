abstract class A {
    A() {
        System.out.println("A-ctor");
    }

    abstract void m();
}

class B extends A {
    B() {
        System.out.println("B-ctor");
    }

    void m() {
        System.out.println("B.m");
    }
}

public class Main {
    public static void main(String[] args) {
        new B().m();
    }
}
