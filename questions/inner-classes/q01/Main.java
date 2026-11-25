class Outer {
    int v = 5;

    class Inner {
        void show() {
            System.out.println(v);
        }
    }

    Inner make() {
        return new Inner();
    }
}

public class Main {
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.make().show();
    }
}
