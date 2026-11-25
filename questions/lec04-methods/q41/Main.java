public class Main {
    public static void main(String[] args) {
        rec(3);
    }

    static void rec(int n) {
        if (n > 0) {
            System.out.println(n);
            rec(n - 1);
        }
    }
}
