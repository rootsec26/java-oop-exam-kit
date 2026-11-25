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
        data[top++] = value;
    }

    public int pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return data[--top];
    }

    public boolean isEmpty() {
        return top == 0;
    }

    public int size() {
        return top;
    }
}
