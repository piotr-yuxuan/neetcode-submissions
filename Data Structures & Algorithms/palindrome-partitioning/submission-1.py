import functools

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s) -> bool:
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True

        @functools.cache
        def dfs(s) -> List[List[str]]:
            if 1 == len(s):
                return [[s]]

            partitions = []
            for i in range(1, len(s)):
                x = s[:i]
                if not is_palindrome(x):
                    continue
                for y in dfs(s[i:]):
                    partitions.append([x] + y)
            if is_palindrome(s):
                partitions.append([s])
            return partitions

        return dfs(s)        