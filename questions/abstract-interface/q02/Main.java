interface I {
    int X = 5;
}

class T implements I {
    void change() {
        X = 10;
    }
}

public class Main {
    public static void main(String[] args) {
        new T().change();
    }
}
