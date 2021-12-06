f=open("demo1.txt","a")
f.write("Learning Python is fun")
f.close()

# open and read file after appending
f=open("demo1.txt","r")
print(f.read())