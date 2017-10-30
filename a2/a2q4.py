def test_delete(dup):
    tmp = dup.prev_trans
    dup.time = tmp.time
    dup.merchandise = tmp.merchandise
    dup.prev_trans = tmp.prev_trans


class Record:
    def __init__(self, merchandise, time, prev):
        self.merchandise = merchandise
        self.time = time
        self.prev_trans = prev

    def __eq__(self, other):
        if type(self) != type(other) :
            return False
        if self.merchandise == other.merchandise and \
            self.time == other.time :
            return self.prev_trans == other.prev_trans
        return False

    def __ne__(self, other):
        return not self == other

    #Converts record list into a string, where the head of the list is on the left
    #(merch, time)(merch, time)....
    def __str__(self):
        rest_of_list = ""
        if self.prev_trans != None:
            rest_of_list = str(self.prev_trans)
        return "({},{})".format(self.merchandise, self.time) + rest_of_list

tx1 = Record("apple", 5580, None)
tx2 = Record("banana", 1580, tx1)
tx3 = Record("carrot", 3452, tx2)
tx4 = Record("doll", 4789, tx3)
print(tx4)
test_delete(tx2)
print(tx4)