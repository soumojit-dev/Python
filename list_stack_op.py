stack = []

def display_stack():
    if(len(stack)==0):
        print("Underflow Condition")
    else:
        print("Stack (top -> bottom):")
        for i in reversed(stack):
            print(i)

while True:
    print("\n----STACK OPERATIONS----\n")
    print("1. PUSH (ADD)")
    print("2. POP (REMOVE)")
    print("3. PEEK (TOP ELEMENT)")
    print("4. CHECK IF EMPTY")
    print("5. DISPLAY STACK")
    print("6. EXIT")

    choice = int(input("Enter your choice of operation (1-6):"))

    if(choice == '1'):
        value = int(input("Enter the value to add:"))
        stack.append(value)
        print(f"{value} is added to the Stack!")

    elif(choice == '2'):
        if(len(stack)==0):
            print("Stack is Empty")
        else:
            popped = stack.pop()
            print(f"Popped: {popped}")
    
    elif(choice == '3'):
        if(len(stack)==0):
            print("Empty Stack")
        else:
            print("Peeked Element:",stack[-1])
    
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
