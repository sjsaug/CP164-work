"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports

# Constants

from Stack_array import Stack


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0:
        stack.push(source.pop())
    return

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())
    return

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    print("Empty Stack Test")
    print("is_empty: {}".format(stack.is_empty()))
    print()
    print("Non-Empty Stack Test")
    print("is_empty: {}".format(stack.is_empty()))
    print("push: {}".format(source[0]))
    stack.push(source[0])
    print("peek: {}".format(stack.peek()))
    print("pop: {}".format(stack.pop()))
    print("is_empty: {}".format(stack.is_empty()))
    print()
    return