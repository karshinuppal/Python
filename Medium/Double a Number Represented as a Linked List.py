# Problem:
# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
# Return the head of the linked list after doubling it.

# Example:
# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. 
# Hence, the returned linked list represents the number 189 * 2 = 378.

# Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if head == None or head.next == None:
            return head

        temp = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return temp

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = self.reverse(head)
        ans = newhead
        carry = 0

        while newhead:
            temp = (newhead.val * 2) + carry
            carry = 0
            if temp > 9:    
                rem = temp % 10
                carry = temp // 10
                newhead.val = rem
            else:
                newhead.val = temp
                
            newhead = newhead.next


        res = self.reverse(ans)

        if carry > 0:
            FNode = ListNode(carry)
            FNode.next = res
            return FNode

        return res
