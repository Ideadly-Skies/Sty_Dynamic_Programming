def count_paths(grid):
    return _count_paths(grid, 0, 0)

def _count_paths(grid, r, c, memo={}):
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        # don't count path that leads to out of bound 
        return 0

    if (r, c) in memo:
        return memo[(r, c)]

    if r == len(grid)-1 and c == len(grid[0])-1:
        # if i am already in the bottom right corner,
        # there's just one way to reach the bottom
        # right corner 
        return 1

    # return total number of ways going down and right 
    down_count = _count_paths(grid, r+1, c, memo)
    right_count = _count_paths(grid, r, c+1, memo)
    memo[(r, c)] = down_count + right_count    
    return down_count + right_count