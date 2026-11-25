class A {
    A() {
        show();
    }

    void show() {
        System.out.println("A.show");
    }
}

class B extends A {
    B() {
        super();
    }

    void show() {
        System.out.println("B.show");
    }
}

public class Main {
    public static void main(String[] args) {
        new B();
    }
}
