from collections import defaultdict


class WordDictionary:

    wildcard = '.'

    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.words = 0


    def addWord(self, word: str, i=0) -> None:
        if len(word) <= i:
            self.words += 1
        else:
            self.children[word[i]].addWord(word, i+1)


    def search(self, word: str, i=0) -> bool:
        if len(word) <= i:
            return 0 < self.words
        elif word[i] in self.children:
            return self.children[word[i]].search(word, i+1)
        elif WordDictionary.wildcard == word[i]:
            for k in self.children.keys():
                if self.children[k].search(word, i+1):
                    return True
        
        return False
