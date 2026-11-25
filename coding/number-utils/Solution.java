class NumberUtils {
    static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    static String toHex(int n) {
        if (n == 0) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            int r = n % 16;
            sb.insert(0, r < 10 ? (char)('0' + r) : (char)('a' + r - 10));
            n /= 16;
        }
        return sb.toString();
    }
}
