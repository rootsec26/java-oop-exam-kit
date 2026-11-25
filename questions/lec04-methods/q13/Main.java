public class Main {
    public static void main(String[] args) {
        System.out.println(sign(3));
    }

    static int sign(int n) {
        if (n > 0) return 1;
        else if (n == 0) return 0;
        else if (n < 0) return -1;
    }
}
