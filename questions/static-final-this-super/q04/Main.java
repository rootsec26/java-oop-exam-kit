class Counter {
    static int count = 0;
    final int id;

    Counter() {
        count++;
        this.id = count;
    }

    void show() {
        System.out.println(this.id + " static=" + Counter.count);
    }
}

public class Main {
    public static void main(String[] args) {
        new Counter().show();
        new Counter().show();
    }
}
