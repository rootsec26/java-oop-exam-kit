interface R {
    void run();
}

public class Main {
    public static void main(String[] args) {
        int x = 5;
        x = 10;
        R r = new R() {
            public void run() {
                System.out.println(x);
            }
        };
        r.run();
    }
}
