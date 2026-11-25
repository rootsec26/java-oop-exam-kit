class A {
    public void m() {
        System.out.println("A.m");
    }
}

class B extends A {
    void m() {
        System.out.println("B.m");
    }
}

public class Main {
    public static void main(String[] args) {
        new B();
    }
}
