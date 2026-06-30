import functools

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        # – i for s1,
        # – j for s2, 
        @functools.cache
        def dfs(i, j):
            #print(f"i={i}, j={j}, s1[:i]={s1[:i]}, s2[:j]={s2[:j]}, s3[i+j]={s3[:i+j]}")
            if i < len(s1) and s3[i+j] == s1[i]:
                if dfs(i+1, j):
                    return True
            if j < len(s2) and s3[i+j] == s2[j]:
                if dfs(i, j+1):
                    return True
            return i == len(s1) and j == len(s2)
        
        return dfs(0, 0)

