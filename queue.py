queue = []
MAX_SIZE = 2
def enqueue(item):
    if len(queue) < MAX_SIZE:
        queue.append(item)
        print(f"Enqueued {item} into the queue.")
    else:
        print("Queue is full. Cannot enqueue.")
def dequeue():
    if len(queue) == 0:
        print("Queue is empty. Cannot dequeue.")
    else:
        dequeued_item = queue.pop(0)
        print(f"Dequeued {dequeued_item} from the queue.")
def menu():
    while True:
        print("\nChoose an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Exit")
       
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            item = input("Enter the item to enqueue: ")
            enqueue(item)
        elif choice == '2':
            dequeue()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid operation.")
menu()

