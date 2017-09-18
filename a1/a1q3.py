##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 01, Problem 3
## ===========================================================================
##

# TODO: add tests

from a1q1 import AppointmentBook

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
    max_appts = 0
    busiest_dates = []

    for date in range(1,366):
        num_appts = len(apptBook.getAppointmentsByDate(date))

        if num_appts == max_appts:
            busiest_dates.append(date)

        if num_appts > max_appts:
            busiest_dates = [date]
            max_appts = num_appts

    return busiest_dates
