#Binary sort
def binary_search(lst, target):
    lst.sort()
    left = 0
    right = len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2  
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found


l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(binary_search(l, 17)) # Expected is 6
