import operator

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if 0 == x:
            return 0
        if 0 == n:
            return 1
        if 1 == n:
            return x
        
        positiveN = 0 < n
        n = abs(n)

        quotient, remainder = divmod(n, 2)
        a = self.myPow(x, quotient)
        result = a * a * self.myPow(x, remainder)

        return result if positiveN else 1/result