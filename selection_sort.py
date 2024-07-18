def select_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i, len(arr)):
            if arr[j]< arr[min]:
                min = j
            
        arr[i], arr[min] = arr[min], arr[i]
        
    print(arr)


arr = [45,59,12,3,65,41,62,47,85,21,73,82,96,12,8,57,39]
(select_sort(arr))