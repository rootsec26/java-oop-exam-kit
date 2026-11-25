abstract class Shape {
    abstract double area();
}

class Circle extends Shape {
    private final double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    double area() {
        // TODO: return the circle area
        return 0;
    }
}

class Rectangle extends Shape {
    private final double width;
    private final double height;

    Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    double area() {
        // TODO: return the rectangle area
        return 0;
    }
}
