# Problem:

# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Solution:

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}

        for i in nums:
            d[i] = d.get(i, 0) + 1

        count = 0

        for key, value in d.items():
            if value > 1:
                count += (value * (value - 1)) // 2

        return count
