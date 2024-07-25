def f(n):
    if n<=1:
        return None
    fib = [1,1]
    while True:
        fibon = fib[-1] + fib[-2]
        if fibon>=n:
            break
        fib.append(fibon)

    left = 0
    right = len(fib)-1
    while left < right:
        mid = (left + right) // 2
        if fib[mid]<n:
            left = mid + 1
        else:
            right = mid -1
    return fib[right]

n = int(input("Enter n: "))
print(f"The largest Fibonacci number less than {n} is {f(n)}")