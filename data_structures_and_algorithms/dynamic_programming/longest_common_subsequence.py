def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    # Step 1: Create 2D array initialized with 0s
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Step 2: Fill the DP table
    for row in range(1, len1 + 1):
        for col in range(1, len2 + 1):
            char1 = str1[row - 1]
            char2 = str2[col - 1]

            if char1 == char2:
                dp[row][col] = 1 + dp[row - 1][col - 1]
            else:
                dp[row][col] = max(
                    dp[row - 1][col],  # Exclude character from str1
                    dp[row][col - 1]   # Exclude character from str2
                )

    return dp[len1][len2]

string1 = "stone"
string2 = "longest"

print("LCS length:", lcs(string1, string2))  # Output: LCS length: 3 ("one")