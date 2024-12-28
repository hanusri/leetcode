class DisjointSet:
    def __init__(self, n):
        """Initialize disjoint set with n elements.
        parent[i] < 0 indicates i is a root and |parent[i]| is the size of the tree.
        """
        self.parent = [-1] * n  # Initialize each element as its own set with size 1
    
    def find(self, x):
        """Find the root of the set containing element x.
        Implements path compression for optimization.
        """
        if self.parent[x] < 0:
            return x
        else:
            # Path compression: make all nodes on path point directly to root
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def union(self, x, y):
        """Union the sets containing elements x and y.
        Union is done by size - larger tree becomes the root.
        Returns True if union was performed, False if x and y were already in same set.
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set
        
        # Get sizes (negative of parent values)
        size_x = -self.parent[root_x]
        size_y = -self.parent[root_y]
        
        # Union by size: attach smaller tree to root of larger tree
        if size_x >= size_y:
            # Add size_y to size_x
            self.parent[root_x] -= size_y
            # Make root_x the parent of root_y
            self.parent[root_y] = root_x
        else:
            # Add size_x to size_y
            self.parent[root_y] -= size_x
            # Make root_y the parent of root_x
            self.parent[root_x] = root_y
        
        return True
    
    def get_size(self, x):
        """Get the size of the set containing element x."""
        root = self.find(x)
        return -self.parent[root]
    
    def is_same_set(self, x, y):
        """Check if elements x and y are in the same set."""
        return self.find(x) == self.find(y)
    
    def get_num_sets(self):
        """Get the number of disjoint sets."""
        return sum(1 for p in self.parent if p < 0)

# Test the implementation
def test_disjoint_set():
    ds = DisjointSet(6)  # Create sets for elements 0 through 5
    
    # Test initial state
    print("Initial parent array:", ds.parent)  # Should be all -1
    print("Initial number of sets:", ds.get_num_sets())  # Should be 6
    
    # Test unions
    ds.union(0, 1)  # Union first two elements
    print("After union(0,1):", ds.parent)
    
    ds.union(2, 3)  # Union next two elements
    print("After union(2,3):", ds.parent)
    
    ds.union(0, 2)  # Union the two pairs
    print("After union(0,2):", ds.parent)
    
    # Test find and set size
    print("Root of 3:", ds.find(3))
    print("Size of set containing 3:", ds.get_size(3))
    
    # Test if elements are in same set
    print("Is 0 and 3 in same set?", ds.is_same_set(0, 3))  # Should be True
    print("Is 0 and 4 in same set?", ds.is_same_set(0, 4))  # Should be False
    
    # Test final state
    print("Number of sets:", ds.get_num_sets())

if __name__ == "__main__":
    test_disjoint_set()