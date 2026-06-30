class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)

        if not self.max_stack:
            self.max_stack.append(val)
        elif self.max_stack[-1] <= val:
            self.max_stack.append(val)


    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()
        if self.max_stack[-1] == val:
            self.max_stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
