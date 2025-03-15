def quickest_concat(s, words):
    """
    return minimum number of word for building the target string.

    Dynamic Programming W/ Memoization:
        s = string length
        n = # of words

    Time: O(n * s)
    Space: O(s) 
    """
    # string is empty 
    if s == "":
        return 0

    # default to large quantity
    min_words = float("inf")
    for word in words:
        if s.startswith(word):
            # chop of front portion
            suffix = s[len(word):]
            attempt = 1 + quickest_concat(suffix, words)
            min_words = min(attempt, min_words)

    # return min_words
    return min_words