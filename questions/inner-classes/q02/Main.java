class Outer {
    int v = 5;

    static class Nested {
        void show() {
            System.out.println(v);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        new Outer.Nested().show();
    }
}
