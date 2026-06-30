class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        board_counter = Counter(c for row in board for c in row)
        if board_counter < Counter(word):
            return False

        def dfs(i, j, k) -> bool:
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            # A clever thing here comes from using the input itself in place 
            # as a reference for backtracking.
            board[i][j] = None
            # I feel sorry for the Python parser.
            for x, y in (i, j-1), (i, j+1), (i-1, j), (i+1, j):
                if dfs(x, y, k+1):
                    # Again from efficient the sample code I read after submitting my
                    # solution, we can return True early and break the backtracking
                    # here since we just want to have one answer.
                    return True
            # Some other nice thing is to restore the value from the word
            # itself and not from a variable.
            board[i][j] = word[k]

            return False

        # Something else equally nice is the use of idiomatic `any` as here.
        return any(
            dfs(i, j, 0)
            for i in range(len(board))
            for j in range(len(board[0]))
        )
