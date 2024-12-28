def compute_lps_array(pattern):
    """
    Computes the Longest Proper Prefix which is also Suffix (LPS) array.
    This is the preprocessing phase of KMP algorithm.
    
    Args:
        pattern (str): The pattern to analyze
    Returns:
        list: LPS array where lps[i] is the length of the longest proper 
             prefix that is also a suffix for pattern[0...i]
    """
    length = len(pattern)
    lps = [0] * length  # Initialize LPS array with zeros
    
    # Length of previous longest prefix & suffix
    prev_lps = 0
    
    # Start from second character (index 1)
    i = 1
    
    while i < length:
        if pattern[i] == pattern[prev_lps]:
            # We found a matching character, extend the prefix
            prev_lps += 1
            lps[i] = prev_lps
            i += 1
        else:
            if prev_lps != 0:
                # Try matching with shorter prefix
                prev_lps = lps[prev_lps - 1]
            else:
                # No prefix found, move to next character
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Implements the Knuth-Morris-Pratt string matching algorithm.
    
    Args:
        text (str): The main text to search within
        pattern (str): The pattern to search for
    Returns:
        list: List of starting indices where pattern is found
    """
    if not pattern or not text:
        return []
        
    # Get lengths and initialize variables
    M = len(pattern)
    N = len(text)
    positions = []
    
    # Compute the LPS array for pattern
    lps = compute_lps_array(pattern)
    
    # Initialize indices for text and pattern
    i = 0  # Index for text
    j = 0  # Index for pattern
    
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        # If we've matched the entire pattern
        if j == M:
            positions.append(i - j)  # Found a match
            j = lps[j - 1]  # Look for next match
        
        # Handle mismatch after j matches
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]  # Use LPS to skip redundant comparisons
            else:
                i += 1
    
    return positions