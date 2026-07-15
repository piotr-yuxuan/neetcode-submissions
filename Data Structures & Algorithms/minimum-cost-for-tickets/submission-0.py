import functools
from bisect import bisect_left


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        durations = (1, 7, 30)

        # Return the cost
        @functools.cache
        def dfs(i) -> int:
            if len(days) <= i:
                return 0

            return min(
                cost + dfs(bisect_left(days, days[i] + duration))
                for duration, cost in zip(durations, costs)
            )

        return dfs(0)
