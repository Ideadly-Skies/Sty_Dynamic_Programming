def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
    if amount in memo:
        return memo[amount]

    # catches scenario when the number is negativ 
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