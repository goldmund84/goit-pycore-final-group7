"""
AddressBook class for managing collection of contacts.
"""
from collections import UserDict
from datetime import datetime, timedelta
# import re
# import pickle

# --------------------- ADDRESSBOOK CLASS ---------------------

class AddressBook(UserDict):
    """Клас для зберігання та управління записами контактів."""
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        """Знаходить запис за іменем."""
        return self.data.get(name)  # повертаємо None, якщо не знайдено

    def delete(self, name):
        """Видаляє запис за іменем."""
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Record not found.")

    def get_upcoming_birthdays(self):
        """Повертає користувачів, яких треба привітати протягом наступного тижня."""
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = record.birthday.value
            birthday_date = datetime.strptime(birthday, "%d.%m.%Y").date()
            birthday_this_year = birthday_date.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            days_until_birthday = (birthday_this_year - today).days

            if 0 <= days_until_birthday <= 7:
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays
    
    #def edit_record(self):

