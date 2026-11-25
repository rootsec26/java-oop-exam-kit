class R implements AutoCloseable {
    private final String name;

    R(String name) {
        this.name = name;
    }

    public void close() {
        System.out.println("close-" + name);
    }
}

public class Main {
    public static void main(String[] args) {
        try (R a = new R("a"); R b = new R("b")) {
            System.out.println("body");
        }
    }
}
