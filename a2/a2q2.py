##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 02, Problem 2
## ===========================================================================
##
##

def swap(node1, node2):
    tmp_time = node1.time
    tmp_merch = node1.merchandise

    node1.time = node2.time
    node1.merchandise = node2.merchandise

    node2.time = tmp_time
    node2.merchandise = tmp_merch

# Returns true if node1 appears in list before node2,
#   i.e. head -> ... -> node1 -> ... -> node2 -> ... -> None
def appears_before(node1, node2):
    if node2 == None:
        return True
    curr = node1
    while curr != None:
        if curr == node2:
            return True
        curr = curr.prev_trans
    return False

# Partitions list as in quicksort and returns node that appears before pivot
def partition(first, last):
    # Using last node for pivot since it has no tail nodes
    # comp_node will be ahead of every node < pivot
    pivot = last
    comp_node = first
    prev_node = comp_node
    curr = first

    while curr != pivot:
        if curr.time >= pivot.time:
            swap(comp_node, curr)
            prev_node = comp_node
            comp_node = comp_node.prev_trans
        curr = curr.prev_trans
    swap(comp_node, pivot)
    return prev_node

def recQuickSort(first, last):
    if appears_before(last, first):
        return
    else:
        # Not the true pivot, but the node before it i.e. node.prev_trans =
        #   true pivot
        pivot = partition(first, last)
        recQuickSort(first, pivot)
        recQuickSort(pivot.prev_trans, last)

# leger_quicksort(leger_head) sorts a given linked list of records leger_head
#   using the logic of quicksort and returns the head node of the newly sorted
#   list
# Effects: Mutates leger_head
# leger_quickSort: Record -> Record
def leger_quickSort(leger_head):
    # set to head and not head.prev_trans to account for empty list
    curr = leger_head
    last = leger_head
    while curr != None:
        last = curr
        curr = curr.prev_trans
    recQuickSort(leger_head, last)
    return leger_head


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