def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
    if amount in memo:
        return memo[amount]

    # catches scenario when the number is negative
    if amount < 0:
        return False
    
    # base case
    if amount == 0:
        return True

    # iterating through numbers array
    for num in numbers:
        if _sum_possible(amount-num, numbers, memo):
            memo[amount] = True
            return True

    # not possible to use any of these number
    # to get the desired amount
    memo[amount] = False 
    return False

# return minimum amount of coins needed
def min_change(amount, coins):
    # Base case
    if not sum_possible(amount, coins):
        return -1

    # Return minimum coins at each node (using memoization)
    memo = {}
    result = _min_change(amount, coins, memo)

    return result if result != float("inf") else -1

def _min_change(amount, coins, memo):
    # Base case - no coins needed for amount 0
    if amount == 0:
        return 0  

    # memoized the result
    if amount in memo:
        return memo[amount]

    # set min coins as inf float
    min_coins = float("inf")

    # Iterating through coins to find the minimum number of coins
    for coin in coins:
        if amount - coin >= 0:
            result = _min_change(amount - coin, coins, memo)
            if result != float("inf"): 
                min_coins = min(min_coins, result + 1)

    # Memoize the result
    memo[amount] = min_coins
    return min_coins

if __name__ == "__main__":
    print(min_change(8, [1, 5, 4, 12])) # -> 2, because 4+4 is the minimum coins possible)
    print(min_change(2017, [4, 2, 10])) # -> -1)