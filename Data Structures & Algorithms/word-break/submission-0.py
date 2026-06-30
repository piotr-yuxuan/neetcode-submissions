import functools

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Return whether the string starting at this index (inclusive) can be seen as composed of words from dict.
        @functools.cache
        def dfs(i):
            if len(s) == i:
                return True
            elif len(s) < i:
                return False
            
            for word in wordDict:
                if word == s[i:i+len(word)]:
                    if dfs(i+len(word)):
                        return True
            return False
        
        return dfs(0)