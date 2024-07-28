# def largest_fib_less_than_n(fib_list, n):
#     for fib in reversed(fib_list):
#         if fib < n:
#             return fib
#     return None

# fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
# n = int(input('Enter No: '))
# result = largest_fib_less_than_n(fib_list, n)
# print(f"The largest Fibonacci number less than {n} is {result}")

def fibwith(list,n):
    left = 0
    right = len(list)-1

    while left <= right:
        mid = (left+right)//2
        if list[mid] < n:
            left = mid + 1
        elif list[mid] > n:
            right = mid - 1
        else:
            return list[mid-1] if mid>0 else None
    return list[right] if right >=0 else None

list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
n = int(input('Enter Number: '))
result = fibwith(list, n)
print(f"The largest Fibonacci number less than {n} is {result}")
