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
        IntStack stack = new ArrayStack();

        check(stack.isEmpty(), "new stack is empty");
        check(stack.size() == 0, "new stack size 0");

        stack.push(1);
        stack.push(2);
        stack.push(3);

        check(!stack.isEmpty(), "stack not empty after pushes");
        check(stack.size() == 3, "size after 3 pushes");

        check(stack.pop() == 3, "pop returns last pushed (LIFO)");
        check(stack.pop() == 2, "second pop");
        check(stack.pop() == 1, "third pop");
        check(stack.isEmpty(), "empty after popping all");

        boolean threw = false;
        try {
            stack.pop();
        } catch (java.util.EmptyStackException e) {
            threw = true;
        }
        check(threw, "pop on empty throws EmptyStackException");

        if (failures > 0) {
            System.out.println(failures + " test(s) failed");
            System.exit(1);
        }
        System.out.println("ALL TESTS PASSED");
    }
}
