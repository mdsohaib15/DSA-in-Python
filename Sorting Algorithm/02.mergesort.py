def mergesort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2 # [1,3,5,2,9,4] (6/2--- mid = 3)
    left = arr[:mid] # 0-(mid-1) or 0-2 
    right = arr[mid:] # 3-last tak
    # left = [1,3,5]
    # right = [2,9,4]
    mergesort(left)
    mergesort(right)
    
    MergeTwosortList(arr, left, right)

def MergeTwosortList(arr, left, right):
    a = len(left)
    b = len(right)
    i = j = k = 0
    
    while i < a and j < b:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < a:
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < b:
        arr[k] = right[j]
        j += 1
        k += 1

arr = [1,3,5,2,9,4] 
print('unsorted array',arr)
mergesort(arr)  # Sorting is done in place
print('sorted array',arr)  # Print the sorted array
