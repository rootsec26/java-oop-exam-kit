class A {
    int v = 1;
}

class B extends A {
    int v = 2;

    void show() {
        System.out.println(v + " " + this.v + " " + super.v);
    }
}

public class Main {
    public static void main(String[] args) {
        new B().show();
    }
}
