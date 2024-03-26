# Problem:
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Solution:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i, val in enumerate(nums):
            val = abs(val)
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val -1] = -nums[val -1]
                elif nums[val - 1] == 0:
                    nums[val - 1] = -(len(nums) + 1)

        for i in range(1,len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1
