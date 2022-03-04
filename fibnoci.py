num=int(input("Enter the number of terms :"))
n1,n2=0,1
for i in range(0,num):
    if n1==0:
        print(n1)
    elif n2==1:
        print(n2)
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
