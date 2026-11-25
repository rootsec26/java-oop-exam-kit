enum Level {
    LOW(1), MEDIUM(5), HIGH(10);

    final int power;

    Level(int power) {
        this.power = power;
    }

    int getPower() {
        return power;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(Level.HIGH.getPower());
        System.out.println(Level.LOW == Level.valueOf("LOW"));
    }
}
