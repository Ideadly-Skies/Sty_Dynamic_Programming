def tribonacci(n, memo={}):
    if (n == 0 or n == 1):
        return 0
    elif (n == 2):
        return 1 
    else:
        if n not in memo:
            memo[n] = tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)
        return memo[n]  

if __name__ == "__main__":
    print(tribonacci(0)) # -> 0
    print(tribonacci(1)) # -> 0
    print(tribonacci(2)) # -> 1
    print(tribonacci(5)) # -> 4
    print(tribonacci(7)) # -> 13)