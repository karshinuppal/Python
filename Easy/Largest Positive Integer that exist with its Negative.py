# Problem:
# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.

# Example:
# Input: nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.


# Solution:
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = {}
        res = -1

        for i in nums:
            temp = -1 * i
            if temp in d:
                if i < 0:
                    res = max(res, temp)
                else:
                    res = max(res, i)
            else:
                    d[i] = temp

        return res
