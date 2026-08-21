# Write file
# file = open("report.txt","w")
# file.write("Everything in this fie.happy")

# Add file("x")
# file = open("report2.txt","x")
# file.write("run = 34, Target = 110 ")

# With Keyboard
file = open("reports.txt","r")
data = file.read()
print("Data is ",data)

with open("reports.txt","r") as f:
 data = f.read()
 print("hello Data: ",data)
