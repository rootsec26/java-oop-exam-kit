public class Main {
    public static void main(String[] args) {
        boolean ok = true;
        for (int i = 0; i < 1000; i++) {
            char c = (char)('a' + Math.random() * ('z' - 'a' + 1));
            if (c < 'a' || c > 'z') ok = false;
        }
        System.out.println(ok);
    }
}
