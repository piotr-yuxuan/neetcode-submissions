# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def binary_search(low, high) -> int:
            while low <= high:
                midpoint = (low+high)//2
                answer = guess(midpoint)
                if -1 == answer:
                    # midpoint higher than target
                    high = midpoint - 1
                elif 1 == answer:
                    # midpoint lower than target
                    low = midpoint + 1
                elif 0 == answer:
                    return midpoint
                else: 
                    raise ValueError("Impossible state")
            return -1
        
        return binary_search(1, n)