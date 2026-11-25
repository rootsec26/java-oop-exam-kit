public class Main {
    public static void main(String[] args) {
        String s = "a";
        s.concat("b");
        System.out.println(s);
        StringBuilder sb = new StringBuilder("a");
        sb.append("b");
        System.out.println(sb.toString());
    }
}
