# Problem:
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

# Solution 1:

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            dif = abs(nums[i]) - 1
            if nums[dif] < 0:
                res.append(abs(nums[i]))
            else:
                nums[dif] *= -1

        return res


# Solution 2:

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
    res = []

    for i in nums:
        i = abs(i)
        if nums[i - 1] < 0:
            res.append(i)
        nums[i - 1] = -nums[i - 1]
        
    return res
