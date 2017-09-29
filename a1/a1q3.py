##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 01, Problem 3
## ===========================================================================
##

from a1q1 import AppointmentBook
import check

## busiestDate(apptBook) retrieves the list, in ascending order, of the busiest
##      date(s) in the appointment book apptBook
## busiestDate: AppointmentBook -> (listof Int)
## Requires: only one appointment record is on each line of apptFile
##           each line in apptFile must start with one of (Make, Cancel, Change)
##           each line in apptFile must be tab-delimited
## Examples:
##      If book1 is an empty appointment book, then
##          busiestDate(book1) => [1, 2, ..., 365]
##      If book2 is built using the appoinment record file "appointment.txt",
##          then busiestDate(book2) => [45, 100, 120]
##      If book3 is built using the appoinment record file "appointment.txt"
##          and another appointment at time 12.5 on date 100 with purpose "IT",
##          then busiestDate(book3) => [100]
def busiestDate(apptBook):
    max_appts = 1
    busiest_dates = []

    for date in range(1,366):
        num_appts = len(apptBook.getAppointmentsByDate(date))

        if num_appts == max_appts:
            busiest_dates.append(date)

        if num_appts > max_appts:
            busiest_dates = [date]
            max_appts = num_appts

    return busiest_dates

# Test 1: Empty AppointmentBook
book = AppointmentBook()
check.expect("Q3T1", busiestDate(book), [])

# Test 2: AppointmentBook with all appointments on the same date
book.makeAppointment(23, 9.0, "Testing")
book.makeAppointment(23, 14.0, "More Testing")
book.makeAppointment(23, 11.5, "Tests")
check.expect("Q3T2", busiestDate(book), [23])

# Test 3: AppointmentBook with 6 appointments, with 3 of them
#   made on same day and the other 3 made on another day
book.makeAppointment(10, 12.5, "Testing")
book.makeAppointment(10, 10.0, "More Testing")
book.makeAppointment(10, 9.0, "Tests")
check.expect("Q3T3", busiestDate(book), [10, 23])

# Test 4: AppointmentBook with 3 appointments, with only 2 made
#   on the same day
book2 = AppointmentBook()
book2.makeAppointment(255, 13.0, "Another one")
book2.makeAppointment(300, 8.5, "We the best")
book2.makeAppointment(255, 10.5, "Liooooon")
check.expect("Q3T4", busiestDate(book2), [255])
