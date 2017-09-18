##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 01, Problem 2
## ===========================================================================
##

# TODO: add tests

from a1q1 import AppointmentBook

## buildApptBook(apptFile) builds an appointment book by reading an
##      appointment record file
## Effects: Reads from the file called apptFile
##          Prints the results of a "Change" command on the outputted
##              appointment book
## buildApptBook: Str -> AppointmentBook
## Requires: only one appointment record is on each line of apptFile
##           each line in apptFile must start with one of (Make, Cancel, Change)
##           each line in apptFile must be tab-delimited
## Examples:
##      If "appt.txt" is empty, then buildApptBook("appt.txt") returns an empty
##          appointment book.
##      If the given file "appointment.txt" is used, then
##          buildApptBook("appointment.txt") returns an appointment book with
##              the dictionary of appointments {(45,10.5): "meeting",
##                                              (120,12): "discussion",
##                                              (100,18): "consulting"}
##          and prints the following to stdout:
##              "There is no appointment at 15 at 80"
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
