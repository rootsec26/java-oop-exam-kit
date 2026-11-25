public class Main {
    public static void main(String[] args) {
        System.out.println(f(5));
        System.out.println(f(5L));
        System.out.println(f(5.0f));
        System.out.println(f(5.0));
    }

    static int f(int x) { return 1; }
    static long f(long x) { return 2; }
    static double f(double x) { return 3; }
}
