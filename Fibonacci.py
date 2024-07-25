def tf(n):
    if n<=1:
        return 1
    else:
        return tf(n-1) + tf(n-2)

limit = int(input("Enter:"))

for i in range(limit):
    print(tf(i), end=" ")
    