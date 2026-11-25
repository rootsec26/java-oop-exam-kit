class Employee {
    protected String name;
    protected double baseSalary;

    Employee(String name, double baseSalary) {
        this.name = name;
        this.baseSalary = baseSalary;
    }

    double getSalary() {
        // TODO: return baseSalary
        return 0;
    }
}

class Manager extends Employee {
    private double bonus;

    Manager(String name, double baseSalary, double bonus) {
        super(name, baseSalary);
        this.bonus = bonus;
    }

    double getSalary() {
        // TODO: return baseSalary + bonus
        return 0;
    }
}

class Payroll {
    static double payroll(Employee[] employees) {
        // TODO: sum getSalary() over all employees
        return 0;
    }
}
