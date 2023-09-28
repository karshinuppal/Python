# Problem:

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

# Example:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Solution 1:

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0

        for r in range(len(nums)):
            if  nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return nums

# Solution 2:

 class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
      res = []

        for i in nums:
            if i % 2 == 0:
                res.append(i)
        
        for i in nums:
            if i % 2 != 0:
                res.append(i)

        return res

# Solution 3:

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] % 2 != 0 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
            elif nums[i] % 2 == 0:
                i += 1
            elif nums[j] % 2 != 0:
                j -= 1

        return nums  
