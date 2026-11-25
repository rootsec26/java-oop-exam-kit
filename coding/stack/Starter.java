import java.util.EmptyStackException;

interface IntStack {
    void push(int value);

    int pop() throws EmptyStackException;

    boolean isEmpty();

    int size();
}

class ArrayStack implements IntStack {
    private final int[] data = new int[10];
    private int top = 0;

    public void push(int value) {
        // TODO: store value and move top
    }

    public int pop() {
        // TODO: return last pushed value, throw EmptyStackException if empty
        return 0;
    }

    public boolean isEmpty() {
        // TODO
        return true;
    }

    public int size() {
        // TODO
        return 0;
    }
}
