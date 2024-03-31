from tree_node import TreeNode
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)
    
    def preOrder(self, root):
        if root:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)
    
    def contains(self, root, data):
        if not root:
            return False
        
        if root.data > data:
            return self.contains(root.left, data)
        elif root.data < data:
            return self.contains(root.right, data)
        else:
            return True
    
    def insert(self, root, data):
        if not root:
            return TreeNode(data)
        
        if root.data > data:
            root.left = self.insert(root.left, data)
        elif root.data < data:
            root.right = self.insert(root.right, data)
        else:
            return root
        
        return root
    
    def delete(self, root, data):
        if not root:
            return root
        
        if root.data > data:
            root.left = self.delete(root.left, data)
        elif root.data < data:
            root.right = self.delete(root.right, data)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                root.data = self.minValue(root.right)
                root.right = self.delete(root.right, root.data)
        
        return root
    
    def minValue(self, root):
        current = root
        while current.left:
            current = current.left
        return current.data
    
# Test the binary search tree
bst = BinarySearchTree()
root = None
root = bst.insert(root, 50)
root = bst.insert(root, 30)
root = bst.insert(root, 20)
root = bst.insert(root, 40)
root = bst.insert(root, 70)
root = bst.insert(root, 60)
root = bst.insert(root, 80)
print("Inorder traversal of the given tree")
bst.inOrder(root)
print("\nDelete 20")
root = bst.delete(root, 20)
print("Inorder traversal of the modified tree")
bst.inOrder(root)
print("\nDelete 30")
root = bst.delete(root, 30)
print("Inorder traversal of the modified tree")
bst.inOrder(root)
