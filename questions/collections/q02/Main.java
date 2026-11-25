import java.util.ArrayList;
import java.util.List;

class P {
    int x;

    P(int x) {
        this.x = x;
    }
}

public class Main {
    public static void main(String[] args) {
        List<P> l = new ArrayList<>();
        P p1 = new P(1);
        l.add(p1);
        l.add(new P(1));
        System.out.println(l.contains(new P(1)));
        System.out.println(l.remove(p1));
        System.out.println(l.size());
    }
}
