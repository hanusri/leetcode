# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Create a hash map to store the indices of elements in postorder
        postorder_index = {val: i for i, val in enumerate(postorder)}
        
        def helper(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            
            root = TreeNode(preorder[pre_start])
            
            if pre_start == pre_end:
                return root
            
            # Find the index of the left subtree's root in postorder
            left_subtree_root_index = postorder_index[preorder[pre_start + 1]]
            left_subtree_size = left_subtree_root_index - post_start + 1
            
            # Recursively construct left and right subtrees
            root.left = helper(pre_start + 1, pre_start + left_subtree_size, 
                               post_start, left_subtree_root_index)
            root.right = helper(pre_start + left_subtree_size + 1, pre_end, 
                                left_subtree_root_index + 1, post_end - 1)
            
            return root
        
        return helper(0, len(preorder) - 1, 0, len(postorder) - 1)