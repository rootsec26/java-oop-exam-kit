public class Main {
    public static void main(String[] args) {
        boolean ok = true;
        for (int i = 0; i < 1000; i++) {
            int r = (int)(Math.random() * 10);
            if (r < 0 || r > 9) ok = false;
        }
        System.out.println(ok);
    }
}
