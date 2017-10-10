def delete_transaction(head_trans , m):
    trans_lst = []
    curr_trans = head_trans
    while curr_trans is not None:
        trans_lst.append(curr_trans)
        curr_trans = curr_trans.prev_trans

    n = len(trans_lst)
    txm = trans_lst[n-m]
    txm_1 = trans_lst[n-m-1]
    merch = txm.merchandise

    txm_1.prev_trans = txm.prev_trans
    return merch


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


#tx1 = Record("apple", 1580, None)
#tx2 = Record("banana", 2390, tx1)
#tx3 = Record("carrot", 3452, tx2)
#tx4 = Record("doll", 3789, tx3)