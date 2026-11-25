class A {
    void m() throws java.io.IOException {
        System.out.println("A.m");
    }
}

class B extends A {
    void m() throws Exception {
        System.out.println("B.m");
    }
}

public class Main {
    public static void main(String[] args) {
        new B();
    }
}
