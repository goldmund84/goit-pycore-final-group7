"""
Record class for managing contact information.
"""


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
