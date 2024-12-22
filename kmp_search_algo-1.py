def compute_lps(pattern):
    """
    Computes the Longest Prefix Suffix (LPS) array for the given pattern.
    """
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    return lps

def kmp_search(text, pattern):
    """
    Finds all occurrences of the pattern in the given text using KMP algorithm.
    """
    lps = compute_lps(pattern)
    j = 0  # index for pattern
    matches = []
    
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == len(pattern):
            matches.append(i - j + 1)
            j = lps[j - 1]
    
    return matches

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = kmp_search(text, pattern)
print("Pattern found at indices:", matches)
