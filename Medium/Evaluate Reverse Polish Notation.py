# Problem:
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example :

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in '+-*/':
                stack.append(i)
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    Sum = int(b) + int(a)
                elif i == '-':
                    Sum = int(b) - int(a)
                elif i == '*':
                    Sum = int(b) * int(a)
                else:
                    Sum = int(b) / int(a)
                stack.append(Sum)
        
        return int(stack.pop())
