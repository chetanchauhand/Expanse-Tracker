file = open("Certificate.txt","r")
data = file.read()
# print("Data of file is: ",data)
data = data.lower()
if "live" in data:
    print(" Yes Live word is present in this file ")
else:
    print("No")