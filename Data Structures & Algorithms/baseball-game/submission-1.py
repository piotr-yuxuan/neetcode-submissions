from collections import deque
from functools import reduce
import operator

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for op in operations:
            if 'D' == op:
                stack.append(2 * stack[-1])
            elif 'C' == op:
                stack.pop()
            elif '+' == op:
                stack.append(stack[-2] + stack[-1])
            else:
                number = int(op)
                stack.append(number)

        return reduce(operator.add, stack, 0)
        
