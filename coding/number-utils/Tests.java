public class Tests {
    static int failures = 0;

    static void check(boolean cond, String name) {
        if (cond) {
            System.out.println("PASS " + name);
        } else {
            failures++;
            System.out.println("FAIL " + name);
        }
    }

    public static void main(String[] args) {
        check(NumberUtils.gcd(48, 18) == 6, "gcd(48,18)=6");
        check(NumberUtils.gcd(17, 5) == 1, "gcd(17,5)=1");
        check(NumberUtils.gcd(0, 5) == 5, "gcd(0,5)=5");
        check(NumberUtils.gcd(100, 10) == 10, "gcd(100,10)=10");
        check(NumberUtils.gcd(7, 13) == 1, "gcd coprime");

        check(NumberUtils.isPrime(2), "isPrime(2)");
        check(NumberUtils.isPrime(7), "isPrime(7)");
        check(NumberUtils.isPrime(97), "isPrime(97)");
        check(NumberUtils.isPrime(7919), "isPrime(7919)");
        check(!NumberUtils.isPrime(1), "isPrime(1)=false");
        check(!NumberUtils.isPrime(0), "isPrime(0)=false");
        check(!NumberUtils.isPrime(9), "isPrime(9)=false");
        check(!NumberUtils.isPrime(100), "isPrime(100)=false");
        check(!NumberUtils.isPrime(-7), "isPrime(-7)=false");

        check(NumberUtils.toHex(0).equals("0"), "toHex(0)");
        check(NumberUtils.toHex(255).equals("ff"), "toHex(255)=ff");
        check(NumberUtils.toHex(16).equals("10"), "toHex(16)=10");
        check(NumberUtils.toHex(305419896).equals("12345678"), "toHex(0x12345678)");
        check(NumberUtils.toHex(10).equals("a"), "toHex(10)=a");
        check(NumberUtils.toHex(14).equals("e"), "toHex(14)=e");
        check(NumberUtils.toHex(1).equals("1"), "toHex(1)=1");

        if (failures > 0) {
            System.out.println(failures + " test(s) failed");
            System.exit(1);
        }
        System.out.println("ALL TESTS PASSED");
    }
}
