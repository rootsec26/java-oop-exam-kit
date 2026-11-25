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

    static void checkClose(double actual, double expected, String name) {
        check(Math.abs(actual - expected) < 1e-9, name + " (got " + actual + ")");
    }

    public static void main(String[] args) {
        Shape[] shapes = {new Circle(1), new Rectangle(2, 3), new Circle(2)};

        checkClose(shapes[0].area(), Math.PI, "circle r=1 area");
        checkClose(shapes[1].area(), 6.0, "rectangle 2x3 area");
        checkClose(shapes[2].area(), 4 * Math.PI, "circle r=2 area");

        double total = 0;
        for (Shape s : shapes) {
            total += s.area();
        }
        checkClose(total, 5 * Math.PI + 6, "polymorphic total");

        if (failures > 0) {
            System.out.println(failures + " test(s) failed");
            System.exit(1);
        }
        System.out.println("ALL TESTS PASSED");
    }
}
