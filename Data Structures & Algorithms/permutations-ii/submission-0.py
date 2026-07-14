from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(counter) -> List[List[int]]:
            input = dict(counter)

            if not counter:
                return [[]]
            
            permutations = []
            keys = list(counter.keys())
            for k in keys:
                v = counter[k]
                counter[k] -= 1
                if 0 == counter[k]:
                    del counter[k]
                for p in backtracking(counter):
                    q = [k] + p
                    permutations.append(q)
                counter[k] = v

            return permutations

        return backtracking(Counter(nums))