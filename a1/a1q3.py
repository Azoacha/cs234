##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 01, Problem 3
## ===========================================================================
##

# TODO: design recipe

from a1q1 import AppointmentBook

# retrieves the busiest date(s) in the appointment book
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