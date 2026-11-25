class A {
}

interface I {
    void m();
}

public class Main {
    public static void main(String[] args) {
        A a = new A();
        I i = (I) a;
        i.m();
    }
}
