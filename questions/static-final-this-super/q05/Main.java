class A {
    static {
        System.out.println("A-static");
    }

    {
        System.out.println("A-init");
    }

    A() {
        System.out.println("A-ctor");
    }
}

class B extends A {
    static {
        System.out.println("B-static");
    }

    {
        System.out.println("B-init");
    }

    B() {
        System.out.println("B-ctor");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("main");
        new B();
    }
}
