FILE_NAME = "contacts.txt"
contacts = {}

# Load contacts from file
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass

# Save contacts to file
def save_contacts():
    with open(FILE_NAME, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists")
        return

    phone = input("Enter phone number: ")
    contacts[name] = phone
    save_contacts()
    print("Contact saved")

def view_contacts():
    if not contacts:
        print("No contacts found")
        return

    print("\nContact List")
    for name, phone in contacts.items():
        print(f"{name} : {phone}")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted")
    else:
        print("Contact not found")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found")

def menu():
    load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

menu()
