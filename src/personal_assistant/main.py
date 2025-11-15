from cli import run_cli

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
    """
    Main function to run Personal Assistant.
    """
    run_cli()


if __name__ == "__main__":
    main()
