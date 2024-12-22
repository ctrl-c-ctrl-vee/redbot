def rabin_karp(text, pattern):
    if len(pattern) == 0 or len(text) == 0:
        return []

    # Define a large prime number for modulo operation to avoid overflow
    prime = 101
    current_hash = 0
    pattern_hash = 0
    h = 1  # The value of h would be "37^len(pattern)" mod prime, but we can precompute it

    # Precompute h = 37^(m-1) % q
    for i in range(len(pattern)-1):
        h = (h * 37) % prime

    # Calculate the hash value of pattern and first window of text
    for i in range(len(pattern)):
        current_hash = (37 * current_hash + ord(text[i])) % prime
        pattern_hash = (37 * pattern_hash + ord(pattern[i])) % prime

    # Slide the pattern over text one by one
    result = []
    for i in range(len(text) - len(pattern) + 1):
        if current_hash == pattern_hash:
            # Check for characters one by one
            if text[i:i+len(pattern)] == pattern:
                result.append(i)

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < len(text) - len(pattern):
            current_hash = (37 * (current_hash - ord(text[i]) * h) + ord(text[i + len(pattern)])) % prime

    return result

# Example usage:
text = "ABABDABACDABABCABAD"
pattern = "ABABCABAD"
print(rabin_karp(text, pattern))
