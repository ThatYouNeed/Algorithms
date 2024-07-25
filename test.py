def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m
m = int(input("Enter: "))
n = int(input("Enter: "))
print(gcd(m,n))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

def verify_fibonacci_gcd(m, n):
    gcd_mn = gcd(m, n)
    Fm = fibonacci(m)
    Fn = fibonacci(n)
    Fgcd_mn = fibonacci(gcd_mn)
    
    return gcd(Fm, Fn) == Fgcd_mn

# Example usage:
m = 8
n = 12
print(verify_fibonacci_gcd(m, n))  # Should print True
