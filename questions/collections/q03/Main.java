import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

class P {
    int x;

    P(int x) {
        this.x = x;
    }

    public boolean equals(Object o) {
        return o instanceof P && ((P) o).x == x;
    }

    public int hashCode() {
        return Objects.hash(x);
    }
}

public class Main {
    public static void main(String[] args) {
        List<P> l = new ArrayList<>();
        l.add(new P(1));
        System.out.println(l.contains(new P(1)));
        System.out.println(l.remove(new P(1)));
        System.out.println(l.size());
    }
}
