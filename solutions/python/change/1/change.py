def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    if not coins:
        raise ValueError("no coins provided")

    # dp[x] = list các đồng xu ít nhất để tạo ra x
    dp = [None] * (target + 1)
    dp[0] = []

    for amount in range(1, target + 1):
        best = None
        for c in coins:
            if amount - c >= 0 and dp[amount - c] is not None:
                candidate = dp[amount - c] + [c]
                if best is None or len(candidate) < len(best):
                    best = candidate
        dp[amount] = best

    if dp[target] is None:
        raise ValueError("can't make target with given coins")
    dp[target].reverse()

    return dp[target]
                                                                                                                                                                                 
