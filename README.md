# Analyse function when_to_buy
## Time complexity:
The time complexity of the function mainly correspond to the loops.
Main loop:
The while loop `while i < n - 1:` (potentially) iterates through the entire list once.

Inner loops:
First inner while loop: `while i < n - 1 and prices[i + 1] <= prices[i]`:
Second inner while loop: `while i < n and prices[i] >= prices[i - 1]`:

These inner loops are iterating through the list, but they're not nested. They're sequential.
return tuple(trades) is O(k) where k is the number of trades, but k ≤ n/2 in the worst case.

Therefore, the time complexity of this function is O(n)

## Space Complexity: 
The space complexity is primarily determined by the trades list and the final tuple:

Worst case: If the prices alternate between rising and falling for each element, we would have n/2 trades.
Each trade is a tuple of two integers, so it takes constant space.
Therefore, the trades list would use O(n) space in the worst case.
The final tuple conversion doesn't increase the order of space complexity.

Thus, the overall space complexity of this function is O(n), where n is the length of the input price list.
The space complexity is O(1) if the function return the buy/sell days (For example, if prices are monotonically increasing or decreasing, only one trade would be recorded, resulting in O(1) additional space usage.), or O(n) if we store all identified trades.

# Analyse function risk_strategy

def risk_strategy(low_risk, high_risk):
    n = len(low_risk)
    if n == 0:
        return 0
    if n == 1:
        return max(low_risk[0], high_risk[0])

    # Initialize dp array
    dp = [0] * n

    # Base cases
    dp[0] = max(low_risk[0], high_risk[0])
    dp[1] = max(dp[0], low_risk[1], high_risk[1])

    # Fill dp array
    for i in range(2, n):
        # Option 1: Take low risk this week
        option1 = dp[i-1] + low_risk[i]

        # Option 2: Take high risk this week (only if previous week was not high risk)
        option2 = dp[i-2] + high_risk[i]

        # Option 3: Take zero risk this week
        option3 = dp[i-1]

        dp[i] = max(option1, option2, option3)

    return dp[n-1]

## Time complexity:
The time complexity of this algorithm is `O(n)`, where n is the number of weeks, as we iterate through the weeks once.

## Space Complexity: 
The space complexity is also `O(n)` due to the dp array.