class A {
    void hi() {
        System.out.println("A.hi");
    }
}

class B extends A {
    void hi() {
        System.out.println("B.hi");
    }

    void test() {
        super.hi();
        hi();
    }
}

public class Main {
    public static void main(String[] args) {
        new B().test();
    }
}
