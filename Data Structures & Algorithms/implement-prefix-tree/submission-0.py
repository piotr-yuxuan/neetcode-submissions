from collections import defaultdict

class PrefixTree:

    def __init__(self):
        self.children = defaultdict(PrefixTree)
        self.word = 0
        

    def insert(self, word: str) -> None:
        c = word[:1]
        if not c:
            self.word += 1
        else:
            self.children[c].insert(word[1:])


    def _search(self, word: str) -> Optional[PrefixTree]:
        c = word[:1]
        if not c:
            return self
        elif c in self.children:
            return self.children[c]._search(word[1:])
        else:
            return None


    def search(self, word: str) -> bool:
        leaf = self._search(word)
        #print(f"search {word=}, {leaf=}")
        return bool(leaf and 0 < leaf.word)


    def startsWith(self, prefix: str) -> bool:
        leaf = self._search(prefix)
        return bool(leaf)
        