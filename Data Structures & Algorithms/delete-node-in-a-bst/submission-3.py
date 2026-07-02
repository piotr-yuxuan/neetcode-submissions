# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def nextInOrderSuccessor(self, root: Optional[TreeNode]):
        if not root:
            return None
        current = root.right
        while current and current.left:
            current = current.left
        return current
        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif successor := self.nextInOrderSuccessor(root):
            right = self.deleteNode(root.right, successor.val)
            successor.left = root.left
            successor.right = right
            return successor
        return root.left