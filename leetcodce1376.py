from typing import List, Dict
class TreeNode:
    def __init__(self, employee_id: int, inform_time: int):
        self.employee_id = employee_id
        self.inform_time = inform_time
        self.subordinates: List[TreeNode] = []

def build_tree(n: int, headID: int, manager: List[int], informTime: List[int]) -> TreeNode:
    nodes: Dict[int, TreeNode] = {}
    
    # Create TreeNode for each employee
    for i in range(n):
        nodes[i] = TreeNode(i, informTime[i])
    
    # Build the tree structure
    for i in range(n):
        if i != headID:
            parent = nodes[manager[i]]
            parent.subordinates.append(nodes[i])
    
    return nodes[headID]

def calculate_inform_time(root: TreeNode) -> int:
    if not root.subordinates:
        return 0
    
    max_subordinate_time = max(calculate_inform_time(subordinate) for subordinate in root.subordinates)
    return root.inform_time + max_subordinate_time

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        company_tree = build_tree(n, headID, manager, informTime)
        return calculate_inform_time(company_tree)