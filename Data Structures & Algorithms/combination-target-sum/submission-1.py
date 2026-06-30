class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        result = []
        work = []

        def backtrack(i, remainder):
            if 0 == remainder:
                result.append(work[::])
                return
            elif remainder < 0:
                return
            elif len(candidates) == i:
                # Discard the current work.
                return

            if candidates[i] <= remainder:
                work.append(candidates[i])
                backtrack(i, remainder - candidates[i])
                work.pop()
            backtrack(i+1, remainder)

        backtrack(0, target)
        return result
