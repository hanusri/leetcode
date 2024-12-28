from typing import Optional,Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_size = float('-inf')

        def dfs(self, root: Optional[TreeNode]) -> Tuple[bool, int]:
            if not root:
                return (True, 0)
            
            if not root.left and not root.right:
                return (True, 1)
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] and right[0]:
                if root.left and root.val > root.left and root.right and root.right > root.val:
                    self.max_size = max(self.max_size, left[1] + right[1] + 1)
                    return (True, left[1] + right[1] + 1)
                
            elif left[0]:
            
            elif right[0]:
            
            else:
