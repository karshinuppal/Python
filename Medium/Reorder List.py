# Problem:

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        rev_head = slow.next
        slow.next = None

        prev = None
        while rev_head:
            temp = rev_head.next
            rev_head.next = prev
            prev = rev_head
            rev_head = temp

        cur = head
        while prev:
            next1 = cur.next
            next2 = prev.next
            cur.next = prev
            prev.next = next1
            cur = next1
            prev = next2

        return head
      
