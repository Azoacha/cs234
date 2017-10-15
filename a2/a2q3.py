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

# lst = Array(5)
# lst[3] = Event(80000, "Breakfast")
# lst[4] = Event(90000, "Woke up")
# lst[0] = Event(100000, "Dancing")
# lst[1] = Event(256, "Nappy nap")
# lst[2] = Event(39000, "Study")
# print(find_first(lst))