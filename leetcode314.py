# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columnTable = {}
        q = Queue()
        q.put((root, 0))  # node, column
        minColumnValue = maxColumnValue = 0

        while not q.empty():
            node, column = q.get()

            if node:
                if column not in columnTable:
                    columnTable[column] = []
                columnTable[column].append(node.val)

                minColumnValue = min(minColumnValue, column)
                maxColumnValue = max(maxColumnValue, column)

                # Enqueue left and right children
                q.put((node.left, column - 1))
                q.put((node.right, column + 1))

        # Construct result using minColumnValue and maxColumnValue
        return [columnTable[col] for col in range(minColumnValue, maxColumnValue + 1) if col in columnTable]