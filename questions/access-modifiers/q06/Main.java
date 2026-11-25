class A {
    private int x = 5;
}

class B extends A {
    void show() {
        System.out.println(x);
    }
}

public class Main {
    public static void main(String[] args) {
        new B().show();
    }
}
