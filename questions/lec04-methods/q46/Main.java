public class Main {
    public static void main(String[] args) {
        System.out.println(f(1, 2));
        System.out.println(f(1));
    }

    static int f(int a, int b) { return a + b; }
    static int f(int a) { return a * 10; }
}
