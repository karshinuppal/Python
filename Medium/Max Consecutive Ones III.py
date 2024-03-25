# Problem:
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Solution:

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = res = 0

        for r, num  in enumerate(nums):
            k -= 1 - num

            if k < 0:
                k += 1 - nums[l]
                l += 1
            else:
                res = max(res, r - l + 1)

        return res
