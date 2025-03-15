def array_stepper(numbers):
    return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, i, memo):
    # memo dictionary
    if i in memo:
       return memo[i]

    # possible to travel through the array 
    if i >= len(numbers) - 1:
       return True

    max_step = numbers[i]
    for step in range(1, max_step + 1):
        if _array_stepper(numbers, i + step, memo):
            memo[i] = True
            return True

    memo[i] = False 
    return False 