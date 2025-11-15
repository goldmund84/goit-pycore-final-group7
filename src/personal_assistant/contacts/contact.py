"""
Record class for managing contact information.
"""
from collections import UserDict
from datetime import datetime, timedelta

from .fields import Name
from .fields import Phone
from .fields import Birthday
from .fields import Email
from .fields import Address
from .address_book import AddressBook

# Decorator for handling input errors
from .input_error import input_error


# --------------------- RECORD CLASS ---------------------

class Record:
    """Клас для зберігання інформації про контакт (ім’я + телефони + день народження)."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def add_phone(self, phone):
        """Додає новий номер телефону."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """Видаляє номер телефону зі списку."""
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        raise ValueError("Phone not found.")

    def edit_phone(self, old_phone, new_phone):
        """Редагує номер телефону."""
        for p in self.phones:
            if p.value == old_phone:
                p.value = Phone(new_phone).value
                return True
        raise ValueError("Old phone not found.")

    def find_phone(self, phone):
        """Пошук телефону у записі."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday):
        """Додає день народження до контакту."""
        self.birthday = Birthday(birthday)

    def add_email(self, email):
        """Додає email до контакту."""
        self.email = Email(email)
    
    def add_address(self, address):
        """Додає адресу до контакту."""
        self.address = Address(address)

    def __str__(self):
        phones = ", ".join(p.value for p in self.phones) if self.phones else "no phones"
        email = self.email.value if getattr(self, "email", None) else "no email"
        address = self.address.value if getattr(self, "address", None) else "no address"

        return f"{self.name}: {phones}, {email}, {address}"
    
# --------------------- HANDLER FUNCTIONS ---------------------
@input_error
def add_contact(args, book: AddressBook):
    if not args:
        raise ValueError("Enter name and phone. Usage: add <name> <phone>")
    
    name = args[0]
    phone = args[1] if len(args) > 1 else None
    record = book.find(name)

    if record is None and phone is None:
        raise ValueError("Phone number is required for a new contact.")
    
    if phone:
        Phone(phone)

    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def search_contact(args, book: AddressBook):
    if not args:
        raise ValueError("Enter a name. Usage: search-contact <name>")

    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError(f"Contact '{name}' not found.")

    # Convert record to a readable string
    # phones = ", ".join(p.value for p in record.phones) if record.phones else "no phones"
    # return f"{record.name}: {phones}"

     # Extract phones
    phones = ", ".join(p.value for p in record.phones) if record.phones else "no phones"

    # Extract email
    # Case 1: email stored as a single field
    email = record.email.value if getattr(record, "email", None) else "no email"

    # multiple emails?
    # email = ", ".join(e.value for e in record.emails) if record.emails else "no emails"

    # Extract address
    address = record.address.value if getattr(record, "address", None) else "no address"

    return f"{record.name}: {phones}, {email}, {address}"

@input_error
def delete_contact(args, book: AddressBook):
    if not args:
        raise ValueError("Enter a name. Usage: delete-contact <name>")

    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError(f"Contact '{name}' not found.")

    book.delete(name)
    return f"Contact '{name}' deleted."

@input_error
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.edit_phone(old_phone, new_phone)
    return "Phone number updated."

@input_error
def show_phones(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return "; ".join(p.value for p in record.phones)

def show_all(args, book: AddressBook):
    if not book.data:
        return "No contacts found."
    result = []
    for record in book.data.values():
        result.append(str(record))
    return "\n".join(result)

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_birthday(birthday)
    return f"Birthday added for {name}."

@input_error
def add_email(args, book: AddressBook):
    name, email = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_email(email)
    return f"Email added for {name}."

@input_error
def add_address(args, book: AddressBook):
    name, address = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_address(address)
    return f"Address added for {name}."


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    if not record.birthday:
        return f"{name} has no birthday set."
    return record.birthday.value

@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays this week."
    return "\n".join([f"{b['name']} -> {b['congratulation_date']}" for b in upcoming])

@input_error
def find_by_birthday(args, book: AddressBook):
    if not args:
        return "Please provide a part of birthday (DD.MM.YYYY)"

    query = args[0].lower()
    matches = []

    for name, record in book.items():
        if not getattr(record, "birthday", None):
            continue

        birthday = record.birthday.value

        if not isinstance(birthday, str):
            continue

        birthday_str = birthday.strip().lower()

        if query in birthday_str:
            matches.append(f"{name}'s birthday is {birthday_str}")

    if not matches:
        return "No contacts found"

    return "\n".join(matches)
