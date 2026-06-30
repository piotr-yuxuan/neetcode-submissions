class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for line in logs:
            if './' == line:
                pass
            elif '../' == line:
                if stack:
                    stack.pop()
            else:
                stack.append(line)
        return len(stack)