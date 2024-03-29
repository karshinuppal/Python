Problem:
You are given an integer array nums and an integer k.
The frequency of an element x is the number of times it occurs in an array.
An array is called good if the frequency of each element in this array is less than or equal to k.
Return the length of the longest good subarray of nums.
A subarray is a contiguous non-empty sequence of elements within an array.

Example :
Input: nums = [1,2,3,1,2,3,1,2], k = 2
Output: 6
Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
It can be shown that there are no good subarrays with length more than 6.

Solution:
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {}
        res = 0
        l = 0

        for r in range(len(nums)):
            d[nums[r]] = d.get(nums[r], 0) + 1
            while d[nums[r]] > k:
                d[nums[l]] -= 1
                l += 1 
            res = max(res, r - l + 1)
        
        return res
