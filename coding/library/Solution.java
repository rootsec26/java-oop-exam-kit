import java.util.ArrayList;
import java.util.List;

class Book {
    private final String title;
    private final String author;

    Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    String getTitle() {
        return title;
    }

    String getAuthor() {
        return author;
    }
}

class Library {
    private final List<Book> books = new ArrayList<>();

    void addBook(Book book) {
        books.add(book);
    }

    Book findByTitle(String title) {
        for (Book b : books) {
            if (b.getTitle().equals(title)) {
                return b;
            }
        }
        return null;
    }

    boolean removeBook(String title) {
        for (int i = 0; i < books.size(); i++) {
            if (books.get(i).getTitle().equals(title)) {
                books.remove(i);
                return true;
            }
        }
        return false;
    }

    int count() {
        return books.size();
    }
}
