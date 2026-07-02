# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def myInsertNode(self, root: Optional[TreeNode], child: TreeNode):
        if not child:
            return root

        if not root:
            return child
        
        if root.val < child.val:
            root.right = self.myInsertNode(root.right, child)
        elif child.val < root.val:
            root.left = self.myInsertNode(root.left, child)
        
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            root.left = self.myInsertNode(root.left, root.right)
            return root.left