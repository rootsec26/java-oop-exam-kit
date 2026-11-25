import java.util.HashSet;

class P {
    int x;

    P(int x) {
        this.x = x;
    }

    public boolean equals(Object o) {
        return o instanceof P && ((P) o).x == x;
    }
}

public class Main {
    public static void main(String[] args) {
        HashSet<P> set = new HashSet<>();
        set.add(new P(1));
        set.add(new P(1));
        set.add(new P(2));
        System.out.println(set.size());
    }
}
