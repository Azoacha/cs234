##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 03, Problem 4
## ===========================================================================
##
##

from dataStructures import BinTreeNode, Stack

def inorderTraversal(root):
    order = Stack()
    if root is not None:
        inorderTraversal(root.left)
        order.push(root.data)
        inorderTraversal(root.right)

    n = len(order)
    traversal = [0]*n
    for i in range(n-1, -1, -1):
        traversal[i] = order.pop()

    return traversal

