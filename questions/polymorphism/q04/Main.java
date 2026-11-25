class T {
    void m(int x) {
        System.out.println("int");
    }

    void m(long x) {
        System.out.println("long");
    }

    void m(String s) {
        System.out.println("String");
    }

    void m(Object o) {
        System.out.println("Object");
    }
}

public class Main {
    public static void main(String[] args) {
        T t = new T();
        t.m(5);
        t.m(5L);
        t.m(null);
    }
}
