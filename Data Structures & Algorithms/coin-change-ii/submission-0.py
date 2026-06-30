import functools

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Return the number of possible combinations.
        @functools.cache
        def dfs(current, adding_coin):
            if amount == current:
                return 1
            elif amount < current:
                return 0
            if len(coins) <= adding_coin:
                return 0

            # Either we add more of the coin, either we the next coin.
            return dfs(current + coins[adding_coin], adding_coin) + dfs(current, adding_coin+1)

        return dfs(0, 0)
