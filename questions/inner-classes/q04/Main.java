enum Color {
    RED, GREEN, BLUE
}

public class Main {
    public static void main(String[] args) {
        for (Color c : Color.values()) {
            System.out.println(c.ordinal() + ":" + c.name());
        }
        System.out.println(Color.valueOf("GREEN"));
        System.out.println(Color.RED == Color.valueOf("RED"));
    }
}
