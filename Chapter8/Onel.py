# Read one line of bio.txt
# with open("bio.txt","r") as f:
#     line1 = f.readline()
#     print("Line 1: ",line1)

# How many list of lines
with open("bio.txt","r") as f:
    listOfLine = f.readline()
   # print("Output of readlines function: ",listOfLine)
    print("Number of line in list: ", len(listOfLine))