
from random import randint

def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide a name and phone number along with command (e.g. add Jane 8099640..)."
    name, phone = args
    if name in contacts:
        num = randint(1, 5)
        return f"Contact '{name}' is already exist'. You can add '{name}{num}' instead"
    contacts[name] = phone
    return f"Contact '{name}' added with phone number '{phone}'."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide a name and new phone number along with command (e.g. change Jane 8099640..)."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact '{name}' updated with new phone number '{phone}'."
    else:
        return f"Error: Contact '{name}' not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Please provide the contact name."
    name = args[0]
    return contacts.get(name, f"Error: Contact '{name}' not found.")

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
