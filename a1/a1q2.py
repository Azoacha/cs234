##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 01, Problem 2
## ===========================================================================
##

# TODO: design recipe

from a1q1 import AppointmentBook

# build appointment book by reading an appointment record file
def buildApptBook(apptFile):
    f = open(apptFile, 'r')
    appt_book = AppointmentBook()

    for line in f:
        details = line.split()
        action = details[0]
        appt_date = int(details[1])
        appt_time = float(details[2])

        if action == "Make":
            appt_book.makeAppointment(appt_date, appt_time, details[3])

        if action == "Cancel":
            appt_book.cancelAppointment(appt_date, appt_time)

        if action == "Change":
            new_appt_date = int(details[3])
            new_appt_time = float(details[4])
            appt_book.changeAppointment(appt_date, appt_time, new_appt_date,
                                        new_appt_time)

    f.close()
    return appt_book