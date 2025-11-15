"""
CLI interface for command parsing and handling.
"""

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit.completion.base import CompleteEvent

from storage import (
    save_data,
    load_data,
    save_notes,
    load_notes
)

from contacts.contact import (
    # CONTACTS
    add_contact,
    search_contact,
    delete_contact,
    change_phone,
    show_phones,
    show_all,

    # BIRTHDAYS
    add_birthday,
    show_birthday,
    birthdays,
    find_by_birthday,

    # OTHER INFO
    add_email,
    add_address,
)

from notes.handlers import (
    # NOTES AND TAGS
    add_note_handler,
    find_notes_handler,
    show_all_notes_handler,
    edit_note_handler,
    delete_note_handler,
    add_tag_handler,
    find_by_tag_handler,
)


# -------------------------
# PARSER
# -------------------------

def parse_input(user_input: str):
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:]
    return command, args


# -------------------------
# COMMAND REGISTRY
# -------------------------

COMMANDS = {
    # CONTACTS
    "add": add_contact,
    "search-contact": search_contact,
    "delete-contact": delete_contact,
    "change": change_phone,
    "phone": show_phones,
    "all-contacts": show_all,

    # BIRTHDAYS
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
    "find-birthday": find_by_birthday,

    # OTHER INFO
    "add-email": add_email,
    "add-address": add_address,

    # NOTES AND TAGS
    "add-note": add_note_handler,
    "find-note": find_notes_handler,
    "show-notes": show_all_notes_handler,
    "edit-note": edit_note_handler,
    "delete-note": delete_note_handler,
    "add-tag": add_tag_handler,
    "find-by-tag": find_by_tag_handler,
}


# -------------------------
# AUTOCOMPLETER
# -------------------------


class CommandCompleter(Completer):
    def __init__(self, commands: dict):
        self.commands = list(commands.keys())

    def get_completions(self, document: Document, complete_event: CompleteEvent):
        text = document.text_before_cursor

        if " " in text:
            return

        word = document.get_word_before_cursor()

        for cmd in self.commands:
            if cmd.startswith(word):
                yield Completion(cmd, start_position=-len(word))


# -------------------------
# MAIN CLI FUNCTION
# -------------------------

def run_cli():
    session = PromptSession(
        completer=CommandCompleter(COMMANDS),
        complete_while_typing=True
    )

    book = load_data()
    notebook = load_notes()
    print("Welcome to the assistant bot!\n")

    while True:
        try:
            user_input = session.prompt("Enter a command: ")
            command, args = parse_input(user_input)

            if command in ("exit", "close"):
                save_data(book)
                save_notes(notebook)
                print("Goodbye!")
                break

            if command == "hello":
                print("How can I help you?")
                continue

            if command in COMMANDS:
                handler = COMMANDS[command]

                try:
                    result = handler(args, book, notebook)
                except TypeError:
                    try:
                        result = handler(args, book)
                    except TypeError:
                        try:
                            result = handler(args)
                        except TypeError:
                            result = handler(book)

                if result is not None:
                    print(result)
                continue

            print("Invalid command.")

        except (KeyboardInterrupt):
            print("Type 'exit' or 'close' to quit.")
            continue
