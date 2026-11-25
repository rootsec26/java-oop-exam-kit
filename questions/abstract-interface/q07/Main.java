interface A {
    default void m() {
        System.out.println("A.m");
    }
}

interface B extends A {
}

class C implements B {
}

public class Main {
    public static void main(String[] args) {
        new C().m();
    }
}
