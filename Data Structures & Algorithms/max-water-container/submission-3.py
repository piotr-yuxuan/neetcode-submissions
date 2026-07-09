class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if 1 == len(heights):
            return 0

        def area(i, j):
            return (j - i) * min(heights[i], heights[j])

        i = 0
        leftmost_max_height = heights[i]
        leftmost_max_height_i = i
        j = len(heights) - 1
        rightmost_max_height = heights[j]
        rightmost_max_height_j = j

        max_area = area(i, j)
        while i < j:
            if leftmost_max_height < heights[i]:
                leftmost_max_height = max(leftmost_max_height, heights[i])
                leftmost_max_height_i = i
            if rightmost_max_height < heights[j]:
                rightmost_max_height = max(rightmost_max_height, heights[j])
                rightmost_max_height_j = j

            current_area = area(
                leftmost_max_height_i,
                rightmost_max_height_j,
            )
            #print(f"{i=}, {j=}, {heights[i]=}, {heights[j]=}, {current_area=}")
            max_area = max(
                max_area,
                current_area,
            )
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_area
