# Problem:

# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Example:

# Input: nums = [1,2,2,3]
# Output: true

# Solution:

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i = 1

        while i < len(nums):
            if nums[i] > nums[i-1]:
                while i < len(nums):
                    if nums[i] < nums[i-1]:
                        return False
                    i += 1
                return True
            elif nums[i] < nums[i-1]:
                while i < len(nums):
                    if nums[i] > nums[i-1]:
                        return False
                    i += 1
                return True
            else:
                i += 1
        return True
