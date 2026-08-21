# Expense Tracker Project

expenses = [] # list of expenses in form of dictionary
print("Welcome to Expense Tracker : Kharcha kam kiya karo ")
while True:
    print("====WELCOME====")
    print("1. Add Expense ")
    print("2. View all Expense ")
    print("3. View total Expense ")
    print("4. Exit ")

    choice = int(input("Please enter your choice: "))

# Add Expense
    if(choice==1):
        date = input("Enter the date when you spent money? ")
        category = input("Which type of expense? (Food , Travel , Makup , Books): ")
        description = input("Give me details: ")
        amount = float(input("Enter the Amount: "))
        
# Add dictionary
        expense={
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }
        expenses.append(expense)
        print("/n Done. Expense is added succesfully ")

# View all expense
if(choice == 2):
    if(len(expense == 0)):
        print("No Expense added.Go and spent money")
    else:
        print("==== Your total expense ====")
        count == 1
        for eachexpense in expenses:
            print(f"Expense Number{count} -> {eachExpense["Date"]},{eachExpense["category"]},{eachExpense["description"]},{eachExpense["Amount"]}")
# View Total Spending

elif(choice == 3):
    total = 0
    for eachexpense in expenselist:
        total = total + eachexpense["amount"]
        print("/n Total Expense = ",total)
# Exit
elif(choice == 4):
    print("Thankyou you have used my system")
    Break
else:
    print("INVELID CHOICE. TRY AGAIN ")