# Problem:
# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Example:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Solution:

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        res = count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while count > 1:
                count -= 1 if nums[l] == 0 else 0
                l += 1
            res = max(res, r - l)

        return res
