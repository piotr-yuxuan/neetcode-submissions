# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def myMerge(start, midpoint, end) -> None:
            i = start
            j = midpoint
            tmp = []
            while i < midpoint and j < end:
                if pairs[i].key <= pairs[j].key:
                    tmp.append(pairs[i])
                    i += 1
                else:
                    tmp.append(pairs[j])
                    j += 1
            if i == midpoint:
                tmp.extend(pairs[j:end])
            else:
                tmp.extend(pairs[i:midpoint])
            #print(f"after myMerge {start=}, {end=}, {tmp=}")
            pairs[start:end] = tmp

        def myMergeSort(start, end) -> None:
            
            if (end-start) <= 1:
                return

            midpoint = (start+end) // 2
            myMergeSort(start, midpoint)
            myMergeSort(midpoint, end)
            myMerge(start, midpoint, end)

        myMergeSort(0, len(pairs))
        return pairs
        
