public class Main {
    public static void main(String[] args) {
        System.out.println(f('a'));
        System.out.println(f(5));
    }

    static int f(int x) { return 10 + x; }
    static double f(double x) { return 20 + x; }
}
