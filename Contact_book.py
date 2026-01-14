contact = {}

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
    for name,phone in contact.item():
        print(f"{name} : {phone}")
