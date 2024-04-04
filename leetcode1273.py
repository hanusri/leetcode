from typing import List
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        children = defaultdict(list)
        for i in range(nodes):
            if parent[i] != -1:
                children[parent[i]].append(i)

        def dfs(node):
            total = value[node]
            count = 1  # count the node itself
            for child in children[node]:
                child_total, child_count = dfs(child)
                if child_total != 0:  # only add the child count if its total is not zero
                    total += child_total
                    count += child_count
            if total == 0:
                return 0, 0
            else:
                return total, count

        return dfs(0)[1]