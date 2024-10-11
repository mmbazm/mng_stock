def when_to_buy(prices):
    """ this version leverages dynamic programming to improve time complexity.
    """
    n = len(prices)
    trades = []
    i = 0

    while i < n - 1:
        # Find local minimum
        while i < n - 1 and prices[i + 1] <= prices[i]:
            i += 1
        if i == n - 1:
            break
        buy = i
        i += 1

        # Find local maximum
        while i < n and prices[i] >= prices[i - 1]:
            i += 1
        sell = i - 1

        trades.append((buy + 1, sell + 1))

    return tuple(trades)


def risk_strategy(low_risk, high_risk):
    n = len(low_risk)
    if n == 0:
        return 0
    if n == 1:
        return max(low_risk[0], high_risk[0])

    # Initialize an array for dynamic programming
    data_arr = [0] * n

    data_arr[0] = max(low_risk[0], high_risk[0])
    data_arr[1] = max(data_arr[0], low_risk[1], high_risk[1])

    # Fill data_arr array
    for i in range(2, n):
        # low risk this week
        option1 = data_arr[i-1] + low_risk[i]

        # high risk this week (i.e., only if previous week was not high risk)
        option2 = data_arr[i-2] + high_risk[i]

        # zero risk this week
        option3 = data_arr[i-1]

        # Finally take the max of them
        data_arr[i] = max(option1, option2, option3)

    return data_arr[n-1]
