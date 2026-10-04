def knapsack(weights, values, capacity):
    items = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(items + 1)]

    for i in range(1, items + 1):
        for current in range(1, capacity + 1):
            if weights[i - 1] <= current:
                dp[i][current] = max(
                    values[i - 1] + dp[i - 1][current - weights[i - 1]],
                    dp[i - 1][current]
                )
            else:
                dp[i][current] = dp[i - 1][current]

    return dp[items][capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Maximum value:", knapsack(weights, values, capacity))