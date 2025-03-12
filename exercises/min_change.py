def min_change(amount, coins):
    ans = _min_change(amount, coins)
    if ans == float('inf'):
      return -1
    else:  
      return ans
      
def _min_change(amount, coins, memo = {}):
    # check for memoized value
    if amount in memo:
        return memo[amount]
    
    # minimum amount of coin to make 0c is 0 
    if amount == 0:
        return 0

    # pass in initial min_coins value as +infinity
    min_coins = float("inf")

    # make recursive call for each coin 
    for coin in coins:
        if (amount - coin) >= 0:
            num_coins = 1 + _min_change(amount-coin, coins)          
            min_coins = min(min_coins, num_coins)

    memo[amount] = min_coins    
    return min_coins