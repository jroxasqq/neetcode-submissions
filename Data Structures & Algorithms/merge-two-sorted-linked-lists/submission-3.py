# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        curr1, curr2 = list1, list2
        temp = ListNode() # tracks the tail of merged list
        while curr1 and curr2:
            while curr1 and curr2 and curr1.val <= curr2.val:
                temp = curr1
                curr1 = curr1.next
            temp.next = curr2
            while curr1 and curr2 and curr2.val <= curr1.val:
                temp = curr2
                curr2 = curr2.next
            temp.next = curr1

        if curr2 is not None:
            temp.next = curr2
        if curr1 is not None:
            temp.next = curr1
        
        return list1 if list1.val <= list2.val else list2
             
