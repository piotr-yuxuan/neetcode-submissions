class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)

        result = []
        path = []

        def backtrack(i, remainder) -> None:
            if 0 == remainder:
                result.append(path[::])
                return
            if remainder < 0:
                return
            if len(candidates) == i:
                return

            path.append(candidates[i])
            backtrack(i+1, remainder - candidates[i])

            # Since we sort the array, avoiding duplicates means skipping
            # values we've already seen here.
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            path.pop()
            backtrack(i+1, remainder)
        
        backtrack(0, target)
        return result