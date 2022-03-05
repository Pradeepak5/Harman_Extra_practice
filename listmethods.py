list=[]
countvar=int(input("Enter the count : "))
for i in range(0,countvar):
    a=input("enter word : ")
    list.append(a)

print(list)

print(list.count("pradeep"))
list_1=["benz","volvo","audi"]
list.extend(list_1)
print(list)
list.insert(3,"maruthi")
print(list)
b=int(input("select index to remove data : "))
list.pop(b)
print(list)
list.sort()
print(list)
list.reverse()
print(list)
