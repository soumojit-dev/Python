stack = []  #EMPTY LIST FOR STACK

def display_stack():  
    if(len(stack)==0):   #CHECKS IF THE STACK IS EMPTY
        print("Underflow Condition")
    else:
        print("Stack (top -> bottom):")
        for i in reversed(stack):
            print(i)

while True:    #MENU-DRIVEN LIST FOR USER
    print("\n----STACK OPERATIONS----\n")
    print("1. PUSH (ADD)")
    print("2. POP (REMOVE)")
    print("3. PEEK (TOP ELEMENT)")
    print("4. CHECK IF EMPTY")
    print("5. DISPLAY STACK")
    print("6. EXIT")

    choice = input("Enter your choice of operation (1-6):")

    if(choice == '1'):
        value = int(input("Enter the value to add:"))  #LIST IS A DYNAMIC DATA TYPE, THEREFORE NO NEED OF CHECKING WHETHER THE STACK IS FULL OR NOT (STACK OVERFLOW CONDITION)
        stack.append(value)
        print(f"{value} is added to the Stack!")

    elif(choice == '2'):
        if(len(stack)==0):
            print("Stack is Empty")
        else:
            popped = stack.pop()  #REMOVES THE TOP-MOST ELEMENT (LIFO PRINCIPLE)
            print(f"Popped: {popped}")
    
    elif(choice == '3'):
        if(len(stack)==0):
            print("Empty Stack")
        else:
            print("Peeked Element:",stack[-1]) #RETURNS THE TOP-MOST ELEMENT
    
    elif(choice=='4'):
        if(len(stack)==0):
            print("Empty Stack")
        else:
            print("Stack has elements")
    
    elif(choice=='5'):
        display_stack()
    
    elif choice == '6':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 6.")

# TEST CASE
# ----STACK OPERATIONS----

# 1. PUSH (ADD)        
# 2. POP (REMOVE)      
# 3. PEEK (TOP ELEMENT)
# 4. CHECK IF EMPTY
# 5. DISPLAY STACK
# 6. EXIT
# Enter your choice of operation (1-6):1
# Enter the value to add:54
# 54 is added to the Stack!

# ----STACK OPERATIONS----

# 1. PUSH (ADD)
# 2. POP (REMOVE)
# 3. PEEK (TOP ELEMENT)
# 4. CHECK IF EMPTY
# 5. DISPLAY STACK
# 6. EXIT
# Enter your choice of operation (1-6):1
# Enter the value to add:56
# 56 is added to the Stack!

# ----STACK OPERATIONS----

# 1. PUSH (ADD)
# 2. POP (REMOVE)
# 3. PEEK (TOP ELEMENT)
# 4. CHECK IF EMPTY
# 5. DISPLAY STACK
# 6. EXIT
# Enter your choice of operation (1-6):1
# Enter the value to add:85
# 85 is added to the Stack!

# ----STACK OPERATIONS----

# 1. PUSH (ADD)
# 2. POP (REMOVE)
# 3. PEEK (TOP ELEMENT)
# 4. CHECK IF EMPTY
# 5. DISPLAY STACK
# 6. EXIT
# Enter your choice of operation (1-6):5
# Stack (top -> bottom):
# 85
# 56
# 54

# ----STACK OPERATIONS----

# 1. PUSH (ADD)
# 2. POP (REMOVE)
# 3. PEEK (TOP ELEMENT)
# 4. CHECK IF EMPTY
# 5. DISPLAY STACK
# 6. EXIT
# Enter your choice of operation (1-6):2
# Popped: 85

# ----STACK OPERATIONS----

# 1. PUSH (ADD)
# 2. POP (REMOVE)
# 3. PEEK (TOP ELEMENT)
# 4. CHECK IF EMPTY
# 5. DISPLAY STACK
# 6. EXIT
# Enter your choice of operation (1-6):3
# Peeked Element: 56

# ----STACK OPERATIONS----

# 1. PUSH (ADD)
# 2. POP (REMOVE)
# 3. PEEK (TOP ELEMENT)
# 4. CHECK IF EMPTY
# 5. DISPLAY STACK
# 6. EXIT
# Enter your choice of operation (1-6):5
# Stack (top -> bottom):
# 56
# 54

# ----STACK OPERATIONS----

# 1. PUSH (ADD)
# 2. POP (REMOVE)
# 3. PEEK (TOP ELEMENT)
# 4. CHECK IF EMPTY
# 5. DISPLAY STACK
# 6. EXIT
# Enter your choice of operation (1-6):6
# Exiting... Thank you!
