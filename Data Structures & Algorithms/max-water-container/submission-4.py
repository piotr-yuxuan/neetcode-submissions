class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if 1 == len(heights):
            return 0

        def area(i, j):
            return (j - i) * min(heights[i], heights[j])

        i = 0
        leftmost_max_height_i = i
        j = len(heights) - 1
        rightmost_max_height_j = j

        max_area = area(i, j)
        while i < j:
            if heights[leftmost_max_height_i] < heights[i]:
                leftmost_max_height_i = i
            if heights[rightmost_max_height_j] < heights[j]:
                rightmost_max_height_j = j

            max_area = max(
                max_area,
                area(
                    leftmost_max_height_i,
                    rightmost_max_height_j,
                ),
            )
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_area
