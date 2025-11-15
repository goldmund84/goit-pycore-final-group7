"""
Main entry point for Personal Assistant CLI application.
"""
from collections import UserDict
from datetime import datetime, timedelta
import re
import pickle

from contacts.address_book import AddressBook
from contacts.contact import add_contact
from contacts.contact import search_contact
from contacts.contact import delete_contact
from contacts.contact import change_phone
from contacts.contact import show_phones
from contacts.contact import show_all
from contacts.contact import add_birthday 
from contacts.contact import add_email
from contacts.contact import add_address
from contacts.contact import show_birthday
from contacts.contact import birthdays
#---------------------  SAVE/LOAD DATA TO/FROM FILE ---------------------

def save_data(book, filename="addressbook.pkl"):
    """Зберігає AddressBook у файл."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """Завантажує AddressBook з файлу або створює нову."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

# --------------------- PARSER ---------------------

def parse_input(user_input: str):
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:]
    return command, args

def main():
    #book = AddressBook()
    book = load_data()  # завантажуємо збережені дані, якщо є
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)  # зберігаємо перед виходом
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "search-contact":
            print(search_contact(args, book))

        elif command == "delete-contact":
            print(delete_contact(args, book))

        elif command == "change":
            print(change_phone(args, book))

        elif command == "phone":
            print(show_phones(args, book))

        elif command == "all-contacts":
            print(show_all(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "add-email":
            print(add_email(args, book))

        elif command == "add-address":
            print(add_address(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
