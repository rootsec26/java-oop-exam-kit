class A {
    private A() {
    }

    static A create() {
        return new A();
    }

    int v = 7;
}

public class Main {
    public static void main(String[] args) {
        A a = A.create();
        System.out.println(a.v);
    }
}
