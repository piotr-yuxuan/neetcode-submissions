# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        val = postorder[-1]
        midpoint = inorder.index(val)

        return TreeNode(
            val,
            self.buildTree(
                inorder[:midpoint],
                postorder[:midpoint],
            ),
            self.buildTree(
                inorder[midpoint + 1 :],
                postorder[midpoint : len(postorder) - 1],
            ),
        )
