"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty() and not source2.is_empty():
        target.push(source1.pop())
        target.push(source2.pop())
    while not source1.is_empty():
        target.push(source1.pop())
    while not source2.is_empty():
        target.push(source2.pop())
    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = Stack()
    while not source.is_empty():
        temp.push(source.pop())
    while not temp.is_empty():
        source.push(temp.pop())
    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    cleaned_string = ''.join(c for c in string if c.isalpha()).lower()

    stack = Stack()
    for c in cleaned_string:
        stack.push(c)

    for c in cleaned_string[:len(cleaned_string)//2]:
        if c != stack.pop():
            return False

    return True


# Constants
OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    for c in string:
        if c.isdigit():
            stack.push(c)
        elif c in OPERATORS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.push(str(eval(operand1 + c + operand2)))
    return float(stack.pop())


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = Stack()
    stack.push('Start')
    visited = set()
    path = []

    while stack:
        point = stack.peek()
        if point == 'X':
            path += ['X']
            path.pop(0)
            return path
        if point not in visited:
            visited.add(point)
            path.append(point)

            for next_point in maze.get(point, []):
                if next_point not in visited:
                    stack.push(next_point)           
        else:
            stack.pop()
            path.pop()
    return None
