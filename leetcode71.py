class Solution:
    def simplifyPath(self, path: str) -> str:
            # Split the path into components
        components = path.split('/')
        
        # Initialize a stack to keep track of directories
        stack = []
        
        for component in components:
            # Ignore empty components and current directory
            if component == '' or component == '.':
                continue
            
            # Go up one level for parent directory
            elif component == '..':
                if stack:
                    stack.pop()
            
            # Add valid directory or file name to stack
            else:
                stack.append(component)
        
        # Construct the canonical path
        if stack:
            return '/'
        else:
            return '/'.join(stack)
