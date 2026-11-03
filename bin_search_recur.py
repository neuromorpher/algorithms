
def bin_search_recur(arr, target, l, r):

    if l > r:

        return -1 

    mid = (l+r)//2

    if arr[mid] == target:

        return mid 

    elif arr[mid] > target:

        return bin_search_recur(arr, target , l, mid-1)
    else: 
        return bin_search_recur(arr, target, mid + 1, r)





    

