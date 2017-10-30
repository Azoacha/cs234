##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 02, Problem 1
## ===========================================================================
##
##

# delete_transaction(head_trans , m) deletes the mth transaction from the
#   linked_list of records head_trans and returns the value of merch for that
#   event
# Effects: Mutates head_trans by deleting one of its nodes.
# delete_trans: Record Int -> String
# Requires: 1 <= m <= n, where n is the length of the linked list
def delete_transaction(head_trans , m):
    trans_lst = []
    curr_trans = head_trans
    while curr_trans is not None:
        trans_lst.append(curr_trans)
        curr_trans = curr_trans.prev_trans

    # the position in the list of T_m
    pos = len(trans_lst) - m
    txm = trans_lst[pos]
    txm_1 = trans_lst[pos-1]
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