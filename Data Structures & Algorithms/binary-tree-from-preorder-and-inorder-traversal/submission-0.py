# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        val = preorder[0]
        midpoint = inorder.index(val)

        return TreeNode(
            val,
            self.buildTree(
                preorder[1 : 1 + midpoint],
                inorder[:midpoint],
            ),
            self.buildTree(
                preorder[1 + midpoint :],
                inorder[midpoint+1:],
            ),
        )
