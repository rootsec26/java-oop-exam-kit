public class Main {
    public static void main(String[] args) {
        System.out.println(gcd(48, 18));
        System.out.println(isPrime(7));
        System.out.println(isPrime(9));
    }

    static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
