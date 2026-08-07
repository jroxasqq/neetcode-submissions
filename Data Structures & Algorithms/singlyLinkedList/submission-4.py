class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def setNext(self, other):
        self.next = other

class LinkedList:
    
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        curr_index: int = 0
        curr_node: Node = self.head
        while curr_index < index:
            curr_node = curr_node.next
            curr_index += 1

        return curr_node.val

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.setNext(self.head)

        self.head = newNode
        if self.size == 0:
            self.tail = newNode

        self.size += 1

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.tail:
            self.tail.setNext(newNode)

        self.tail = newNode
        if self.size == 0:
            self.head = newNode

        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False

        if index == 0:
            # removing the head.
            self.head = self.head.next
        else:
            # removing from the middle or the tail.
            curr_index: int = 0
            curr_node: Node = self.head
            while curr_index < index - 1:
                curr_node = curr_node.next
                curr_index += 1
            
            # curr_node should be the node just before the node to be removed.
            curr_node.next = curr_node.next.next

            # if we removed the tail.
            if index == self.size - 1:
                self.tail = curr_node

        self.size -= 1

        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values
