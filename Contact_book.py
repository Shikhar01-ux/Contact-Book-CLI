contact = {}
contact_file = "contact.txt"

def save_contacts():
    with open(contact_file, "w") as file:
        for name, phone in contact.items():
            file.write(f"{name},{phone}\n")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")
    contact[name] = phone 
    print("Contact added")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contact:
        del contact[name]
        save_contacts()
        print("🗑 Contact deleted")
    else:
        print("❌ Contact not found")

def search_contact():
    name = input("Enter name to search: ")
    if name in contact:
        print(f"{name} : {contact[name]}")
    else:
        print(" Contact not found")

def view_contact():
    if not contact:
        print ("No contact found")
        return
    print("\n Contact list")
    for name,phone in contact.items():
        print(f"{name} : {phone}")

while True:
    print("\n----Contact Book----")
    print("1. Add contact")
    print("2. View contact")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_contact()

    elif choice == 2:
        view_contact()
    elif choice == 3:
        print("Exiting contact book. Bye Bye")
        break
    else:
        print("Invalid choice")
        