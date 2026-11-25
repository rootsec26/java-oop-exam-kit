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
        check(CalendarUtils.isLeapYear(2000), "leap 2000");
        check(CalendarUtils.isLeapYear(2004), "leap 2004");
        check(!CalendarUtils.isLeapYear(1900), "not leap 1900");
        check(!CalendarUtils.isLeapYear(1800), "not leap 1800");
        check(!CalendarUtils.isLeapYear(2023), "not leap 2023");

        check(CalendarUtils.getNumOfDaysInMonth(2024, 2) == 29, "Feb leap");
        check(CalendarUtils.getNumOfDaysInMonth(2023, 2) == 28, "Feb normal");
        check(CalendarUtils.getNumOfDaysInMonth(1900, 2) == 28, "Feb 1900");
        check(CalendarUtils.getNumOfDaysInMonth(2023, 1) == 31, "Jan 31");
        check(CalendarUtils.getNumOfDaysInMonth(2023, 4) == 30, "Apr 30");
        check(CalendarUtils.getNumOfDaysInMonth(2023, 12) == 31, "Dec 31");

        check(CalendarUtils.getTotalNumOfDays(1800, 1) == 0, "total 1800/1");
        check(CalendarUtils.getTotalNumOfDays(1800, 2) == 31, "total 1800/2");
        check(CalendarUtils.getTotalNumOfDays(1800, 3) == 59, "total 1800/3");
        check(CalendarUtils.getTotalNumOfDays(1801, 1) == 365, "total 1801/1");
        check(CalendarUtils.getTotalNumOfDays(2000, 1) > 0, "total 2000/1 positive");

        check(CalendarUtils.getStartDay(1800, 1) == 3, "startDay Jan1800=Wed");
        check(CalendarUtils.getStartDay(1800, 2) == 6, "startDay Feb1800=Sat");
        check(CalendarUtils.getStartDay(1801, 1) == 4, "startDay Jan1801=Thu");
        check(CalendarUtils.getStartDay(2024, 1) == 1, "startDay Jan2024=Mon");

        check(CalendarUtils.getMonthName(1).equals("January"), "name 1");
        check(CalendarUtils.getMonthName(2).equals("February"), "name 2");
        check(CalendarUtils.getMonthName(12).equals("December"), "name 12");

        if (failures > 0) {
            System.out.println(failures + " test(s) failed");
            System.exit(1);
        }
        System.out.println("ALL TESTS PASSED");
    }
}
