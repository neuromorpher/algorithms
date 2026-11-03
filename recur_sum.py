def recur_sum(arr):

    if not arr:
        return 0

    return arr[0] + recur_sum(arr[1:])

# 1 + (2+(3+(4+(...)))



