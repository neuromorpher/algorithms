def count_items(arr):
    if not arr:
        return 0
    return 1 + count_items(arr[1:])
