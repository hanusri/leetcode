def build_bad_character_table(pattern):
    """
    Build an improved bad character table for Boyer-Moore algorithm using the formula:
    length(pattern) - index - 1
    
    This version also includes a wildcard '*' that matches any character not in the pattern
    with a shift of the full pattern length.
    
    Args:
        pattern (str): The pattern to search for
    
    Returns:
        dict: A dictionary mapping characters to their shift values
    """
    # Get pattern length once since we'll use it multiple times
    pattern_length = len(pattern)
    
    # Initialize the bad character table
    bad_char = {}
    
    # Add the wildcard '*' with shift equal to pattern length
    # This handles any character not explicitly in our pattern
    bad_char['*'] = pattern_length
    
    # Calculate shifts for each character in pattern using the formula:
    # pattern_length - index - 1
    for index in range(pattern_length - 1):  # Note: we don't include the last character
        char = pattern[index]
        shift = pattern_length - index - 1
        bad_char[char] = shift
    
    # The last character gets a shift of the pattern length
    # (if it appears earlier in the pattern, its shift was already set)
    if pattern_length > 0:
        last_char = pattern[-1]
        if last_char not in bad_char:
            bad_char[last_char] = pattern_length
            
    return bad_char

def boyer_moore_search(text, pattern):
    """
    Implement Boyer-Moore string search algorithm with improved bad character rule.
    Returns all occurrences of pattern in text.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
        
    Returns:
        list: List of starting positions where pattern occurs in text
    """
    if not pattern or not text:
        return []
    
    # Build the improved bad character table
    bad_char = build_bad_character_table(pattern)
    
    occurrences = []
    pattern_length = len(pattern)
    text_length = len(text)
    
    if pattern_length > text_length:
        return occurrences
    
    # Main search loop
    index = pattern_length - 1  # Start at the end of the pattern
    
    while index < text_length:
        skip = 0
        found = True
        
        # Compare pattern with text from right to left
        for j in range(pattern_length):
            text_char = text[index - j]
            pattern_char = pattern[pattern_length - 1 - j]
            
            if text_char != pattern_char:
                # Character mismatch - look up the shift in bad character table
                found = False
                # Use the shift for the mismatched character, or '*' if not in table
                skip = bad_char.get(text_char, bad_char['*'])
                break
        
        if found:
            # Pattern found - add position to results
            occurrences.append(index - pattern_length + 1)
            # Move one position to find overlapping matches
            skip = 1
        
        index += max(skip, 1)  # Ensure we always move forward
        
    return occurrences