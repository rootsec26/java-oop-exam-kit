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
        Library lib = new Library();
        check(lib.count() == 0, "empty library count");

        Book b1 = new Book("Clean Code", "Robert Martin");
        Book b2 = new Book("Effective Java", "Joshua Bloch");
        lib.addBook(b1);
        lib.addBook(b2);
        lib.addBook(new Book("Clean Code", "Someone Else"));

        check(lib.count() == 3, "count after adding 3 books");
        check(lib.findByTitle("Effective Java") == b2, "findByTitle returns the book");
        check(lib.findByTitle("Missing") == null, "findByTitle missing returns null");
        check("Clean Code".equals(lib.findByTitle("Clean Code").getTitle()),
                "findByTitle finds first match");

        check(lib.removeBook("Clean Code"), "removeBook existing returns true");
        check(lib.count() == 2, "count after remove");
        check("Someone Else".equals(lib.findByTitle("Clean Code").getAuthor()),
                "removeBook removed only the first match");
        check(!lib.removeBook("Nope"), "removeBook missing returns false");
        check(lib.count() == 2, "count unchanged after failed remove");

        if (failures > 0) {
            System.out.println(failures + " test(s) failed");
            System.exit(1);
        }
        System.out.println("ALL TESTS PASSED");
    }
}
