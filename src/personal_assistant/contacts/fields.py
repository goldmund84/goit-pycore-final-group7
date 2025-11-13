"""
Класи для полів контакту з валідацією.
"""

import re
from datetime import datetime


class Field:
    """
    Базовий клас для полів запису.
    Використовує @property та @setter для контролю значення.
    """
    def __init__(self, value):
        self.__value = None
        self.value = value  # Викликається setter

    @property
    def value(self):
        """Повертає значення поля."""
        return self.__value

    @value.setter
    def value(self, new_value):
        """Встановлює значення поля."""
        self.__value = new_value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value})"


class Name(Field):
    """
    Клас для зберігання імені контакту.
    Валідує, що ім'я не порожнє.
    """
    @Field.value.setter
    def value(self, new_value):
        """
        Встановлює ім'я з валідацією.

        Args:
            new_value: Ім'я контакту

        Raises:
            ValueError: якщо ім'я порожнє або містить лише пробіли
        """
        if not new_value or not new_value.strip():
            raise ValueError("Name cannot be empty.")
        self._Field__value = new_value.strip()


class Phone(Field):
    """
    Клас для зберігання номера телефону з валідацією.
    Телефон має містити рівно 10 цифр.
    """
    @Field.value.setter
    def value(self, new_value):
        """
        Встановлює номер телефону з валідацією.

        Args:
            new_value: Номер телефону (10 цифр)

        Raises:
            ValueError: якщо номер телефону не відповідає формату (10 цифр)
        """
        if not self._validate(new_value):
            raise ValueError("Invalid phone number format. Phone must contain exactly 10 digits.")
        self._Field__value = new_value

    @staticmethod
    def _validate(value):
        """
        Перевіряє коректність номера телефону.

        Args:
            value: Рядок для перевірки

        Returns:
            bool: True якщо номер коректний (10 цифр), False інакше
        """
        return isinstance(value, str) and value.isdigit() and len(value) == 10


class Email(Field):
    """
    Клас для зберігання email адреси з валідацією.
    Перевіряє базовий формат email.
    """
    # Простий regex для валідації email
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    @Field.value.setter
    def value(self, new_value):
        """
        Встановлює email з валідацією.

        Args:
            new_value: Email адреса

        Raises:
            ValueError: якщо email не відповідає стандартному формату
        """
        if not self._validate(new_value):
            raise ValueError("Invalid email format. Email must match pattern: user@example.com")
        self._Field__value = new_value.lower()  # Зберігаємо в нижньому регістрі

    @classmethod
    def _validate(cls, value):
        """
        Перевіряє коректність email адреси.

        Args:
            value: Рядок для перевірки

        Returns:
            bool: True якщо email коректний, False інакше
        """
        return isinstance(value, str) and re.match(cls.EMAIL_REGEX, value) is not None


class Birthday(Field):
    """
    Клас для зберігання дня народження з валідацією формату.
    Формат: DD.MM.YYYY
    """
    def __init__(self, value):
        self.__date = None
        super().__init__(value)

    @Field.value.setter
    def value(self, new_value):
        """
        Встановлює день народження з валідацією формату.

        Args:
            new_value: Дата у форматі DD.MM.YYYY

        Raises:
            ValueError: якщо дата не відповідає формату DD.MM.YYYY
        """
        try:
            # Перевірка коректності дати та перетворення рядка на об'єкт datetime
            date_obj = datetime.strptime(new_value, "%d.%m.%Y")

            # Перевірка, що дата не в майбутньому
            if date_obj > datetime.now():
                raise ValueError("Birthday cannot be in the future.")

            self._Field__value = new_value
            self.__date = date_obj
        except ValueError as e:
            if "does not match format" in str(e) or "unconverted data remains" in str(e):
                raise ValueError("Invalid date format. Use DD.MM.YYYY")
            raise

    @property
    def date(self):
        """
        Повертає datetime об'єкт дня народження.

        Returns:
            datetime: Об'єкт дати народження
        """
        return self.__date


class Address(Field):
    """
    Клас для зберігання адреси контакту.
    Валідує, що адреса не порожня.
    """
    @Field.value.setter
    def value(self, new_value):
        """
        Встановлює адресу з валідацією.

        Args:
            new_value: Адреса контакту

        Raises:
            ValueError: якщо адреса порожня або містить лише пробіли
        """
        if not new_value or not new_value.strip():
            raise ValueError("Address cannot be empty.")
        self._Field__value = new_value.strip()
