import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = max(0, bisect.bisect_left(arr, x)-(k))
        right = min(len(arr)-1, bisect.bisect_right(arr, x)+(k))

        while k < right-left+1:
            if x-arr[left] <= arr[right]-x:
                right -= 1
            else:
                left += 1
        return arr[left:right+1]