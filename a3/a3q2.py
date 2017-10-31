##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 03, Problem 2
## ===========================================================================
##
##

from dataStructures import PriorityQueue
import check

# TODO: add design recipe
# TODO: Remove uses of _qList

# Implementation of the Stack ADT using a Priority Queue.
class Stack:
    def __init__(self):
        self._theItems = PriorityQueue()

    def isEmpty(self):
        return self._theItems.isEmpty()

    def __len__(self):
        return len(self._theItems)

    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        val = 0
        n = len(self._theItems)
        for i in range(n):
            # pop and push to end
            val = self._theItems.dequeue()
            self.push(val)
        return val

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        last = self._theItems.dequeue()
        return last

    def push(self, item):
        # Last item in list should have the highest priority
        priority = len(self) * -1
        self._theItems.enqueue(item, priority)

# Test 1: Normal use case
s = Stack()
s.push(12)
check.expect("Question 2 Test 1", s.isEmpty(), False)
s.push(98)
check.expect("Question 2 Test 1", s.peek(), 98)
s.push(14)
check.expect("Question 2 Test 1", s.pop(), 14)
check.expect("Question 2 Test 1", s.peek(), 98)
check.expect("Question 2 Test 1", len(s), 2)

# Test 2: Empty Stack
s1 = Stack()
check.expect("Question 2 Test 2", s1.isEmpty(), True)
check.expect("Question 2 Test 2", len(s1), 0)
