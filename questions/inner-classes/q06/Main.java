class Outer {
    static void make() {
        class Local {
            void m() {
                System.out.println("local");
            }
        }
        new Local().m();
    }
}

public class Main {
    public static void main(String[] args) {
        Outer.make();
    }
}
