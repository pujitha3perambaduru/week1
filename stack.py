stack = []
MAX_SIZE = 2
def push(item):
    if len(stack) < MAX_SIZE:
        stack.append(item)
        print(f"Pushed {item} onto the stack.")
    else:
        print("Stack is full. Cannot push.")
def pop():
    if len(stack) == 0:
        print("Stack is empty. Cannot pop.")
    else:
        popped_item = stack.pop()
        print(f"Popped {popped_item} from the stack.")
def menu():
    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            item = input("Enter the item to push: ")
            push(item)
        elif choice == '2':
            pop()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid operation.")
menu()


