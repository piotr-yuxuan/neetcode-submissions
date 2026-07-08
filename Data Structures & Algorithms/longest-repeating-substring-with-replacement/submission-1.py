from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Left and right both inclusive.

        def metric(counter, left, right):
            return right-left+1 - max(counter.values())

        def add(counter, char):
            counter[char] += 1
        
        def dec(counter, char):
            counter[char] -= 1
            if 0 == counter[char]:
                del counter[char]

        counter = defaultdict(int)
        max_length = 0
        left = 0
        for right in range(len(s)):
            add(counter, s[right])
            while k < metric(counter, left, right):
                dec(counter, s[left])
                left += 1
            max_length = max(max_length, (right-left+1))
        
        return max_length

