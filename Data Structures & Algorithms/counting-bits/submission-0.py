class Solution:
    def countBits(self, n: int) -> List[int]:
        def one_count(n):
            counter = 0
            while 0 < n:
                if n & 1:
                    counter += 1
                n = n >> 1
            return counter
        
        return [one_count(x) for x in range(n+1)]