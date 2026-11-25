import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> l = new ArrayList<>();
        l.add("a");
        l.add("b");
        for (String s : l) {
            if (s.equals("a")) {
                l.add("c");
            }
        }
    }
}
