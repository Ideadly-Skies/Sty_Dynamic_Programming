# non adjacent sum
def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, 0, {})

# i = logical beginning of number you want to consider
def _non_adjacent_sum(nums, i, memo):
    if i in memo:
        return memo[i] 
    
    if i >= len(nums):
        return 0

    # if you take index 0 you should not include index 2 and the rest
    # ([a, b, c, d])j
    # a + ([c, d])
    include = nums[i] + _non_adjacent_sum(nums, i+2, memo)
    exclude = _non_adjacent_sum(nums, i+1, memo)

    memo[i] = max(include, exclude)
    return memo[i] 

if __name__ == "__main__":
    print(non_adjacent_sum([2, 4, 5, 12, 7]))