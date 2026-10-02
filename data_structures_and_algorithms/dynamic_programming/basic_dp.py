# Compute nth number where each step adds 5
# 10, 15, 20, 25...

def dpBasic(n):
    # Step 1: Array creation with 0s
    dp = [0] * (n + 1)

    # Step 2: Base declaration
    dp[0] = 10

    # Step 3: Main portion
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 5

    return dp[n]


print("Result for n = 5:", dpBasic(5))