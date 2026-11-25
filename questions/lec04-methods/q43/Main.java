public class Main {
    public static void main(String[] args) {
        System.out.println('a' + 1);
        System.out.println((char)('a' + 1));
        System.out.println(show('b'));
    }

    static int show(char c) { return c + 1; }
}
