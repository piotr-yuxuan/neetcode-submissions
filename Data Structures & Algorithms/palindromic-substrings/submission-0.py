class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        t = '#' + '#'.join(c for c in s) + '#'
        for i in range(len(t)):
            radius = 0
            while 0 <= i-radius and i+radius < len(t) and t[i-radius] == t[i+radius]:
                if '#' != t[i-radius] and '#' != t[i+radius]:
                    result += 1
                radius += 1
        return result
