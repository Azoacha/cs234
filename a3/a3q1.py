##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 03, Problem 1
## ===========================================================================
##
##

from dataStructures import Queue
import check

# TODO: add design recipe

# Implementation of the Stack ADT using a single Queue.
class Stack:
    def __init__(self):
        self._theItems = Queue()

    def isEmpty(self):
        return self._theItems.isEmpty()

    def __len__(self):
        return len(self._theItems)

    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems._qList[-1]

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems._qList.pop(-1)

    def push(self, item):
        self._theItems.enqueue(item)

# Test 1: Normal use case
s = Stack()
s.push(12)
check.expect("Question 1 Test 1", s.isEmpty(), False)
s.push(98)
check.expect("Question 1 Test 1", s.peek(), 98)
s.push(14)
check.expect("Question 1 Test 1", s.pop(), 14)
check.expect("Question 1 Test 1", s.peek(), 98)
check.expect("Question 1 Test 1", len(s), 2)

# Test 2: Empty Stack
s1 = Stack()
check.expect("Question 1 Test 2", s1.isEmpty(), True)
check.expect("Question 1 Test 2", len(s1), 0)
