public class Main {
    public static void main(String[] args) {
        int a = 5, b = 2;
        System.out.println(max(a, b));
        System.out.println(max(9, 4));
    }

    static int max(int num1, int num2) {
        int result;
        if (num1 > num2) {
            result = num1;
        } else {
            result = num2;
        }
        return result;
    }
}
