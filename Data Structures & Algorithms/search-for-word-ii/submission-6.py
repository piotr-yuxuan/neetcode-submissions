class PrefixTree:
    def __init__(self):
        self.children = dict()
        self.word_count = 0


    def add_word(self, word):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = PrefixTree()
            current = current.children[c]
        current.word_count += 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Backtrack all possible strings on the grid, marking a word when the current string appear in words.

        prefix_tree = PrefixTree()
        for word in words:
            prefix_tree.add_word(word)


        ret = list()

        path, seen = list(), set()

        # Return yes if word is included
        def dfs(node, path, seen, i, j) -> bool:
            if _is_oob := (i < 0 or len(board) <= i) or (j < 0 or len(board[0]) <= j):
                return False

            if (i, j) in seen:
                return False

            node = node.children.get(board[i][j], None)
            if not node:
                return False

            c = board[i][j]
            path.append(c)
            
            if 0 < node.word_count:
                ret.append(''.join(path))
                node.word_count -= 1

            seen.add((i, j))
            for i1, j1 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                dfs(node, path, seen, i1, j1)

            path.pop()
            seen.remove((i, j))


        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(prefix_tree, path, seen, i, j)
        
        return ret


