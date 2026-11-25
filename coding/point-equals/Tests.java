import java.util.HashSet;
import java.util.Set;

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
        Point p1 = new Point(3, 4);
        Point p2 = new Point(3, 4);
        Point p3 = new Point(3, 5);

        check(p1.equals(p1), "equals reflexive");
        check(p1.equals(p2), "equals same coords");
        check(!p1.equals(p3), "equals different y");
        check(!p1.equals(null), "equals null");
        check(!p1.equals("not a point"), "equals wrong type");
        check(p2.equals(p1), "equals symmetric");

        check(p1.hashCode() == p2.hashCode(), "hashCode consistent with equals");
        check(p1.toString().equals("Point(3, 4)"), "toString format");

        Set<Point> set = new HashSet<>();
        set.add(p1);
        set.add(p2);
        set.add(p3);
        check(set.size() == 2, "HashSet dedups equal points");
        check(set.contains(new Point(3, 4)), "HashSet contains equal point");

        if (failures > 0) {
            System.out.println(failures + " test(s) failed");
            System.exit(1);
        }
        System.out.println("ALL TESTS PASSED");
    }
}
