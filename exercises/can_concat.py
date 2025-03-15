def can_concat(s, words):
  return _can_concat(s, words, 0, {})

def _can_concat(s, words, i, memo):
    if i in memo:
        return memo[i]
    
    if i == len(s):
        return True

    for word in words:
        # do word begins at the front of s
        if s.startswith(word, i):
            if _can_concat(s, words, i + len(word), memo):
                memo[i] = True
                return True

    memo[i] = False
    return False