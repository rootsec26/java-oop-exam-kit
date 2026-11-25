public class Main {
    public static void main(String[] args) {
        Object o = "hello";
        if (o instanceof String) {
            String s = (String) o;
            System.out.println(s.length());
        } else {
            System.out.println("not string");
        }
        Object n = 42;
        System.out.println(n instanceof String);
    }
}
