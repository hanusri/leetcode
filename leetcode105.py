from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder_start: int, preorder_end: int, inorder_start: int, inorder_end: int):
            if preorder_start > preorder_end or inorder_start > inorder_end:
                return None

            root_value = preorder[preorder_start]
            root = TreeNode(root_value)
            root_index = inorder.index(root_value)

            # Compute the number of elements in the left subtree
            left_subtree_size = root_index - inorder_start

            root.left = helper(preorder_start + 1, preorder_start + left_subtree_size, inorder_start, root_index - 1)
            root.right = helper(preorder_start + left_subtree_size + 1, preorder_end, root_index + 1, inorder_end)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)