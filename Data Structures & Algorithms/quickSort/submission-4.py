from random import randint


# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def partition(s, e) -> int:
            left = s
            pivot = e - 1

            # Loop and swap
            for i in range(s, pivot):
                if pairs[i].key < pairs[pivot].key:
                    pairs[left], pairs[i] = pairs[i], pairs[left]
                    left += 1
            pairs[left], pairs[pivot] = pairs[pivot], pairs[left]
            return left

        # Inclusive start, exclusive end.
        def quick_sort(s, e) -> None:
            if e - s + 1 <= 1:
                return

            pivot = partition(s, e)
            quick_sort(s, pivot)
            quick_sort(pivot + 1, e)

        quick_sort(0, len(pairs))
        return pairs
