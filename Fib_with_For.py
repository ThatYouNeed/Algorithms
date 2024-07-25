n = int(input('Enter: '))

n1,n2 = 0,1

if n==0:
    print("Chusko Bro!")
if n>=1:
    print(n1,end = " ")
if n>=2:
    print(n2,end = " ")

for i in range(2,n):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3,end=" ")
    