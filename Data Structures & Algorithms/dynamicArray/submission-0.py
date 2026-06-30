class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None for _ in range(capacity)]


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        element = self.array[self.size-1]
        self.array[self.size-1] = None
        self.size -= 1

        return element
 

    def resize(self) -> None:
        self.array.extend(
            [None for _ in range(self.capacity)]
        )
        self.capacity *= 2
        return None

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
