class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        work = []

        m = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }

        def backtrack(i) -> None:
            if len(digits) == i:
                if work:
                    result.append(''.join(work))
                return
            
            for c in m[digits[i]]:
                work.append(c)
                backtrack(i+1)
                work.pop()
        
        backtrack(0)
        return result