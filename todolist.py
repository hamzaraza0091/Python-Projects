tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    
    elif choice == "2":
        print("\nYour Tasks:")
        for t in tasks:
            print("-", t)
    
    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found.")
    
    elif choice == "4":
        break
    else:
        print("Invalid choice.")