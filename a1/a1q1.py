##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 01, Problem 1
## ===========================================================================
##

# TODO: design recipe

# AppointmentBook ADT implementation
# AppointmentBook is dictionary of appointments, where the key is a tuple (
#   date, time), and value is the purpose of the appointment
class AppointmentBook:
    # create an empty appointment book
    def __init__(self):
        self.appts = {}
        self.num_appts = 0

    #determines if an appointment exists for the date and time specified
    def isAppointment(self, apptDate, apptTime):
        appt_to_check = (apptDate, apptTime)
        return appt_to_check in self.appts
    
    #inserts the appointment for the date, time and purpose specified,
    #as long as it does not conflict with an existing appointment
    def makeAppointment(self, apptDate, apptTime, purpose):
        appt_check = not self.isAppointment(apptDate, apptTime)
        if appt_check:
            self.appts[(apptDate, apptTime)] = purpose
            self.num_appts = self.num_appts + 1
        return appt_check
    
    #deletes the appointment for the date and time specified
    def cancelAppointment(self, apptDate, apptTime):
        appt_check = self.isAppointment(apptDate, apptTime)
        if appt_check:
            self.appts.pop((apptDate, apptTime))
            self.num_appts = self.num_appts - 1
        return appt_check
    
    # retrieves the purpose of the appointment if one exists
    def checkAppointment(self, apptDate, apptTime):
        appt_check = self.isAppointment(apptDate, apptTime)
        if appt_check:
            return self.appts[(apptDate, apptTime)]
        return ""
    
    #change the date or time for an appointment
    def changeAppointment(self, oldDate, oldTime, newDate, newTime):
        old_appt_check = not self.isAppointment(oldDate, oldTime)
        new_appt_check = self.isAppointment(newDate, newTime)
        appt_check = not(old_appt_check or new_appt_check)
        message = ""

        if old_appt_check:
            message = "There is no appointment at {} on {}."\
                .format(oldTime, oldDate)
        elif new_appt_check:
            message = "There is already an appointment at {} on {}."\
                .format(newTime, newDate)
        else:
            self.appts[(newDate, newTime)] = self.appts.pop((oldDate, oldTime))
            message = "The appointment has been rescheduled to {} on {}."\
                .format(newTime, newDate)

        print(message)
        return appt_check
    
    # retrieves all the appointment on the given date
    def getAppointmentsByDate(self, date):
        appt_keys = [key for key in self.appts if key[0] == date]
        appt_list = []

        for key in appt_keys:
            appt_time = key[1]
            appt_purpose = self.appts[key]
            appt_list.append((appt_time, appt_purpose))

        return appt_list