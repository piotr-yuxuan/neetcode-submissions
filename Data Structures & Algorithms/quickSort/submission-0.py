# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        # Inclusive start, exclusive end.
        def my_sort(pairs, s, e) -> None:
            print(f"{s=}, {e=}, {list(x.key for x in pairs)}")
            if e-s+1 <= 1:
                return
            
            # Indices
            left = s
            pivot = e-1

            for i in range(s, pivot):
                if pairs[i].key < pairs[pivot].key:
                    pairs[i], pairs[left] = pairs[left], pairs[i]
                    left += 1
            pairs[pivot], pairs[left] = pairs[left], pairs[pivot]

            my_sort(pairs, s, left)
            my_sort(pairs, left+1, e)
        
        my_sort(pairs, 0, len(pairs))
        return pairs
