def max_palin_subsequence(string):
    return _max_palin_subsequence(string, 0, len(string)-1, {})

def _max_palin_subsequence(string, i, j, memo):
    # if you have seen this logical substring previously  
    if (i, j) in memo:
        # return memo key
        return memo[(i, j)] 
    
    if i == j:
        return 1
    
    if i > j:
        return 0

    # if the back is equal to the front
    if string[i] == string[j]:
        memo[(i, j)] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
    else:
        memo[(i, j)] = max(
            _max_palin_subsequence(string, i + 1, j, memo),
            _max_palin_subsequence(string, i, j - 1, memo)
        )

    return memo[(i, j)]