public class Main {
    static void m() {
        throw new Exception("checked");
    }

    public static void main(String[] args) {
        m();
    }
}
