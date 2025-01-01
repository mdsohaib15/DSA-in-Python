def QuickSort(arr, low, high):
    if low < high:
        pidx = partition(arr, low, high)
        QuickSort(arr, low, pidx - 1)
        QuickSort(arr, pidx + 1, high)

def partition(arr, low, high):
    pivot = arr[high] #pivot = 5 
    i = low - 1 #i=1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1 # i=0(index)
            arr[i], arr[j] = arr[j], arr[i] #swapping
            # 11  , 1      =  1     ,  11
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
# [1, 7, 8, 9, 11, 5]
    #  low            high
arr = [11, 7, 8, 9, 1, 5]
print("Original Array:", arr)
QuickSort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
