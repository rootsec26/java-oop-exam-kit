public class Main {
    public static void main(String[] args) {

        double amount = 11.56;
        int remaining = (int)(amount * 100);
        int dollars = remaining / 100;
        remaining = remaining % 100;
        int quarters = remaining / 25;
        remaining = remaining % 25;
        int dimes = remaining / 10;
        remaining = remaining % 10;
        int nickels = remaining / 5;
        int pennies = remaining % 5;
        System.out.println(dollars);
        System.out.println(quarters);
        System.out.println(dimes);
        System.out.println(nickels);
        System.out.println(pennies);
    }
}

