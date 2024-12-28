from typing import List, Optional
from Trees.tree_node import TreeNode
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def collectAndRemoveLeaves(root: Optional[TreeNode], subResult: List[int]) -> TreeNode:
            if root is None:
                return None
            
            if root.left is None and root.right is None:
                subResult.append(root.val)
                return None
            
            root.left = collectAndRemoveLeaves(root.left, subResult)
            root.right = collectAndRemoveLeaves(root.right, subResult)

            return root
        
        while root is not None: 
            subResult = []
            root = collectAndRemoveLeaves(root, subResult)
            if subResult:
                result.append(subResult)
        
        return result