# end <= n
def leger_partition(leger_head, end_node):
    if leger_head == None or leger_head.prev_trans == None:
        return leger_head

    pivot = leger_head

    old_trans = pivot
    curr_trans = pivot.prev_trans

    while curr_trans != end_node:
        if curr_trans.time > pivot.time:
            old_trans.prev_trans = curr_trans.prev_trans
            curr_trans.prev_trans = leger_head
            leger_head = curr_trans
            curr_trans = old_trans.prev_trans
        else:
            old_trans = curr_trans
            curr_trans = curr_trans.prev_trans

    #print("Test: " + str(leger_head))
    return leger_head

def quickSort(llist, end_node):
    final_list = leger_partition(llist, None)
    quickSort(end_node, None)
    return quickSort(final_list, end_node)

def leger_quickSort(leger_head):
    pivot = leger_head
    return quickSort(leger_partition(leger_head, None), pivot)


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


tx1 = Record("apple", 2580, None)
tx2 = Record("banana", 4390, tx1)
tx3 = Record("carrot", 3452, tx2)
tx4 = Record("doll", 3789, tx3)
print(str(tx4))
print(str(leger_quickSort(tx4)))