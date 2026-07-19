class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(x for x in s) + '#'
        
        max_radius = 0
        center = 0
        for i in range(len(t)):
            radius = 0
            while 0 <= i-radius and i+radius < len(t) and t[i-radius] == t[i+radius]:
                if max_radius < radius:
                    max_radius = radius
                    center = i
                radius += 1
        return s[(center-max_radius)//2: (center+max_radius)//2]