# Fibonacci series using Dynamic Programming
# F(n) = F(n-1) + F(n-2)

def fibDP(n):
    # Base case
    if n == 0:
        return 0

    if n == 1:
        return 1

    # Step 1: Array creation with 0s
    dp = [0] * (n + 1)

    # Step 2: Base values
    dp[0] = 0
    dp[1] = 1

    # Step 3: Main portion
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print("nth term of fibonacci series:", fibDP(10))