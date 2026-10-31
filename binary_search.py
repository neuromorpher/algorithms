def binary_search(arr:list[int], target: int) -> int | None:

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2
        guess = arr[mid] 

        if guess == target: 

            return mid  

        if guess < target: 

            low = mid + 1 
        else:

            high = mid - 1

    return None  


print(binary_search([1,3,5,7,9], 7)) 
print(binary_search([1,3,5,7,9], 10)) 
