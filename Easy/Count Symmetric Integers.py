# Question:

# You are given two positive integers low and high.

# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

# Return the number of symmetric integers in the range [low, high].

# Example 1:

# Input: low = 1, high = 100
# Output: 9
# Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

# Solution:

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for i in range(low, high+1):
            if len(str(i)) % 2 == 1:
                continue
            else:
                mid = len(str(i)) // 2
                num = str(i)
                sum1, sum2 = 0, 0
                for j in num[:mid]:
                    sum1 += int(j)
                for j in num[mid:]:
                    sum2 += int(j)
                if sum1 == sum2:
                    res += 1

        return res
