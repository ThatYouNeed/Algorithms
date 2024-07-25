def gfun(m,n):
    if m ==0:
        return n
    elif n ==0:
        return m
    else:
        return gfun(abs(m-n),min(m,n))

m = int(input("Enter: "))
n = int(input("Enter Again: "))
print("The anaswer is: ",gfun(m,n))