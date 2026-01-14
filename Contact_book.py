contact = {}
contact_file = "contact.txt"

def load_contact():
    try:
        with open (contact_file,"a") as file :
            for line in file:
                name,phone = line.strip().split(",")
                contact[name] = phone 
    except FileNotFoundError:
        pass

def save_contacts():
    with open(contact_file, "w") as file:
        for name, phone in contact.items():
            file.write(f"{name},{phone}\n")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")
    contact[name] = phone 
    print("Contact added")


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
        