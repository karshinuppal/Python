# Problem:
# You are given the head of a linked list.
# Remove every node which has a node with a greater value anywhere to the right side of it.
# Return the head of the modified linked list.

# Example:
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

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


    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = self.reverse(head)

        prev = newhead
        cur = newhead.next
        res = prev

        while cur:
            if cur.val >= prev.val:
                prev.next = cur
                cur = cur.next
                prev = prev.next
            else:
                cur = cur.next

        prev.next = None
        ans = self.reverse(res)

        return ans
