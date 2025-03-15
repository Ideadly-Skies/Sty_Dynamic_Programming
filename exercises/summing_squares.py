import math

def summing_squares(n):
    # you would need no perfect squares to add up to 0 
    if n == 0:
       return 0

    # min_squares
    min_squares = float("inf")
    for i in range(1, math.floor(math.sqrt(n))+ 1):
       square = i * i
       num_squares = 1 + summing_squares(n - square)
       min_squares = min(num_squares, min_squares)

    # return min_squares
    return min_squares