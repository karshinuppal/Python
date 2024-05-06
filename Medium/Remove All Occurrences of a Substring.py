# Problem:
# Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
# Find the leftmost occurrence of the substring part and remove it from s.
# Return s after removing all occurrences of part.
# A substring is a contiguous sequence of characters in a string.

# Example:
# Input: s = "daabcbaabcbc", part = "abc"
# Output: "dab"
# Explanation: The following operations are done:
# - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
# - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
# - s = "dababc", remove "abc" starting at index 3, so s = "dab".
# Now s has no occurrences of "abc".

# Solution:

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if len(part) == 1:
            for i in s:
                s = s.replace(part, "")
            return s



        stack = []

        for i in s:
            if i == part[-1]:
                l = len(part) - 1
                temp = "".join(stack[-l:]) + i
                if part == temp:
                    while l:
                        stack.pop()
                        l -= 1
                else:
                    stack.append(i)
            else:
                stack.append(i)

        res = "".join(stack)

        return res
