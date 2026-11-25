class A {
    {
        System.out.println("A-init");
    }

    A() {
        System.out.println("A-ctor");
    }
}

class B extends A {
    {
        System.out.println("B-init");
    }

    B() {
        System.out.println("B-ctor");
    }
}

public class Main {
    public static void main(String[] args) {
        new B();
    }
}
