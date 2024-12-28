class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        def dfs(node):
            nonlocal result
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            result += abs(left - right)
            return left + right + node.val

        dfs(root)
        return result
    
    # write test cases

# Test cases
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(root.findTilt(root)) # 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(root.findTilt(root)) # 15