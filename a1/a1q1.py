##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 01, Problem 1
## ===========================================================================
##

# TODO: account for values outside range
# TODO: design recipe
# TODO: add tests

# AppointmentBook ADT implementation
# AppointmentBook is dictionary of appointments, where the key is a tuple (
#   date, time), and value is the purpose of the appointment
class AppointmentBook:
    """
    Fields: appts ((dictof (tuple Int Float) Str)),
    Requires: 1 <= date <=365, where date is the first element of the keys of
                    appts
              8.0 <= time <= 16.5, where time is the second element of the keys
                    of appts
    """

    # AppointmentBook() produces an empty AppointmentBook object with an empty
    #   dictionary of appointments appts, with the keys being a tuple of the
    #   date and time of the appointment and the values being the purpose, i.e.
    #   an entry in appts would be of format (date, time):purpose
    # __init__: None -> AppointmentBook
    def __init__(self):
        self.appts = {}

    # isAppointment(self, apptDate, apptTime) determines if an appointment
    #   exists for the date apptDate and time apptTime specified and returns
    #   True if there does, and False if there doesn't.
    # isAppointment: AppointmentBook Int Float -> Bool
    # Requires: 1 <= apptDate <=365
    #           8.0 <= apptTime <= 16.5
    def isAppointment(self, apptDate, apptTime):
        # checking the type and values of the parameters
        assert type(apptDate) is int, \
            "Invalid Type: apptDate is not an integer"
        assert type(apptTime) is float, \
            "Invalid Type: apptTime is not a float"
        assert (apptDate >= 1 and apptDate <= 365), \
            "Invalid Value: apptDate should be between 1 and 365, inclusive"
        assert (apptTime >= 8.0 and apptTime <= 16.5), \
            "Invalid Value: apptTime should be between 8.0 and 16.5, inclusive"

        appt_to_check = (apptDate, apptTime)
        return appt_to_check in self.appts

    # makeAppointment(self,apptDate,apptTime,purpose) inserts the appointment
    #   for the date apptDate, time apptTime and purpose specified (as long as
    #   it does not conflict with an existing appointment), and returns True if
    #   successfully added and False if not.
    # Effects: Mutates self.
    # makeAppointment: AppointmentBook Int Float Str -> Bool
    # Requires: 1 <= apptDate <=365
    #           8.0 <= apptTime <= 16.5
    def makeAppointment(self, apptDate, apptTime, purpose):
        # checking the type and values of the parameters
        assert type(apptDate) is int, \
            "Invalid Type: apptDate is not an integer"
        assert type(apptTime) is float, \
            "Invalid Type: apptTime is not a float"
        assert (apptDate >= 1 and apptDate <= 365), \
            "Invalid Value: apptDate should be between 1 and 365, inclusive"
        assert (apptTime >= 8.0 and apptTime <= 16.5), \
            "Invalid Value: apptTime should be between 8.0 and 16.5, inclusive"

        appt_check = not self.isAppointment(apptDate, apptTime)
        if appt_check:
            self.appts[(apptDate, apptTime)] = purpose
        return appt_check

    #deletes the appointment for the date and time specified
    def cancelAppointment(self, apptDate, apptTime):
        # checking the type and values of the parameters
        assert type(apptDate) is int, \
            "Invalid Type: apptDate is not an integer"
        assert type(apptTime) is float, \
            "Invalid Type: apptTime is not a float"
        assert (apptDate >= 1 and apptDate <= 365), \
            "Invalid Value: apptDate should be between 1 and 365, inclusive"
        assert (apptTime >= 8.0 and apptTime <= 16.5), \
            "Invalid Value: apptTime should be between 8.0 and 16.5, inclusive"

        appt_check = self.isAppointment(apptDate, apptTime)
        if appt_check:
            self.appts.pop((apptDate, apptTime))
        return appt_check

    # retrieves the purpose of the appointment if one exists
    def checkAppointment(self, apptDate, apptTime):
        # checking the type and values of the parameters
        assert type(apptDate) is int, \
            "Invalid Type: apptDate is not an integer"
        assert type(apptTime) is float, \
            "Invalid Type: apptTime is not a float"
        assert (apptDate >= 1 and apptDate <= 365), \
            "Invalid Value: apptDate should be between 1 and 365, inclusive"
        assert (apptTime >= 8.0 and apptTime <= 16.5), \
            "Invalid Value: apptTime should be between 8.0 and 16.5, inclusive"

        appt_check = self.isAppointment(apptDate, apptTime)
        if appt_check:
            return self.appts[(apptDate, apptTime)]
        return None

    #change the date or time for an appointment
    def changeAppointment(self, oldDate, oldTime, newDate, newTime):
        # checking the type and values of the parameters
        assert type(oldDate) is int, \
            "Invalid Type: oldDate is not an integer"
        assert type(oldTime) is float, \
            "Invalid Type: oldTime is not a float"
        assert (oldDate >= 1 and oldDate <= 365), \
            "Invalid Value: oldDate should be between 1 and 365, inclusive"
        assert (oldTime >= 8.0 and oldTime <= 16.5), \
            "Invalid Value: oldTime should be between 8.0 and 16.5, inclusive"

        assert type(newDate) is int, \
            "Invalid Type: newDate is not an integer"
        assert type(newTime) is float, \
            "Invalid Type: newTime is not a float"
        assert (newDate >= 1 and newDate <= 365), \
            "Invalid Value: newDate should be between 1 and 365, inclusive"
        assert (newTime >= 8.0 and newTime <= 16.5), \
            "Invalid Value: newTime should be between 8.0 and 16.5, inclusive"

        old_appt_check = not self.isAppointment(oldDate, oldTime)
        new_appt_check = self.isAppointment(newDate, newTime)
        appt_check = not(old_appt_check or new_appt_check)

        if old_appt_check:
            print("There is no appointment at {} on {}."\
                    .format(oldTime, oldDate))
        elif new_appt_check:
            print("There is already an appointment at {} on {}."\
                    .format(newTime, newDate))
        else:
            self.appts[(newDate, newTime)] = self.appts.pop((oldDate, oldTime))
            print("The appointment has been rescheduled to {} on {}."\
                    .format(newTime, newDate))

        return appt_check

    # retrieves all the appointment on the given date
    def getAppointmentsByDate(self, date):
        # checking the type and values of the parameters
        assert type(date) is int, \
            "Invalid Type: date is not an integer"
        assert (date >= 1 and date <= 365), \
            "Invalid Value: date should be between 1 and 365, inclusive"

        appt_keys = [key for key in self.appts if key[0] == date]
        appt_list = []

        for key in appt_keys:
            appt_time = key[1]
            appt_purpose = self.appts[key]
            appt_list.append((appt_time, appt_purpose))

        return appt_list
