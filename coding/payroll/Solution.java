class Employee {
    protected String name;
    protected double baseSalary;

    Employee(String name, double baseSalary) {
        this.name = name;
        this.baseSalary = baseSalary;
    }

    double getSalary() {
        return baseSalary;
    }
}

class Manager extends Employee {
    private double bonus;

    Manager(String name, double baseSalary, double bonus) {
        super(name, baseSalary);
        this.bonus = bonus;
    }

    double getSalary() {
        return baseSalary + bonus;
    }
}

class Payroll {
    static double payroll(Employee[] employees) {
        double total = 0;
        for (Employee e : employees) {
            total += e.getSalary();
        }
        return total;
    }
}
