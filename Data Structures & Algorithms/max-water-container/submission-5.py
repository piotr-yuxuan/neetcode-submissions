class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if 1 == len(heights):
            return 0

        def area(i, j):
            return (j - i) * min(heights[i], heights[j])

        i = 0
        j = len(heights) - 1

        max_area = area(i, j)
        while i < j:
            current_area = area(
                i,
                j
            )
            max_area = max(max_area, current_area)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_area
