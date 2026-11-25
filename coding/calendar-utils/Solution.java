class CalendarUtils {
    static final int[] DAYS = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    static final String[] NAMES = {
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    };

    static boolean isLeapYear(int year) {
        return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
    }

    static int getNumOfDaysInMonth(int year, int month) {
        if (month == 2 && isLeapYear(year)) {
            return 29;
        }
        return DAYS[month - 1];
    }

    static int getTotalNumOfDays(int year, int month) {
        int total = 0;
        for (int y = 1800; y < year; y++) {
            total += isLeapYear(y) ? 366 : 365;
        }
        for (int m = 1; m < month; m++) {
            total += getNumOfDaysInMonth(year, m);
        }
        return total;
    }

    static int getStartDay(int year, int month) {
        return (3 + getTotalNumOfDays(year, month)) % 7;
    }

    static String getMonthName(int month) {
        return NAMES[month - 1];
    }
}
