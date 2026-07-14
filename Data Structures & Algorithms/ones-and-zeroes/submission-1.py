import functools
from collections import Counter


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        counts = [0 for _ in range(len(strs))]
        for i in range(len(strs)):
            counter = Counter(strs[i])
            counts[i] = (counter.get("0", 0), counter.get("1", 0))

        @functools.cache
        def dfs(i, m, n):
            #print(i, m, n)
            if len(counts) == i:
                return 0
            
            mm = m - counts[i][0]
            nn = n - counts[i][1]
            
            return max(
                dfs(i+1, m, n),
                1 + dfs(i+1, mm, nn) if 0 <= mm and 0 <= nn else 0
            )


        return dfs(0, m, n)