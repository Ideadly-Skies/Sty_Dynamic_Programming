# fibonnaci recursive
def fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    else:
        if n not in memo:
            # compute the memoized result
            memo[n] = fib(n-1) + fib(n-2)

        # return the memoized result 
        return memo[n]

if __name__ == "__main__":
    print(fib(0)) # -> 0
    print(fib(1)) # -> 1
    print(fib(2)) # -> 1
    print(fib(3)) # -> 2
    print(fib(4)) # -> 3
    print(fib(46)); # -> 1836311903