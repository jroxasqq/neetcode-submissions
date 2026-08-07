# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes, size = [], 0
        curr = head
        while curr:
            nodes.append(curr)
            size += 1
            curr = curr.next

        for i in range(size // 2):
            curr_node = nodes[i]
            next_node = nodes[i + 1]
            end_node = nodes[size - i - 1]
            
            curr_node.next = end_node
            end_node.next = next_node

        nodes[size // 2].next = None # prevent infinite loops
