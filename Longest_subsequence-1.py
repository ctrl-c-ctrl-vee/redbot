def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create a 2D array to store lengths of longest common subsequence
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the LCS table in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Following code is used to print LCS
    index = L[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is", lcs(X, Y))
