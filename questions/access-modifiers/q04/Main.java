class Outer {
    private int x = 5;

    class Inner {
        int get() {
            return x;
        }
    }

    int run() {
        return new Inner().get();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(new Outer().run());
    }
}
