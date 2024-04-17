class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: Node) -> int:
        diameter = 0
        def height(node):
            nonlocal diameter
            if not node:
                return -1
            
            if len(node.children) == 0:
                return 0
            
            max_height1, max_height2 = 0, 0
            for child in node.children:
                parent_height = height(child) + 1
                if parent_height > max_height1:
                    max_height1, max_height2 = parent_height, max_height1
                elif parent_height > max_height2:
                    max_height2 = parent_height
            diameter = max(diameter, max_height1 + max_height2)
            return max_height1
        
        height(root)
        return diameter