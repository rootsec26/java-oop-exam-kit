interface I {
    static void m() {
        System.out.println("I.m");
    }

    default void d() {
        System.out.println("I.d");
    }
}

class T implements I {
}

public class Main {
    public static void main(String[] args) {
        I.m();
        T t = new T();
        t.d();
    }
}
