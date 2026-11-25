class A {
}

class B extends A {
    void m() {
        System.out.println("B.m");
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new B();
        B b = (B) a;
        b.m();
    }
}
