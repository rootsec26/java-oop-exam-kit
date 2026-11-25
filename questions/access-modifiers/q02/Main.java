class A {
    protected int x = 5;

    protected void m() {
        System.out.println("A.m");
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new A();
        System.out.println(a.x);
        a.m();
    }
}
