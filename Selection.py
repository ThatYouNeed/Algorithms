def selection(arr):
    for i in range(len(arr)):
        small = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[small]:
                small = j

        temp = arr[i]
        arr[i] = arr[small]
        arr[small] = temp

arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
selection(arr)
print("Sorted array:", arr)