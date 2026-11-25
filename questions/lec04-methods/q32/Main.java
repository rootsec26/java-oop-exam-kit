public class Main {
    public static void main(String[] args) {
        int i = 1;
        System.out.println(max(i++, i));
        System.out.println(i);
    }

    static int max(int a, int b) { return a > b ? a : b; }
}
