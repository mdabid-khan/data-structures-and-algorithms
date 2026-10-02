# ============================================================
# 0/1 Knapsack using Dynamic Programming
# ============================================================


# Function to solve the 0/1 Knapsack problem
def dpknap(weights, profits, capacity):

    # Number of items
    n = len(profits)

    # Create a DP table
    # Rows    = items
    # Columns = bag capacities
    #
    # Initially, all values are 0
    dp = [
        [0 for _ in range(capacity + 1)]
        for _ in range(n + 1)
    ]

    # Go through each item
    for i in range(1, n + 1):

        # Try every possible bag capacity
        for w in range(1, capacity + 1):

            # Check if the current item's weight
            # can fit inside the current capacity
            if weights[i - 1] <= w:

                # Two choices:
                #
                # 1. Do not take the current item
                #    dp[i - 1][w]
                #
                # 2. Take the current item
                #    dp[i - 1][w - weight] + profit
                #
                # Choose the option with greater profit
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]]
                    + profits[i - 1]
                )

            else:
                # If the item does not fit,
                # keep the previous maximum profit
                dp[i][w] = dp[i - 1][w]

    # Return the maximum profit
    # using all items and the given capacity
    return dp[n][capacity]


# ------------------------------------------------------------
# Item weights
# ------------------------------------------------------------

item_weights = [2, 3, 4, 5]


# ------------------------------------------------------------
# Item profits
# ------------------------------------------------------------

item_profits = [3, 4, 5, 6]


# ------------------------------------------------------------
# Maximum capacity of the bag
# ------------------------------------------------------------

bag_capacity = 8


# ------------------------------------------------------------
# Call the function
# ------------------------------------------------------------

max_profit = dpknap(
    item_weights,
    item_profits,
    bag_capacity
)


# ------------------------------------------------------------
# Display the result
# ------------------------------------------------------------

print(f"Maximum Profit: {max_profit}")