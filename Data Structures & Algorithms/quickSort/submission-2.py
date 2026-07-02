from random import randint

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        # Inclusive start, exclusive end.
        def my_sort(pairs, s, e) -> None:
            if e-s+1 <= 1:
                return
            
            left = s
            pivot = e-1

            # Loop and swap
            for i in range(s, pivot):
                if pairs[i].key < pairs[pivot].key:
                    pairs[left], pairs[i] = pairs[i], pairs[left]
                    left += 1
            pairs[left], pairs[pivot] = pairs[pivot], pairs[left]

            my_sort(pairs, s, left)
            my_sort(pairs, left+1, e)


        my_sort(pairs, 0, len(pairs))
        return pairs
