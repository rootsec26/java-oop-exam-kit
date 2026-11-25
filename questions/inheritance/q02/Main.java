class A {
    int x = 1;

    A() {
        x = 2;
        System.out.println("A x=" + x);
    }
}

class B extends A {
    int x = 10;

    B() {
        x = 20;
        System.out.println("B x=" + x);
    }
}

public class Main {
    public static void main(String[] args) {
        new B();
    }
}
