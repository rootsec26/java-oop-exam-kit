public class Main {
    static void change(String s) {
        s = "changed";
    }

    public static void main(String[] args) {
        String s = "orig";
        change(s);
        System.out.println(s);
    }
}
