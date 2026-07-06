class MinHeap:
    
    def __init__(self):
        dummy = None
        self.empty = [dummy]
        self.a = self.empty
        

    def push(self, val: int) -> None:
        i = len(self.a)
        self.a.append(val)

        # Percolate up
        while 1 < i and self.a[i] < self.a[i//2]:
            self.a[i], self.a[i//2] = self.a[i//2], self.a[i]
            i = i//2


    def _percolate_down(self, i) -> None:
        #print(f"_percolate_down {self.a=}")
        while 2*i < len(self.a):
            #print(f"_percolate_down loop {i=}, {self.a=}")
            left_val = self.a[2*i]
            if 2*i+1 < len(self.a):
                right_val = self.a[2*i+1]
                #print(f"{i=}, {self.a[i]=}, {left_val=}, {right_val=} left and right")
                if self.a[i] <= min(left_val, right_val):
                    break
                elif left_val < self.a[i] and left_val <= right_val:
                    self.a[2*i], self.a[i] = self.a[i], self.a[2*i]
                    i = 2*i
                else:
                    self.a[2*i+1], self.a[i] = self.a[i], self.a[2*i+1]
                    i = 2*i+1
            else:
                #print(f"{i=}, {self.a[i]=}, {left_val=} left only")
                if self.a[i] <= left_val:
                    break
                else:
                    self.a[2*i], self.a[i] = self.a[i], self.a[2*i]
                    i = 2*i
        #print(f"_percolate_down end {self.a}")


    def pop(self) -> int:
        #print(f"pop")
        if len(self.a) == 1:
            return -1

        ret = self.a[1]
        self.a[1] = self.a[-1]
        self.a.pop()

        i = 1
        self._percolate_down(i)
        return ret


    def top(self) -> int:
        if len(self.a) == 1:
            return -1
    
        return self.a[1]
        

    def heapify(self, nums: List[int]) -> None:
        #print("heapify")
        self.a = self.empty + nums
        if len(self.a) in {1, 2}:
            return
        
        i = (len(self.a)-1)//2
        #print(f"{self.a=}, {i=}")
        while 1 <= i:
            self._percolate_down(i)
            #print(f"{self.a=}, {i=}")
            i -= 1
