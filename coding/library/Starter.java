class Book {
    private final String title;
    private final String author;

    Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    String getTitle() {
        // TODO
        return "";
    }

    String getAuthor() {
        // TODO
        return "";
    }
}

class Library {
    // TODO: books list field

    void addBook(Book book) {
        // TODO
    }

    Book findByTitle(String title) {
        // TODO: return matching book or null
        return null;
    }

    boolean removeBook(String title) {
        // TODO: remove first matching book, return true if removed
        return false;
    }

    int count() {
        // TODO
        return 0;
    }
}
