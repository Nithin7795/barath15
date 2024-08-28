import json

# Initialize the contact book dictionary
contact_book = {}

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contact_book, file, indent=4)

def load_contacts():
    global contact_book
    try:
        with open('contacts.json', 'r') as file:
            contact_book = json.load(file)
    except FileNotFoundError:
        contact_book = {}

def add_contact():
    phone = input("Enter contact phone number: ").strip()
    if phone in contact_book:
        print("Contact with this phone number already exists.")
        return

    name = input("Enter contact name: ").strip()
    
    contact_book[phone] = {'name': name}
    save_contacts()
    print(f"Contact with phone number {phone} added successfully.")

def view_contacts():
    if not contact_book:
        print("No contacts available.")
        return

    for phone, details in contact_book.items():
        print(f"Phone: {phone}")
        print(f"  Name: {details['name']}")
        print()

def search_contact():
    search_type = input("Search by (1) Phone Number or (2) Name: ").strip()
    
    if search_type == '1':
        phone = input("Enter phone number to search: ").strip()
        contact = contact_book.get(phone)
        
        if contact:
            print(f"Phone: {phone}")
            print(f"  Name: {contact['name']}")
        else:
            print("Contact not found.")
    
    elif search_type == '2':
        name = input("Enter name to search: ").strip()
        found = False
        for phone, details in contact_book.items():
            if details['name'].lower() == name.lower():
                print(f"Phone: {phone}")
                print(f"  Name: {details['name']}")
                found = True
        
        if not found:
            print("Contact not found.")
    
    else:
        print("Invalid choice.")

def update_contact():
    search_type = input("Update by (1) Phone Number or (2) Name: ").strip()
    
    if search_type == '1':
        phone = input("Enter phone number to update: ").strip()
        if phone not in contact_book:
            print("Contact not found.")
            return
        
        new_name = input("Enter new name: ").strip()
        contact_book[phone] = {'name': new_name}
        save_contacts()
        print(f"Contact with phone number {phone} updated successfully.")
    
    elif search_type == '2':
        name = input("Enter name of contact to update: ").strip()
        found = False
        for phone, details in contact_book.items():
            if details['name'].lower() == name.lower():
                new_name = input("Enter new name: ").strip()
                contact_book[phone] = {'name': new_name}
                save_contacts()
                print(f"Contact with phone number {phone} updated successfully.")
                found = True
                break
        
        if not found:
            print("Contact not found.")
    
    else:
        print("Invalid choice.")

def delete_contact():
    search_type = input("Delete by (1) Phone Number or (2) Name: ").strip()
    
    if search_type == '1':
        phone = input("Enter phone number to delete: ").strip()
        if phone not in contact_book:
            print("Contact not found.")
            return
        
        del contact_book[phone]
        save_contacts()
        print(f"Contact with phone number {phone} deleted successfully.")
    
    elif search_type == '2':
        name = input("Enter name of contact to delete: ").strip()
        found = False
        for phone, details in contact_book.items():
            if details['name'].lower() == name.lower():
                del contact_book[phone]
                save_contacts()
                print(f"Contact with name {name} and phone number {phone} deleted successfully.")
                found = True
                break
        
        if not found:
            print("Contact not found.")
    
    else:
        print("Invalid choice.")

def main():
    load_contacts()
    
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
