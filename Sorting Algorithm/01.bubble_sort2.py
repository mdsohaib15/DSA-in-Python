# bubble sort . second method
def bubblesort(array):
          n = len(array)
          for i in range(n-1):
                    swapped = False
                    for j in range(n-1- i):
                              if array[j] > array[j+1]:
                                        array[j],array[j+1]=array[j+1],array[j]
                    swapped = True
          if (not swapped):
                    return

array = [5,4,3,2,1]
bubblesort(array)
print('sorted array in Ascending order:')
print(array)