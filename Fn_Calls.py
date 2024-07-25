cno = 0

def tf(n):
    global cno
    cno+=1
    if n<=1:
        return 1
    else:
        return tf(n-1) + tf(n-2)

limit = int(input("Enter:"))

tf(limit)

print("\nTotal counts are: " ,cno)