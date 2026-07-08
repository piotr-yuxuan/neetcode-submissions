from collections import defaultdict

class Counter:
    def __init__(self):
        self.counter = defaultdict(int)
    
    def metric(self, length) -> None:
        return length - max(self.counter.values())

    def add(self, char) -> None:
        self.counter[char] += 1
    
    def dec(self, char) -> None:
        self.counter[char] -= 1
        if 0 == self.counter[char]:
            del self.counter[char]


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Left and right both inclusive.
        def length(left, right) -> int:
            return right-left+1

        counter = Counter()
        max_length = 0
        left = 0
        for right in range(len(s)):
            counter.add(s[right])
            while k < counter.metric(length(left, right)):
                counter.dec(s[left])
                left += 1
            max_length = max(max_length, length(left, right))
        
        return max_length

