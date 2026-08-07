class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    # assume only values at indices previously "pushed back" can be set.
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        popped = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1

        return popped

    # resize the instance's array to double capacity.
    def resize(self) -> None:
        self.array += ([None] * self.capacity)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
