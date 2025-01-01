def mergesort(arr):
    if len(arr) <=1:
        return
    mid = len(arr) //2
    left=arr[:mid]
    right=arr[mid:]
    mergesort(left)
    mergesort(right)
    MergeTwoSortList(arr,left,right)

def MergeTwoSortList(arr,left,right):
    a = len(left)
    b = len(right)
    i=j=k=0
    while i<a and j<b:
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1

    while i<a:
        arr[k]=left[i]
        i+=1
        k+=1
    while j<b:
        arr[k]=right[j]
        j+=1
        k+=1

array=[2,6,1,7,3,9]
print('unsorted',array)
mergesort(array)
print('sorted',array)