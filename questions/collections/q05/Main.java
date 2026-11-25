import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> l = new ArrayList<>();
        l.add("a");
        l.add("b");
        l.add("c");
        l.remove(1);
        System.out.println(l);
        l.remove("a");
        System.out.println(l);
    }
}
