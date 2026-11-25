class A {
    void m(Object o) {
        System.out.println("Object");
    }
}

class B extends A {
    void m(String s) {
        System.out.println("String");
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new B();
        a.m("x");
        new B().m("x");
    }
}
