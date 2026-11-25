public class Main {
    static int m() {
        try {
            throw new RuntimeException("boom");
        } catch (Exception e) {
            System.out.println("caught");
            return 1;
        } finally {
            System.out.println("finally");
            return 3;
        }
    }

    public static void main(String[] args) {
        System.out.println(m());
    }
}
