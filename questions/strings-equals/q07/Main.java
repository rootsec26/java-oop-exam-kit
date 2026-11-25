public class Main {
    public static void main(String[] args) {
        String a = "ab";
        String b = "a" + "b";
        String c = new String("ab");
        String d = "a" + new String("b");
        System.out.println(a == b);
        System.out.println(a == c);
        System.out.println(a == d);
        System.out.println(a.equals(d));
    }
}
