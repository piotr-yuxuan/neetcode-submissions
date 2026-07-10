from collections import defaultdict


class WordDictionary:

    wildcard = '.'

    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.words = 0

    
    def __repr__(self):
        return f"{self.words=}, {self.children.keys()=}"
        

    def addWord(self, word: str) -> None:
        c = word[:1]
        if not c:
            self.words += 1
        else:
            self.children[c].addWord(word[1:])
        

    def search(self, word: str) -> bool:
        c = word[:1]
        if not c:
            return 0 < self.words
        elif c in self.children:
            return self.children[c].search(word[1:])
        elif WordDictionary.wildcard == c:
            for k in self.children.keys():
                if self.children[k].search(word[1:]):
                    return True
        
        return False
