##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 02, Problem 3
## ===========================================================================
##
##

from myArray import Array

# find_first(disordered) finds the time of the first event in the array
#   disordered that has been split and concatenated incorrectly
# find_first: Array -> Int
# Requires: disordered contains a break, i.e. it was an ordered list that was
#   split and concatenated incorrectly
def find_first(disordered):
    low = 0
    high = len(disordered) - 1
    first_time = disordered[0].time

    while low <= high:
        mid = 1 + (high + low)//2
        if high == low:
            return disordered[low].time
        elif disordered[mid].time < disordered[mid-1].time:
            return disordered[mid].time
        elif disordered[mid].time < first_time:
            high = mid - 1
        else:
            low = mid + 1

class Event:
    def __init__(self, time, event):
        self.time = time
        self.event = event

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.time == other.time:
            return self.event == other.event
        return False