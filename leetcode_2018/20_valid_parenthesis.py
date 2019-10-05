"""
20. Valid Parenthesis

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: '()'
Output: true
Example 2:

Input: '()[]{}'
Output: true
Example 3:

Input: '(]'
Output: false

"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            # it's a closing bracket
            top_elem = stack.pop() if stack else '#'
            if top_elem != mapping[char]:
                return False
        else:
            # it's a opening bracket
            stack.append(char)
    return not stack
