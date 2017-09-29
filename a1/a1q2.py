##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 01, Problem 2
## ===========================================================================
##

import check
from a1q1 import AppointmentBook

## buildApptBook(apptFile) builds an appointment book by reading an
##      appointment record file
## Effects: Reads from the file called apptFile
##          Prints the results of a "Change" command on the outputted
##              appointment book if there are any in the file
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
##                                              (120,12.0): "discussion"}
##          and prints the following to stdout:
##              "There is no appointment at 15 at 80."
def buildApptBook(apptFile):
    f = open(apptFile, 'r')
    appt_book = AppointmentBook()

    for line in f:
        details = line.split()
        action = details[0]
        appt_date = int(details[1])
        appt_time = float(details[2])

        try:
            if action == "Make":
                appt_book.makeAppointment(appt_date, appt_time, details[3])
            elif action == "Cancel":
                appt_book.cancelAppointment(appt_date, appt_time)
            elif action == "Change":
                new_appt_date = int(details[3])
                new_appt_time = float(details[4])
                appt_book.changeAppointment(appt_date, appt_time,
                                            new_appt_date, new_appt_time)
            else:
                continue

        except:
            continue

    f.close()
    return appt_book

# Test 1: empty text file
book1 = AppointmentBook()
check.expect("Q2T1", buildApptBook("q2_empty.txt"), book1)

# Test 2: text file with just a 'Make' command
book2 = AppointmentBook()
book2.makeAppointment(32, 12.0, "checkup")
check.expect("Q2T2", buildApptBook("q2_make.txt"), book2)

# Test 3: text file with just a 'Cancel' command
check.set_screen("There is no appointment at 9.5 on 10.")
check.expect("Q2T3", buildApptBook("q2_cancel.txt"), book1)

# Test 4: text file with just a 'Change' command
check.expect("Q2T4", buildApptBook("q2_change.txt"), book1)

# Test 5: text file with invalid inputs (values given are out of range)
check.expect("Q2T5", buildApptBook("q2_invalid.txt"), book1)

# Test 6: general case
book6 = AppointmentBook()
book6.makeAppointment(45, 10.5, "meeting")
book6.makeAppointment(120, 12.0, "discussion")
check.set_screen("There is no appointment at 15.0 on 80.")
check.expect("Q2T6", buildApptBook("appointment.txt"), book6)