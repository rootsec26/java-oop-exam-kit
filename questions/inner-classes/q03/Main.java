interface I {
    void m();
}

public class Main {
    public static void main(String[] args) {
        I i = new I() {
            public void m() {
                System.out.println("anon");
            }
        };
        i.m();
    }
}
