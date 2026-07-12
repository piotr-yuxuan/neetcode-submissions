# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = self._inorder_left(list(), root)


    def _inorder_left(self, stack, current):
        while current:
            stack.append(current)
            current = current.left
        return stack
        

    def next(self) -> int:
        ret = self.stack.pop()
        self._inorder_left(self.stack, ret.right)
        return ret.val
        

    def hasNext(self) -> bool:
        return 0 < len(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()