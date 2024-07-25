def fib(n):
    if n<=1:
        return None
    fibo=[1,1]
    while True:
        fibon = fibo[-1] + fibo[-2]
        if fibon>=n:
            break
        fibo.append(fibon)

    left=0
    right=len(fibo)-1
    while left<right:
        mid = (left+right)//2
        if fibo[mid]<n:
            left=mid+1
        else:
            right=mid-1
    return fibo[right]

n = int(input("Enter: "))
print(f"The largest Fibonacci number less than {n} is {fib(n)}")