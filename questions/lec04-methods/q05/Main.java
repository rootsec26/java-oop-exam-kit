class Swap {
    static void swap(int a, int b) {
        int t = a;
        a = b;
        b = t;
    }
}

public class Main {
    public static void main(String[] args) {
        int x = 1, y = 2;
        Swap.swap(x, y);
        System.out.println(x + " " + y);
    }
}
