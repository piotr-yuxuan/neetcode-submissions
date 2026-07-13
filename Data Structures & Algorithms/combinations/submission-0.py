class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ret = list()
        current = list()
        def backtracking(i):
            if n < i:
                if k == len(current):
                    ret.append(list(current))
                return
            
            current.append(i)
            backtracking(i+1)
            current.pop()
            backtracking(i+1)
        
        backtracking(1)
        return ret