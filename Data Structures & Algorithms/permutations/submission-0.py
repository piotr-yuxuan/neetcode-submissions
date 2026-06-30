class Solution:

    # Naive.
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(l: List):
            if 1 == len(l):
                return [l]
            values = []
            for i in range(len(l)):
                for sublist in permutations(l[:i] + l[i+1:]):
                    values.append([l[i]] + sublist)
            return values
        
        return permutations(nums)

    # Backtracking with seen set.
    def _permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        work = []
        seen = set()

        def backtrack():
            if len(work) == len(nums):
                result.append(work[:])
                return
            for i in range(len(nums)):
                if i in seen:
                    continue
                seen.add(i)
                work.append(nums[i])
                backtrack()
                work.pop()
                seen.remove(i)

        backtrack()
        return result

    # Idiomatic, https://en.wikipedia.org/wiki/Heap%27s_algorithm
    def _permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        work = nums

        def swap(i, j) -> None:
            nums[i], nums[j] = nums[j], nums[i]

        def permutations(k) -> None:
            if 1 == k:
                result.append(work[::])
                return
            
            # Permutations with last element fixed.
            permutations(k-1)

            # Permutations with last element swapped out.
            for i in range(k-1):
                if k % 2 == 0:
                    swap(i, k-1)
                else:
                    swap(0, k-1)
                permutations(k-1)

        permutations(len(nums))
        return result

    # Vanilla, https://en.wikipedia.org/wiki/Heap%27s_algorithm
    def _permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def swap(A, i, j) -> None:
            A[i], A[j] = A[j], A[i]

        def permutations(k, A) -> None:
            if 1 == k:
                result.append(A[::])
                return
            
            # Permutations with last element fixed.
            permutations(k-1, A)
            # Permutations with last element swapped out.
            for i in range(k-1):
                if k % 2 == 0:
                    swap(A, i, k-1)
                else:
                    swap(A, 0, k-1)
                permutations(k-1, A)

        permutations(len(nums), nums)
        return result


    def _permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(l: List):
            if 1 == len(l):
                return [l]
            values = []
            for i in range(len(l)):
                for sublist in permutations(l[:i] + l[i+1:]):
                    values.append([l[i]] + sublist)
            return values

        return permutations(nums)