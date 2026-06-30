class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        prev = -1
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            current_max = max(current_max, prev)
            arr[i] = current_max
            prev = current

        return arr

