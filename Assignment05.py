# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# Foundation of programming in Python
# Assignment05
# By: Mazyar Kazemi
# Date: 11/04/2019
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"  # Data Storage File
strData = ""  # A row of text data from the file
lstRow = []
lstData = [] #A list of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
# Process the data
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    print(lstRow[0] + ',' + lstRow[1].strip())
objFile.close()

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
# TODO: Add Code Here

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Print and Exit Program
    """)
    strFile = "ToDoList.txt"
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile = open(strFile, "r")
        print(lstTable)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        x = input("Enter a Task: ")
        y = input("Enter priority of this task")
        lstData = [x, y]
        lstTable += [lstData]
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        print(lstTable)
        x = input("Which line you want to delete?")
        y=int(x)
        z=y-1
        del lstTable[z:y]
        print(lstTable)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "a")
        for row in lstTable:
            objFile.write("\n"+ row[0] + ',' + row[1].strip())
        objFile.close()
        print("Data Saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",")
            print(lstRow[0] + '|' + lstRow[1].strip())
        objFile.close()
        print("\n" + "The End")
        break  # and Exit the program
