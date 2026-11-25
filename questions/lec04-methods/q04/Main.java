public class Main {
    public static void main(String[] args) {
        nPrintln("Welcome", 3);
    }

    static void nPrintln(String message, int n) {
        for (int i = 0; i < n; i++) {
            System.out.println(message);
        }
    }
}
