# Deque Program in Python (Without OOP)

MAX = 5
dq = [0] * MAX
front = -1
rear = -1


def insert_front():
    global front, rear

    if (front == 0 and rear == MAX - 1) or (front == rear + 1):
        print("Deque Overflow")

    else:
        item = int(input("Enter element to insert at front: "))

        if front == -1:
            front = 0
            rear = 0

        elif front == 0:
            front = MAX - 1

        else:
            front = front - 1

        dq[front] = item
        print(item, "inserted at front")


def insert_rear():
    global front, rear

    if (front == 0 and rear == MAX - 1) or (front == rear + 1):
        print("Deque Overflow")

    else:
        item = int(input("Enter element to insert at rear: "))

        if front == -1:
            front = 0
            rear = 0

        elif rear == MAX - 1:
            rear = 0

        else:
            rear = rear + 1

        dq[rear] = item
        print(item, "inserted at rear")


def delete_front():
    global front, rear

    if front == -1:
        print("Deque Underflow")

    else:
        item = dq[front]
        print(item, "deleted from front")

        if front == rear:
            front = -1
            rear = -1

        elif front == MAX - 1:
            front = 0

        else:
            front = front + 1


def delete_rear():
    global front, rear

    if rear == -1:
        print("Deque Underflow")

    else:
        item = dq[rear]
        print(item, "deleted from rear")

        if front == rear:
            front = -1
            rear = -1

        elif rear == 0:
            rear = MAX - 1

        else:
            rear = rear - 1


def display():
    global front, rear

    if front == -1:
        print("Deque is Empty")

    else:
        print("Deque elements are:")

        if front <= rear:
            for i in range(front, rear + 1):
                print(dq[i])

        else:
            for i in range(front, MAX):
                print(dq[i])

            for i in range(0, rear + 1):
                print(dq[i])


while True:
    print("\n--- DEQUE MENU ---")
    print("1. Insert Front")
    print("2. Insert Rear")
    print("3. Delete Front")
    print("4. Delete Rear")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_front()

    elif choice == 2:
        insert_rear()

    elif choice == 3:
        delete_front()

    elif choice == 4:
        delete_rear()

    elif choice == 5:
        display()

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")