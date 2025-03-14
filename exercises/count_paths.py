def count_paths(grid):
    ans = _count_paths(grid, 0, 0)
    return ans

def _count_paths(grid, r, c, memo={}):
    # return memo in dictionary
    if (r, c) in memo:
        return memo[(r, c)]

    # handle the case when you step out of bounds
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        return 0 # don't want to count any paths that lead out of bounds

    # base case
    if r == len(grid)-1 and c == len(grid[0])-1:
        return 1 # count this as 1

    # recursive case
    down_count = _count_paths(grid, r+1, c, memo)
    right_count = _count_paths(grid, r, c+1, memo)

    # place computation in memo
    memo[(r, c)] = down_count + right_count
    return memo[(r, c)] 

if __name__ == "__main__":
    grid = [
        ["O", "O"],
        ["O", "O"]
    ] 

    grid = [
        ["O", "O", "X"],
        ["O", "O", "O"],
        ["O", "O", "O"],
    ] 

    print(count_paths(grid))