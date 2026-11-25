class A {
    static void m() {
        System.out.println("A.m");
    }
}

class B extends A {
    static void m() {
        System.out.println("B.m");
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new B();
        B b = new B();
        a.m();
        b.m();
    }
}
