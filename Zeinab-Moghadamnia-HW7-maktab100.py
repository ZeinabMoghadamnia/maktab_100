
import pickle
import re

class Contact:
    contacts = {}
    def __init__(self, name, phone, email):
        self.name = name
        self.email = email
        self.phone = phone

    def add_contact(self):
        if self.validate_email(self.email) and self.validate_phone(self.phone):
            Contact.contacts[self.name] = [self.phone, self.email]
            with open("contact_file.pickle", 'wb') as f:
                pickle.dump(Contact.contacts, f)
            return "\nAdded successfully!"
        else:
            return "\nInvalid information"
       
    def edit_contact(self, editor_name, new_phone, new_email):
        if self.validate_email(new_email) and self.validate_phone(new_phone) and (editor_name in Contact.contacts):
            Contact.contacts[self.name] = [new_phone, new_email]
            with open("contact_file.pickle", 'wb') as f:
                pickle.dump(Contact.contacts, f)
            return "\nEdited successfully!"
        else:
            return "\nNot valid!"
       
    def delete_contact(self, del_name):
        Contact.contacts.pop(del_name)
        with open("contact_file.pickle", 'wb') as f:
            pickle.dump(Contact.contacts, f)
        return f"\n{del_name} deleted successfully!"
    
    def view_contacts(self):
        with open("contact_file.pickle", 'rb') as f:
            Contact.contacts = pickle.load(f)
        print("\nContacts:")
        for key, values in Contact.contacts.items():
            print(f"Name: {key}, Phone: {values[0]}, Email: {values[1]}")
   
    def validate_email(self, email):
        pattern = re.compile(r'^[\w\.-]+@[\w\.-]+$\b')
        return bool(re.match(pattern, email))

    def validate_phone(self, phone):
        pattern = re.compile(r"^(\+98|0)?9\d{9}$")
        return bool(re.match(pattern, phone))

class User:
    users = {}
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_user(self):
        User.users[self.username] = self.password
        with open("user_file.pickle", 'wb') as f:
            pickle.dump(User.users, f)
        return "Created!"

    @staticmethod
    def authenticate():
        username = input("Enter your username: ")
        if username in User.users:
            entered_password = input("Enter your password: ")
            if User.users[username] == entered_password:
                return True
            else:
                return False
        else:
            return False
        

    def change_password(self):
        username = input("Enter your username: ")
        with open("user_file.pickle", 'rb') as f:
            User.users = pickle.load(f)
        if username in User.users:
            new_password = input("Enter your new password: ")
            self.password = new_password
            User.users[username] = self.password
            with open("user_file.pickle", 'wb') as f:
                pickle.dump(User.users, f)
            return f"\nPassword changed successfully : ({self.username} - {self.password})"
        
        else:
            return "\nThis username is not exist!"
        
u1 = User("zeinab", "123")
u2 = User("gorbe", "456")
u1.create_user()
u2.create_user()


contact = Contact("", "", "")
if u1.authenticate():
    print("\nAuthentication successful!")
    while True:
            print("\nOptions:")
            print("1. Add")
            print("2. Edit")
            print("3. Delete")
            print("4. View all")
            print("5. Quit")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "1":
                name = input("Enter your name: ")
                if name not in Contact.contacts:
                    phone = input("Enter your phone number: ")
                    email = input("Enter your email: ")
                    con = Contact(name , phone, email)
                    print(con.add_contact())
                else:
                    print(f"{name} is exist!")

            elif choice == "2":
                name = input("Enter the name to edit informations: ")
                if name in Contact.contacts:
                    new_phone = input("Enter the new phone number: ")
                    new_email = input("Enter the new email: ")
                    print(Contact(name, "", "").edit_contact(name, new_phone, new_email))
                    
                else:
                    print(f"{name} is not exist!")

            elif choice == "3":
                name = input("Enter the name of the contact to delete: ")
                print(contact.delete_contact(name))

            elif choice == "4":
                contact.view_contacts()

            elif choice == "5":
                break

            else:
                print("Invalid choice. Please select a valid option (1/2/3/4/5).")
else:
    print("Authentication failed!")