class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        min_val = root.val
        while root:
            if abs(root.val - target) < abs(min_val - target):
                min_val = root.val
            elif abs(root.val - target) == abs(min_val - target):
                min_val = root.val if root.val < min_val else min_val
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return min_val
        
