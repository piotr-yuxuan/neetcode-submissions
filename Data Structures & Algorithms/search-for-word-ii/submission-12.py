class PrefixTree:
    def __init__(self):
        self.children = dict()
        self.word = None


    def add_word(self, word):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = PrefixTree()
            current = current.children[c]
        current.word = word
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Backtrack all possible strings on the grid, marking a word when the current string appear in words.

        prefix_tree = PrefixTree()
        for word in words:
            prefix_tree.add_word(word)


        ret = list()

        path = list()

        # Return yes if word is included
        def dfs(node, path, i, j) -> bool:
            if _is_oob := (i < 0 or len(board) <= i) or (j < 0 or len(board[0]) <= j):
                return False

            node = node.children.get(board[i][j], None)
            if not node:
                return False

            c = board[i][j]
            board[i][j] = None
            path.append(c)
            
            if word := node.word:
                ret.append(word)
                node.word = ""

            dfs(node, path, i-1, j)
            dfs(node, path, i+1, j)
            dfs(node, path, i, j-1)
            dfs(node, path, i, j+1)

            path.pop()
            board[i][j] = c


        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(prefix_tree, path, i, j)
        
        return ret


