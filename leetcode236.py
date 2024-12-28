from collections import defaultdict
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # create dictionary of parent using stack iteration
        tree_iteration_stack = [root]
        parents_dictionary = defaultdict(TreeNode)
        while p not in parents_dictionary or q not in parents_dictionary:
            node = tree_iteration_stack.pop()
            if node.left:
                parents_dictionary[node.left] = node
                tree_iteration_stack.append(node.left)
            if node.right:
                parents_dictionary[node.right] = node
                tree_iteration_stack.append(node.right)
        # construct ancestors using p
        ancestors  = set()
        while p:
            ancestors.add(p)
            p = parents_dictionary[p]

        # iterate over q parents and find first ancestor
        while q not in ancestors:
            q = parents_dictionary[q]
        
        return q