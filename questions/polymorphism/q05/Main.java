class Shape {
    void area() {
        System.out.println("Shape");
    }
}

class Circle extends Shape {
    void area() {
        System.out.println("Circle");
    }
}

class Square extends Shape {
    void area() {
        System.out.println("Square");
    }
}

public class Main {
    public static void main(String[] args) {
        Shape[] shapes = {new Circle(), new Square(), new Shape()};
        for (Shape s : shapes) {
            s.area();
        }
    }
}
