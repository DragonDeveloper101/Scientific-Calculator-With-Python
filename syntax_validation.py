from math import *
from collections import deque

# This function checks if all the brackets in the inputted expression are all corresponding and valid

def brackets_valid(string):
    brackets = {
        ")": "(",
        "}": "{",
        "]": "["
        }
    stack = deque()

    # if string[0] not in brackets.values(): return False

    for bracket in string:
        if bracket in brackets.values():
            stack.appendleft(bracket)
        elif bracket not in brackets.keys():
            continue
        else:
            if len(stack) == 0 or brackets[bracket] != stack[0]:
                return False
            else:
                stack.popleft()

    if len(stack) != 0:
        return False

    return True
