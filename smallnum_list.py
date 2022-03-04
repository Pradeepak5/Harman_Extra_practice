list=[]
count=int(input("Enter number of lists : "))
for i in range(0,count):
    num=int(input("Enter number :"))
    list.append(num)

print("minimum num :",min(list))
print("maximum num :",max(list))
print(Cloning(list))