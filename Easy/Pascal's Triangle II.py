# Problem:
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
 
# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

# Solution:

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]

        if rowIndex == 0:
            return res[0]
        if rowIndex == 1:
            return [1, 1]

        for i in range(rowIndex):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        
        return res[-1]
        
                
