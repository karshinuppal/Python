# Problem:
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Solution:

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Max = cur = 0


        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
                Max = max(cur, Max)
            else:
                cur = 0

        return Max
