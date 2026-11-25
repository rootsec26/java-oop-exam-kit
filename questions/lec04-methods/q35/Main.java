public class Main {
    public static void main(String[] args) {
        int s = 0;
        for (int i = 0; i < 2; i++) { s += i; }
        for (int i = 0; i < 3; i++) { s += i * 10; }
        System.out.println(s);
    }
}
