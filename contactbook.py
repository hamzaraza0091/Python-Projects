contacts = {}

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Phone: ")
        contacts[name] = number
        print("Contact saved!")

    elif choice == "2":
        for name, num in contacts.items():
            print(name, ":", num)

    elif choice == "3":
        name = input("Enter name to search: ")
        print(contacts.get(name, "Not found"))

    elif choice == "4":
        break