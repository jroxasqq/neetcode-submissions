# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, follow = None, head, head
        while curr:
            follow = follow.next
            curr.next = prev
            prev = curr
            curr = follow

        return prev
        