class T {
    T() {
        this(1);
        System.out.println("noarg");
    }

    T(int x) {
        System.out.println("arg" + x);
    }
}

public class Main {
    public static void main(String[] args) {
        new T();
    }
}
