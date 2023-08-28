# Problem:

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.
 

# Example:

# Input: s = "()"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        d = { ')':'(', ']':'[', '}':'{'}

        stack = []

        for i in s:
            if i in d:
                if not stack:
                    return False
                elif stack[-1] != d[i]:
                    return False
                elif stack and stack[-1] == d[i]:
                    print(stack[-1])
                    stack.pop()
            else:
                stack.append(i)

        if not stack:
            return True
        return False
