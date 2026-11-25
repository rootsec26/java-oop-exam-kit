public class Main {
    public static void main(String[] args) {
        try {
            System.out.println("try");
        } catch (Exception e) {
            System.out.println("catch-ex");
        } catch (RuntimeException e) {
            System.out.println("catch-runtime");
        } finally {
            System.out.println("finally");
        }
    }
}
