class A {
    static int s = 3;
}

public class Main {
    public static void main(String[] args) {
        A a = new A();
        a.s = 10;
        System.out.println(A.s + " " + a.s);
    }
}
