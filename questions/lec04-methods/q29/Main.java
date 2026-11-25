public class Main {
    public static void main(String[] args) {
        boolean ok = true;
        for (int i = 0; i < 1000; i++) {
            int r = 50 + (int)(Math.random() * 50);
            if (r < 50 || r > 99) ok = false;
        }
        System.out.println(ok);
    }
}
