# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # with size being the number of nodes in the list,
        # the solution involves moving finding the "size - n" node from
        # the start of the list with a single list iteration.

        temp = ListNode(next=head)
        first, second = temp, temp
        counter = 1 # start at 1 since the head is included

        # loop terminates after first has moved "size" nodes
        while first:
            # since we only move second after "first" has moved n + 1 nodes,
            # the "second" will only move "size - (n + 1)" nodes as intended.
            # the n + 1 is so "second" is assigned to the node just before
            # the node to be removed.
            if counter > n + 1:
                second = second.next

            first = first.next
            counter += 1

        second.next = second.next.next

        return temp.next
    