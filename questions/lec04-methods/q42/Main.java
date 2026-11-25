public class Main {
    public static void main(String[] args) {
        rec(1);
    }

    static void rec(int n) {
        rec(n + 1);
    }
}
