class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s.casefold() if c.isalnum()]
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True