interface A {
    default void m() {
        System.out.println("A.m");
    }
}

interface B {
    default void m() {
        System.out.println("B.m");
    }
}

class C implements A, B {
}

public class Main {
    public static void main(String[] args) {
        new C().m();
    }
}
