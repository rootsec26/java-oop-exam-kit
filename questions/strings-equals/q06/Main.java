class A {
    public boolean equals(Object o) {
        return o instanceof A;
    }
}

class B extends A {
    public boolean equals(Object o) {
        return o instanceof B;
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new A();
        B b = new B();
        System.out.println(a.equals(b));
        System.out.println(b.equals(a));
    }
}
