from collections import defaultdict


class WordDictionary:

    wildcard = '.'

    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.words = 0
        

    def addWord(self, word: str) -> None:
        c = word[:1]
        if not c:
            self.words += 1
        else:
            self.children[c].addWord(word[1:])
            if WordDictionary.wildcard != c:
                self.children[WordDictionary.wildcard].addWord(word[1:])
        

    def search(self, word: str) -> bool:
        c = word[:1]
        print(f"DEBUG 1 {word=}, {c=}, {(c in self.children)=}")
        if not c:
            return 0 < self.words

        if c in self.children:
            return self.children[c].search(word[1:])
            print(f"DEBUG 1 {word=}, {c=}, {(c in self.children)=}, {is_found=}")
        return False

        
