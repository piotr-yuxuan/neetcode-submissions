class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0

        highest_left = [x for x in height]
        highest_right = [x for x in height]
        for i in range(1, n):
            highest_left[i] = max(highest_left[i - 1], height[i])
            highest_right[n - 1 - i] = max(highest_right[n - i], height[n - 1 - i])

        return sum(
            max(
                0,
                min(
                    highest_left[i],
                    highest_right[i],
                )
                - height[i],
            )
            for i in range(n)
        )
