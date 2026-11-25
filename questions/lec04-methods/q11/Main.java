public class Main {
    public static void main(String[] args) {
        System.out.println(max(1, 2));
    }

    static double max(int a, double b) { return a > b ? a : b; }
    static double max(double a, int b) { return a > b ? a : b; }
}
