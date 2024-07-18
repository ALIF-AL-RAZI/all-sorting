def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i, j, k = 0,0,0

        while i<len(left_arr) and j< len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k] = left_arr[i]
                i+=1

            else:
                arr[k] = right_arr[j]
                j+=1

            k+=1

        while i< len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1

        while j< len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1

    return arr





arr = [45,59,12,3,65,41,62,47,85,21,73,82,96,12,8,57,39]

print(merge_sort(arr))