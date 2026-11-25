class A {
    void m() {
    }
}

class B extends A {
    @Override
    void n() {
    }
}

public class Main {
    public static void main(String[] args) {
        new B();
    }
}
