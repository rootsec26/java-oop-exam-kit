class A {
    A() {
        System.out.println("A-ctor");
    }
}

class B extends A {
    B() {
        System.out.println("B-ctor");
    }
}

class C extends B {
    C() {
        System.out.println("C-ctor");
    }
}

public class Main {
    public static void main(String[] args) {
        new C();
    }
}
