class A {
    A(int x) {
    }
}

class B extends A {
    B() {
        System.out.println("hi");
    }
}

public class Main {
    public static void main(String[] args) {
        new B();
    }
}
