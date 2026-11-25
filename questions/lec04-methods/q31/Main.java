public class Main {
    public static void main(String[] args) {
        System.out.println(f(g(1), g(2)));
    }

    static int g(int x) {
        System.out.println("g" + x);
        return x;
    }

    static int f(int a, int b) {
        return a * 10 + b;
    }
}
