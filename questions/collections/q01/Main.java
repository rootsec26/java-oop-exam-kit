import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> l = new ArrayList<>();
        l.add("b");
        l.add("a");
        l.add("b");
        System.out.println(l);
        System.out.println(l.size());
        System.out.println(l.get(1));
    }
}
