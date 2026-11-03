import random 

def qsort(arr):

    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            return arr 

    pivot_idx = random.randint(0, len(arr) - 1) 

    smaller = [] 
    bigger= []

    for num in (arr[:pivot_idx] + arr[pivot_idx + 1:]):

        if num <= arr[pivot_idx]:

            smaller.append(num) 

        else:

            bigger.append(num) 

    merged = qsort(smaller) + [arr[pivot_idx]] + qsort(bigger) 

    return merged 





