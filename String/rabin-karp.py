def pattern_matching(text, pattern):
    prime = 101
    mod = 1000000007  # Large prime for modulo operations
    
    m = len(pattern)
    n = len(text)
    
    if m > n:
        return -1
        
    pattern_hash = create_hash(pattern, m)
    text_hash = create_hash(text[:m], m)
    
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if check_equal(text[i:i+m], pattern):
                return i
        if i < n - m:    
            text_hash = recalculate_hash(text, i, i+m, text_hash, m, prime, mod)
    return -1

def check_equal(str1, str2):
    # First check if lengths are different
    if len(str1) != len(str2):
        return False
    
    # Compare characters one by one
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True
    
def create_hash(input_str, length):
    prime = 101
    mod = 1000000007
    hash_val = 0
    
    for i in range(length):
        hash_val = (hash_val + ord(input_str[i]) * pow(prime, i, mod)) % mod
    return hash_val

def recalculate_hash(input_str, old_index, new_index, old_hash, pattern_len, prime, mod):
    # Remove leftmost character
    old_hash = (old_hash - ord(input_str[old_index])) % mod
    
    # Divide by prime
    old_hash = (old_hash * pow(prime, mod-2, mod)) % mod  # Using Fermat's little theorem for division
    
    # Add new character
    new_hash = (old_hash + ord(input_str[new_index]) * pow(prime, pattern_len-1, mod)) % mod
    
    return new_hash