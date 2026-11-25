class T {
    static {
        System.out.println("static-block");
    }

    {
        System.out.println("inst-init");
    }

    T() {
        System.out.println("ctor");
    }

    static T t = new T();
}

public class Main {
    public static void main(String[] args) {
        new T();
    }
}
