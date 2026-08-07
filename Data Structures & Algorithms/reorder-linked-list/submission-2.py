# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list in half (by finding mid node), and then reverse
        # the second half. traverse both halves simultaneous and re-assign
        # pointers as necessary.

        mid_node, temp = head, head
        while temp and temp.next:
            mid_node = mid_node.next
            temp = temp.next.next
        
        # by the above "slow and fast" traversal, the second reversed list
        # is always equal size or one greater than the first list.
        curr1, curr2 = head, self.reverseList(mid_node)
        while curr1:
            curr1.next, curr1 = curr2, curr1.next
            if curr2:
                curr2.next, curr2 = curr1, curr2.next
            
