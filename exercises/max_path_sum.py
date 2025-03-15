def max_path_sum(grid):
    # memo to store computed result 
    memo = {} 

    return _max_path_sum(grid, 0, 0, memo)

def _max_path_sum(grid, r, c, memo):
    # return value of memo in pos 
    if (r, c) in memo:
        return memo[(r, c)]

    # check if entry is out of bounds
    if r == len(grid) or c == len(grid[0]):
        return float("-inf")

    # base case 
    if r == len(grid)-1 and c == len(grid[0])-1:
        return grid[r][c] 
        
    # recursive case
    left_sum = _max_path_sum(grid, r+1, c, memo)
    right_sum = _max_path_sum(grid, r, c+1, memo) 

    # return max from left_sum and right_sum
    memo[(r, c)] = grid[r][c] + max(left_sum, right_sum)
    return memo[(r, c)]

if __name__ == "__main__":
    grid = [
        [1, 3, 12],
        [5, 1, 1],
        [3, 6, 1],
    ]
    
    print(max_path_sum(grid)) # -> 18

    grid = [
        [1, 2, 8,  1],
        [3, 1, 12, 10],
        [4, 0, 6,  3],
    ]
max_path_sum(grid) # -> 36