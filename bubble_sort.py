def bubble_sort(arr):
    for i in range(len(arr)-1, 0 , -1):
        for j in range(i):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


arr = [45,59,12,3,65,41,62,47,85,21,73,82,96,12,8,57,39]

print(bubble_sort(arr))