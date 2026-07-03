
class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


    # Iterative, no recursion.
    def insert(self, key: int, value: int) -> None:
        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key, value)
            else:
                self.left.insert(key, value)
        elif self.key < key:
            if self.right is None:
                self.right = TreeNode(key, value)
            else:
                self.right.insert(key, value)
        else:
            self.value = value


    def get(self, key: int) -> int:
        if key < self.key and self.left:
            return self.left.get(key)
        elif self.key < key and self.right:
            return self.right.get(key)
        elif self.key == key:
            return self.value
        return -1

    def _getMin(self) -> TreeNode:
        current = self
        while current.left is not None:
            current = current.left
        return current


    def getMin(self) -> int:
        return self._getMin().value


    def getMax(self) -> int:
        current = self
        while current.right:
            current = current.right
        return current.value


    def remove(self, key: int) -> None:
        if self.key == key:
            if not self.left and not self.right:
                self.key = None # Flag for removal
                return
            elif self.left and not self.right:
                self.key = self.left.key
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
            elif not self.left and self.right:
                self.key = self.right.key
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            else:
                successor = self.right._getMin()
                self.key = successor.key
                self.value = successor.value
                self.right.remove(successor.key)
        elif self.right and self.key < key:
            self.right.remove(key)
        elif self.left and key < self.key:
            self.left.remove(key)
        
        if self.right and self.right.key is None:
            self.right = None
        if self.left and self.left.key is None:
            self.left = None


    def getInorderKeys(self) -> List[int]:
        def walk(node):
            if not node:
                return
            yield from walk(node.left)
            yield node.key
            yield from walk(node.right)
        
        return list(x for x in walk(self))

class TreeMap:
    def __init__(self):
        self.root = None
    
    def insert(self, key: int, value: int) -> None:        
        if self.root is None:
            self.root = TreeNode(key, value)
            return
        return self.root.insert(key, value)


    def get(self, key: int) -> int:
        return -1 if self.root is None else self.root.get(key)

    def getMin(self) -> int:
        return -1 if self.root is None else self.root.getMin()


    def getMax(self) -> int:
        return -1 if self.root is None else self.root.getMax()


    def remove(self, key: int) -> None:
        if self.root:
            self.root.remove(key)
            if self.root.key == None:
                self.root = None

    def getInorderKeys(self) -> List[int]:
        return [] if self.root is None else self.root.getInorderKeys()
