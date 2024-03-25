# Problem:
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Solution:

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            i = abs(i)
            if nums[i - 1] < 0:
                return i
            nums[i - 1] = -nums[i - 1]
