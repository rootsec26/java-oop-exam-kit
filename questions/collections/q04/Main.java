import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Number> l = new ArrayList<>();
        l.add(1);
        l.add(2.5);
        l.add(3L);
        l.add(4);
        for (Number n : l) {
            System.out.println(n.getClass().getSimpleName() + ":" + n);
        }
    }
}
