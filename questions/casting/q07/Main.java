import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List raw = new ArrayList();
        raw.add("hello");
        List<Integer> nums = (List<Integer>) raw;
        int n = nums.get(0);
        System.out.println(n);
    }
}
