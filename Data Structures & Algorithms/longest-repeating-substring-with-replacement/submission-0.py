from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Left and right both inclusive.

        def metric(left, right):
            counter = Counter(s[left:right+1])
            length = right-left + 1
            return length - max(counter.values())
        
        max_length = 0
        left = 0
        for right in range(len(s)):
            while k < metric(left, right):
                left += 1
            max_length = max(max_length, (right-left+1))
        
        return max_length
                
