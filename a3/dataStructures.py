# Implementation of the Queue ADT using a Python list.
class Queue:
   # Creates an empty queue.
    def __init__(self):
        self._qList = list()
    
   # Returns True if the queue is empty.
    def isEmpty(self):
        return len(self) == 0
    
   # Returns the number of items in the queue.
    def __len__(self):
        return len(self._qList)
    
   # Adds the given item to the queue.
    def enqueue(self, item):
        self._qList.append(item)
    
   # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self._qList.pop(0)

   # print(Queue) for debugging purpose
    def __str__(self):
        assert not self.isEmpty(), "Cannot print from an empty queue."
        return " ".join([str(item) for item in self._qList])



# Implementation of the unbounded Priority Queue ADT using a Python list
# with new items appended to the end.

class PriorityQueue:
    # Create an empty unbounded priority queue.
    def __init__(self):
        self._qList = list()

    # Returns True if the queue is empty.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in the queue.
    def __len__(self):
        return len(self._qList)

    # Adds the given item to the queue.
    def enqueue(self, item, priority):
        # Create a new instance of the storage class and append it to the list.
        entry = _PriorityQEntry(item, priority)
        self._qList.append(entry)

    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        # Find the entry with the highest priority.
        highest = self._qList[0].priority
        high_index = 0
        for i in range(len(self)):
            # See if the ith entry contains a higher priority (smaller integer).
            if self._qList[i].priority < highest:
                highest = self._qList[i].priority
                high_index = i

        # Remove the entry with the highest priority and return the item.
        entry = self._qList.pop(high_index)
        return entry.item

    # print(PriorityQueue) for debugging purpose
    def __str__(self):
        assert not self.isEmpty(), "Cannot print from an empty priority queue."

        return " ".join(["(" + str(node.item) + " " + str(node.priority) + ")"
                         for node in self._qList])

# Private storage class for associating queue items with their priority.
class _PriorityQEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

# Implementation of the Stack ADT using a Python list.
class Stack:
    def __init__(self):
        self._theItems = list()

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._theItems)

    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()

    def push(self, item):
        self._theItems.append(item)

    def __str__(self):
        assert not self.isEmpty(), "Cannot print from an empty stack."
        return " ".join([str(item) for item in self._theItems])


## Tree Node for Q4
class BinTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right




