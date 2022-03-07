file=open("filesample.txt","w")
data=file.write("Hi I am Pradeep Kumar.......")

file=open("filesample.txt","a")
data=file.write("I was born and raised in Erode.")

file=open("filesample.txt","r")
data=file.read()
print(data)