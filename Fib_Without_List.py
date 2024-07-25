def largest_fib_less_than_n(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

n = int(input('Enter No: '))
result = largest_fib_less_than_n(n)
print(f"The largest Fibonacci number less than {n} is {result}")
