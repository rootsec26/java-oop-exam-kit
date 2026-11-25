interface I {
    void m();
}

class T implements I {
    void m() {
        System.out.println("T.m");
    }
}

public class Main {
    public static void main(String[] args) {
        new T().m();
    }
}
