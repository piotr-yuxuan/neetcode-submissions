class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for line in logs:
            if './' == line:
                pass
            elif '../' == line:
                depth = max(0, depth - 1)
            else:
                depth += 1
        return depth
