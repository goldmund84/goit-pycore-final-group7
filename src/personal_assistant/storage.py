"""
Storage module for saving and loading contacts and notes.
"""

import pickle

from contacts.address_book import AddressBook
from notes.note import NoteBook

# -------------------------
# SAVE/LOAD DATA TO/FROM FILE
# -------------------------


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


def save_notes(notebook, filename="notes.pkl"):
    """Зберігає NoteBook у файл."""
    with open(filename, "wb") as f:
        pickle.dump(notebook, f)


def load_notes(filename="notes.pkl"):
    """Завантажує NoteBook з файлу або створює нову."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NoteBook()
