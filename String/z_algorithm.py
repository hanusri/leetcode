def construct_z_array(string):
    """
    Constructs the Z Array for a given string.
    The Z Array stores the length of the longest substring starting at each position
    that matches a prefix of the string.
    
    Args:
        string (str): Input string to analyze
    Returns:
        list: Z Array where Z[i] is the length of the longest substring starting 
             at position i that matches a prefix of the string
    """
    n = len(string)
    z = [0] * n
    z[0] = n  # First position matches entire string
    
    # Initialize left and right boundaries of Z-box
    left = right = 0
    
    # Process remaining positions
    for i in range(1, n):
        if i > right:
            # Position i is outside the current Z-box
            # Compute Z[i] by comparing characters explicitly
            left = right = i
            while right < n and string[right] == string[right - left]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            # Position i is inside the current Z-box
            k = i - left
            
            # If Z[k] is less than remaining Z-box length,
            # we can directly copy the value
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                # Otherwise, we need to match characters beyond right
                left = i
                while right < n and string[right] == string[right - left]:
                    right += 1
                z[i] = right - left
                right -= 1
    
    return z

def z_algorithm_search(text, pattern):
    """
    Uses Z Algorithm to find all occurrences of pattern in text.
    
    Args:
        text (str): The main text to search within
        pattern (str): The pattern to search for
    Returns:
        list: List of starting indices where pattern is found
    """
    # Create concatenated string with a special character
    # that won't appear in pattern or text
    concat = pattern + "$" + text
    n = len(concat)
    
    # Construct Z Array for concatenated string
    z = construct_z_array(concat)
    
    # Find pattern matches
    pattern_length = len(pattern)
    matches = []
    
    # Check Z values that correspond to text positions
    # Pattern match occurs when Z value equals pattern length
    for i in range(pattern_length + 1, n):
        if z[i] == pattern_length:
            # Subtract pattern length and 1 (for $) to get original text position
            matches.append(i - pattern_length - 1)
    
    return matches