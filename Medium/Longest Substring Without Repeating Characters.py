# Problem:
# Given a string s, find the length of the longest 
# substring without repeating characters.

# Example :

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Max, left = 0, 0

        Set = set()

        for right in range(len(s)):
            while s[right] in Set:
                Set.remove(s[left])
                left += 1
            Set.add(s[right])
            Max = max(Max, right - left + 1)

        return Max
