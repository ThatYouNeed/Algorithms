def lfm(arr,target):
    left = 0
    right = len(arr)-1
    result=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            result = mid
            right = mid - 1
        elif arr[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return result

arr = [1,2,3,4,4,4,5,6,7,7,7,8,9,0,0,0,1,3,3,]
target = 3
index = lfm(arr,target)
print(f"The target {target} is in the index {index}")