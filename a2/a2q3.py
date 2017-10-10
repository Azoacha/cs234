from myArray import Array

# TODO: Add design recipe
# TODO: Explain why this is O(log n) - use the logic behind binary searches

def find_first(disordered):
    low = 0
    high = len(disordered) - 1
    first_time = disordered[0].time

    while low <= high:
        mid = 1 + (high + low)//2
        if high == low:
            return disordered[low]
        elif disordered[mid].time < disordered[mid-1].time:
            return disordered[mid]
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

#lst = Array(5)
#lst[1] = Event(256, "Nappy nap")
#lst[0] = Event(10000, "Dancing")
#lst[2] = Event(39000, "Study")
#lst[3] = Event(80000, "Breakfast")
#st[4] = Event(90000, "Woke up")
#print(find_first(lst).event)