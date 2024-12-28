from heapq import heapify, heappush, heappop
from collections import defaultdict

class HuffmanNode:
    """
    A node in the Huffman tree. Each node has:
    - frequency: how often this character/subtree appears
    - char: the character this node represents (None for internal nodes)
    - left and right children
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        # For heap comparison - compare based on frequency
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}
    
    def make_frequency_dict(self, text):
        """Count frequency of each character in the text"""
        frequencies = defaultdict(int)
        for char in text:
            frequencies[char] += 1
        return frequencies
    
    def make_heap(self, frequency_dict):
        """Create a priority queue of HuffmanNodes"""
        for char, freq in frequency_dict.items():
            node = HuffmanNode(char, freq)
            heappush(self.heap, node)
    
    def merge_nodes(self):
        """
        Merge nodes until we have a single tree.
        Always merge the two lowest frequency nodes.
        """
        while len(self.heap) > 1:
            # Get the two nodes with lowest frequencies
            node1 = heappop(self.heap)
            node2 = heappop(self.heap)
            
            # Create new internal node with their combined frequency
            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            
            heappush(self.heap, merged)
    
    def make_codes_helper(self, root, current_code):
        """Recursively generate codes for each character"""
        if root is None:
            return

        # If we reach a leaf node (with a character), save its code
        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_codes[current_code] = root.char
            return

        # Traverse left (add '0') and right (add '1')
        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")
        
    def make_codes(self):
        """Generate Huffman codes for each character"""
        root = heappop(self.heap)
        self.make_codes_helper(root, "")
    
    def encode(self, text):
        """Convert text to Huffman coded binary string"""
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text
    
    def decode(self, encoded_text):
        """Convert Huffman coded binary string back to text"""
        current_code = ""
        decoded_text = ""
        
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_codes:
                char = self.reverse_codes[current_code]
                decoded_text += char
                current_code = ""
                
        return decoded_text
    
    def compress(self, text):
        """Main function to compress text using Huffman coding"""
        # Build frequency dictionary
        freq_dict = self.make_frequency_dict(text)
        
        # Create priority queue of nodes
        self.make_heap(freq_dict)
        
        # Merge nodes to create Huffman tree
        self.merge_nodes()
        
        # Generate codes for each character
        self.make_codes()
        
        # Encode the text
        return self.encode(text)