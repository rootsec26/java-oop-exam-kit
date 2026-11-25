class A {
    static int v = 1;
}

class B extends A {
    static int v = 2;
}

public class Main {
    public static void main(String[] args) {
        A a = new B();
        B b = new B();
        System.out.println(a.v + " " + b.v + " " + B.v + " " + A.v);
    }
}
