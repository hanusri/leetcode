from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return 'None'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        index = 0
        def helper(values: List[str]) -> Optional[TreeNode]:
            nonlocal index
            if values[index] == 'None':
                index += 1
                return None
            root = TreeNode(int(values[index]))
            index += 1
            root.left = helper(values)
            root.right = helper(values)
            return root
        return helper(data.split(','))