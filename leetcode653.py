class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        return self.dfs(root, set(), k)
    
    def dfs(self, root, s, k):
        if not root:
            return False
        if k - root.val in s:
            return True
        s.add(root.val)
        return self.dfs(root.left, s, k) or self.dfs(root.right, s, k)