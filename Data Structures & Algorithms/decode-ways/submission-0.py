def solution(input: str) -> int:
    n = len(input)

    valid_one = {str(i) for i in range(1, 10)}
    valid_two = {str(i) for i in range(10, 27)}

    def dfs(i) -> int:
        if n <= i:
            return 1

        code_one = dfs(i + 1) if input[i : i + 1] in valid_one else 0
        code_two = dfs(i + 2) if input[i : i + 2] in valid_two else 0
        return code_one + code_two

    return dfs(0)


class Solution:
    def numDecodings(self, s: str) -> int:
        return solution(s)