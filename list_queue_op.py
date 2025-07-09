queue = [] #EMPTY LIST FOR QUEUE

def enq(): #FUNCTION TO INSERT ELEMENT FROM THE END OF THE QUEUE (REAR)
    value = input("Enter the value to insert in the Queue:")
    queue.append(value)
    print(f"{value} is inserted in the Queue")

def dq():  #FUNCTION TO REMOVE THE FIRST ELEMENT FROM THE QUEUE (FRONT)
    if(len(queue)==0):
        print("Underflow Condition Occured!")
    else:
        removed = queue.pop()  #QUEUE FOLLOWS FIFO PRINCIPLE
        print("Popped Element:",removed)

def peek():  #FUNCTION THAT RETURNS THE FIRST ELEMENT IN THE QUEUE
    if(len(queue)==0):
        print("Stack is Empty")
    else:
        print("Peek element:",queue[-1])
    
def display():
    if(len(queue)==0):
        print("Empty Stack")
    else:
        print("Queue (Front -> Rear):",queue)

while True:  #MENU-DRIVEN PROGRAM FOR USERS
    print("\n---QUEUE OPERATIONS---\n")
    print("1. Enqueue (Inserts element in the Queue from the end)")
    print("2. DEQUEUE (Removes element from the front of the queue)")
    print("3. PEEK (Returns the first element in the queue)")
    print("4. DISPLAY QUEUE")
    print("5. EXIT")

    ch = input("Enter your choice of operation from the menu:")

    if ch == '1':
        enq()
    elif ch == '2':
        dq()
    elif ch == '3':
        peek()
    elif ch == '4':
        display()
    elif ch == '5':
        print("EXITING...THANK YOU")
        break
    else:
        print("INVALID INPUT!")

# TEST CASE
# ---QUEUE OPERATIONS---

# 1. Enqueue (Inserts element in the Queue from the end)  
# 2. DEQUEUE (Removes element from the front of the queue)
# 3. PEEK (Returns the first element in the queue)        
# 4. DISPLAY QUEUE
# 5. EXIT
# Enter your choice of operation from the menu:1
# Enter the value to insert in the Queue:MIKE
# MIKE is inserted in the Queue

# ---QUEUE OPERATIONS---

# 1. Enqueue (Inserts element in the Queue from the end)
# 2. DEQUEUE (Removes element from the front of the queue)
# 3. PEEK (Returns the first element in the queue)
# 4. DISPLAY QUEUE
# 5. EXIT
# Enter your choice of operation from the menu:1
# Enter the value to insert in the Queue:JOSH  
# JOSH is inserted in the Queue

# ---QUEUE OPERATIONS---

# 1. Enqueue (Inserts element in the Queue from the end)
# 2. DEQUEUE (Removes element from the front of the queue)
# 3. PEEK (Returns the first element in the queue)
# 4. DISPLAY QUEUE
# 5. EXIT
# Enter your choice of operation from the menu:1
# Enter the value to insert in the Queue:KYLIE 
# KYLIE is inserted in the Queue

# ---QUEUE OPERATIONS---

# 1. Enqueue (Inserts element in the Queue from the end)
# 2. DEQUEUE (Removes element from the front of the queue)
# 3. PEEK (Returns the first element in the queue)
# 4. DISPLAY QUEUE
# 5. EXIT
# Enter your choice of operation from the menu:4
# Queue (Front -> Rear): ['MIKE', 'JOSH', 'KYLIE']

# ---QUEUE OPERATIONS---

# 1. Enqueue (Inserts element in the Queue from the end)
# 2. DEQUEUE (Removes element from the front of the queue)
# 3. PEEK (Returns the first element in the queue)
# 4. DISPLAY QUEUE
# 5. EXIT
# Enter your choice of operation from the menu:2
# Popped Element: KYLIE

# ---QUEUE OPERATIONS---

# 1. Enqueue (Inserts element in the Queue from the end)
# 2. DEQUEUE (Removes element from the front of the queue)
# 3. PEEK (Returns the first element in the queue)
# 4. DISPLAY QUEUE
# 5. EXIT
# Enter your choice of operation from the menu:3
# Peek element: JOSH

# ---QUEUE OPERATIONS---

# 1. Enqueue (Inserts element in the Queue from the end)
# 2. DEQUEUE (Removes element from the front of the queue)
# 3. PEEK (Returns the first element in the queue)
# 4. DISPLAY QUEUE
# 5. EXIT
# Enter your choice of operation from the menu:4
# Queue (Front -> Rear): ['MIKE', 'JOSH']

# ---QUEUE OPERATIONS---

# 1. Enqueue (Inserts element in the Queue from the end)
# 2. DEQUEUE (Removes element from the front of the queue)
# 3. PEEK (Returns the first element in the queue)
# 4. DISPLAY QUEUE
# 5. EXIT
# Enter your choice of operation from the menu:5
# EXITING...THANK YOU