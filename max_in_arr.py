
def max_in_arr(arr, left, right):

    if left == right:

        return arr[left]

    if right == left + 1:

        return arr[left] if arr[left] > arr[right] else arr[right] 

    mid = (left + right) // 2
    
    max_left = max_in_arr(arr, left, mid) 
    max_right = max_in_arr(arr, mid + 1, right)
    
    return max_left if max_left > max_right else max_right 




