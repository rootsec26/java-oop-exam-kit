class A {
    static void m() {
    }
}

class B extends A {
    void m() {
    }
}

public class Main {
    public static void main(String[] args) {
        new B();
    }
}
