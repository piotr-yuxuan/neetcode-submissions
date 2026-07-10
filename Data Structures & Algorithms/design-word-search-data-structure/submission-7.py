from collections import defaultdict, deque


class WordDictionary:

    wildcard = "."

    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.words = 0

    def addWord(self, word: str) -> None:
        current = self
        for char in word:
            current = current.children[char]
        current.words += 1

    def search(self, word: str) -> bool:
        q = deque([(self, 0)])

        while q:
            current, i = q.popleft()

            if i == len(word):
                if current.words > 0:
                    return True
                continue

            if word[i] == self.wildcard:
                for child in current.children.values():
                    q.append((child, i + 1))
            else:
                child = current.children.get(word[i])
                if child is not None:
                    q.append((child, i + 1))

        return False