public class Main {
    static void m() {
        try {
            int[] a = new int[1];
            a[2] = 5;
        } catch (NullPointerException e) {
            System.out.println("npe");
        }
    }

    public static void main(String[] args) {
        m();
    }
}
