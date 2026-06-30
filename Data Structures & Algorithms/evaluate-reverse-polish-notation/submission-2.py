class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '-': lambda x, y: x - y,
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / float(y))
        }
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(token)
                continue
            op = operations[token]
            stack.append(
                op(y=int(stack.pop()), x=int(stack.pop()))
            )
        return int(stack.pop())