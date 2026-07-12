# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        def inorder(current, l):
            if not current:
                return None
            stack = []

            while current or stack:
                if current:
                    stack.append(current)
                    current = current.left
                else:
                    current = stack.pop()
                    l.append(current.val)
                    current = current.right
            return l
        
        self.order = inorder(root, list())
        self.offset = 0


    def next(self) -> int:
        if not self.hasNext():
            return -1

        ret = self.order[self.offset]
        self.offset += 1
        return ret
        

    def hasNext(self) -> bool:
        return self.offset < len(self.order)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()