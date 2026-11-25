public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2};
        change(arr);
        System.out.println(arr[0]);
    }

    static void change(int[] x) {
        x[0] = 99;
        x = new int[]{7, 8};
        x[0] = 7;
    }
}
