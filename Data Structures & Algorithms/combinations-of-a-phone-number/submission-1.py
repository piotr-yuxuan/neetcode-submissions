class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        values = []
        if 0 == len(digits):
            return values

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ret = []
        def backtracking(i, a):
            if len(digits) == i:
                ret.append(''.join(a))
                return
            
            for l in letters[digits[i]]:
                a.append(l)
                backtracking(i+1, a)
                a.pop()
        
        backtracking(0, list())
        return ret