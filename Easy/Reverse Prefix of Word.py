# Problem:
# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

# Example:
# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

# Solution:

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = 0
        for i in range(len(word)):
            if word[i] == ch:
                ind = i
                break

        res = word[:ind + 1][::-1] + word[ind+1:]


        return res
