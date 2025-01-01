'''
Question No. 02. Implement the linked list data structure for a contact list in a mobile phone. In this scenario, each contact is represented by a node in the linked list, and each node contains information about a specific person, such as their name and phone number.
'''
class ContactNode:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.next = None  # Pointer to the next node

# Class to represent the contact list
class ContactList:
    def __init__(self):
        self.head = None  # The start of the linked list

    # Function to add a contact to the list
    def add_contact(self, name, phone_number):
        new_node = ContactNode(name, phone_number)
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Append the new node at the end

    # Function to display all contacts
    def display_contacts(self):
        if not self.head:
            print("No contacts in the list.")
            return
        current = self.head
        while current:
            print(f"Name: {current.name}, Phone Number: {current.phone_number}")
            current = current.next

    # Function to delete a contact by name
    def delete_contact(self, name):
        if not self.head:
            print("No contacts to delete.")
            return
        if self.head.name == name:  # If the head node is the one to delete
            self.head = self.head.next
            print(f"Contact '{name}' deleted.")
            return
        current = self.head
        while current.next and current.next.name != name:
            current = current.next
        if current.next:  # If the contact is found
            current.next = current.next.next
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")


contacts = ContactList()
    
# Adding contacts
contacts.add_contact("Sohaib", "03192008354")
contacts.add_contact("Hammad", "03193719041")
contacts.add_contact("Shehryar", "03192047910")

# Displaying contacts
print("Contact List:")
contacts.display_contacts()

# Deleting a contact
print("\nDeleting 'Shehryar':")
contacts.delete_contact("Shehryar")
    
# Displaying contacts after deletion
print("\nUpdated Contact List:")
contacts.display_contacts()
