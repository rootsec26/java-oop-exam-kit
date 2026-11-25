public class Main {
    public static void main(String[] args) {
        int x = 5;
        inc(x);
        System.out.println(x);
        x += inc2(x);
        System.out.println(x);
    }

    static void inc(int n) { n = n + 1; }
    static int inc2(int n) { return n + 10; }
}
