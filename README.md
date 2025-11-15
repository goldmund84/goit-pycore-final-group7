# Personal Assistant - CLI Application

Персональний помічник з інтерфейсом командного рядка для управління контактами та нотатками.

## Опис проєкту

Personal Assistant - це консольна програма для зберігання контактів адресної книги та нотаток. Програма дозволяє додавати, редагувати, видаляти та шукати інформацію, а також автоматично зберігає всі дані між сесіями.

### Основні можливості

**Управління контактами:**
- Додавання, редагування та видалення контактів
- Зберігання імені, телефонів, email, адреси та дня народження
- Пошук контактів за іменем або номером телефону або датою народження(частковою)
- Перегляд майбутніх днів народження (на наступні 7 днів)
- Валідація номерів телефонів, email та дат

**Управління нотатками:**
- Створення та редагування нотаток
- Додавання тегів для категоризації
- Пошук нотаток за ключовими словами
- Пошук нотаток за тегами
- Сортування нотаток за кількістю тегів
- Автоматичні мітки часу створення

**Інші функції:**
- Автоматичне збереження даних при виході
- Автодоповнення команд при введенні (натисніть TAB)
- Підтримка команди help для довідки
- Обробка помилок та валідація введення

## Вимоги

- Python 3.9 або вище
- Залежності:
  - `prompt_toolkit>=3.0.0` - для автодоповнення команд в CLI

## Встановлення

### 1. Клонування репозиторію

```bash
git clone https://github.com/your-username/goit-pycore-final-group7.git
cd goit-pycore-final-group7
```

### 2. Створення віртуального середовища (рекомендовано)

```bash
python3 -m venv venv
source venv/bin/activate  # Для Linux/Mac
# або
venv\Scripts\activate  # Для Windows
```

### 3. Встановлення пакета

```bash
# Встановлення в режимі розробки
pip install -e .

# Або звичайне встановлення
pip install .
```

### 4. Альтернативний спосіб встановлення

Якщо ви хочете встановити залежності без встановлення пакета:

```bash
pip install -r requirements.txt
python -m personal_assistant.main
```

## Використання

Після встановлення пакета запустіть програму командою:

```bash
personal-assistant
```

Або через Python модуль:

```bash
python -m personal_assistant.main
```

## Команди

### Загальні команди

| Команда | Опис |
|---------|------|
| `hello` | Привітання від бота |
| `help` | Показати всі доступні команди з описом |
| `close` або `exit` | Зберегти дані та вийти з програми |

### Команди для роботи з контактами

| Команда | Параметри | Опис |
|---------|-----------|------|
| `add` | `[ім'я] [телефон]` | Додати новий контакт або телефон до існуючого |
| `change` | `[ім'я] [старий_телефон] [новий_телефон]` | Змінити номер телефону контакту |
| `phone` | `[ім'я]` | Показати телефони контакту |
| `all-contacts` | - | Показати всі контакти |
| `add-birthday` | `[ім'я] [ДД.ММ.РРРР]` | Додати день народження до контакту |
| `show-birthday` | `[ім'я]` | Показати день народження контакту |
| `birthdays` | - | Показати дні народження на наступний тиждень |
| `find-birthday` | `[частина ДД.ММ.РРРР]` | Показати всі контакти з частковим співпадінням дати народження |
| `search-contact` | `[запит]` | Знайти контакти за іменем або номером телефону |
| `delete-contact` | `[ім'я]` | Видалити контакт |
| `add-email` | `[ім'я] [email]` | Додати email до контакту |
| `add-address` | `[ім'я] [адреса]` | Додати адресу до контакту |

### Команди для роботи з нотатками

| Команда | Параметри | Опис |
|---------|-----------|------|
| `add-note` | `[контент]` | Створити нотатку. Увесь зміст вводиться в один рядок. |
| `show-notes` | - | Показати всі нотатки. |
| `find-note` | `[ключове-слово]` | Знайти нотатки за ключовим словом у контенті. |
| `edit-note` | `[id] [новий_контент]` | Редагувати нотатку за ID. |
| `delete-note` | `[id]` | Видалити нотатку за ID. |
| `add-tag` | `[id] [тег]` | Додати тег до нотатки за ID. |
| `find-by-tag` | `[тег]` | Знайти нотатки за тегом. |
| `sort-notes-by-tag` | - | Показати всі нотатки, відсортовані за кількістю тегів. |

## Приклади використання

### Робота з контактами

```bash
# Запуск програми
$ personal-assistant
Welcome to the assistant bot!

# Додавання контакту
Enter a command: add John 0501234567
Contact added.

# Додавання дня народження
Enter a command: add-birthday John 15.06.1990
Birthday added for John.

# Додавання email
Enter a command: add-email John john@example.com
Email added for John.

# Додавання адреси
Enter a command: add-address John Kyiv_Main_Street_123
Address added for John.

# Перегляд всіх контактів
Enter a command: all-contacts
John: 0501234567, john@example.com, Kyiv_Main_Street_123

# Перегляд телефонів контакту
Enter a command: phone John
0501234567

# Пошук контакту
Enter a command: search-contact John
Found 1 contact(s):
  John: 0501234567, john@example.com, Kyiv_Main_Street_123

# Майбутні дні народження
Enter a command: birthdays
John -> 17.06.2025
```

### Робота з нотатками

```bash
# Додавання нотатки
# Увесь контент вводиться в одному рядку
Enter a command: add-note Buy milk, bread, eggs
Note added with ID: 1

# Додавання ще однієї нотатки
Enter a command: add-note Finish project presentation
Note added with ID: 2

# Додавання тегів
Enter a command: add-tag 1 shopping
Tag 'shopping' added to Note ID 1.

Enter a command: add-tag 2 work
Tag 'work' added to Note ID 2.

Enter a command: add-tag 2 urgent
Tag 'urgent' added to Note ID 2.

# Перегляд всіх нотаток
Enter a command: show-notes
--- Note Book ---
ID 1: [2025-11-16 00:08:23] Note: Buy milk, bread, eggs (Tags: shopping)
ID 2: [2025-11-16 00:08:23] Note: Finish project presentation (Tags: work, urgent)

# Пошук за тегом
Enter a command: find-by-tag work
Found 1 notes with tag 'work':
ID 2: [2025-11-16 00:08:23] Note: Finish project presentation (Tags: work, urgent)

# Сортування нотаток за тегами
Enter a command: sort-notes-by-tag
--- Notes Sorted by Tags ---
ID 2 [2 tag(s)]: [2025-11-16 00:08:23] Note: Finish project presentation (Tags: work, urgent)
ID 1 [1 tag(s)]: [2025-11-16 00:08:23] Note: Buy milk, bread, eggs (Tags: shopping)
```

## Структура проєкту

```
goit-pycore-final-group7/
├── src/
│   └── personal_assistant/
│       ├── __init__.py
│       ├── main.py                # Точка входу
│       ├── contacts/              # Управління контактами
│       │   ├── __init__.py
│       │   ├── fields.py          # Field, Name, Phone, Email, etc.
│       │   ├── contact.py         # Record (контакт)
│       │   └── address_book.py    # AddressBook
│       ├── notes/                 # Управління нотатками
│       │   ├── __init__.py
│       │   ├── note.py            # Note (нотатка)
│       │   └── handlers.py        # Note handlers
│       ├── storage.py             # Збереження даних
│       └── cli.py                 # CLI інтерфейс
├── setup.py                       # Конфігурація пакета
├── requirements.txt               # Залежності
├── README.md                      # Документація
└── .gitignore
```

## Формати даних

### Номер телефону
- Тільки цифри
- Рівно 10 символів
- Приклад: `0501234567`

### Дата народження
- Формат: `ДД.ММ.РРРР`
- Приклад: `15.06.1990`

### Email
- Валідація за стандартним форматом email
- Приклад: `user@example.com`

## Збереження даних

Програма автоматично зберігає всі дані у файли при виході:
- `addressbook.pkl` - контакти адресної книги
- `notes.pkl` - нотатки

Дані завантажуються автоматично при наступному запуску програми.

## Обробка помилок

Програма коректно обробляє наступні ситуації:
- Некоректний формат команди
- Невірний формат телефону, дати або email
- Відсутній контакт або нотатка
- Недостатня кількість параметрів
- Спроба додати дублікат

## Розробка

### Запуск у режимі розробки

```bash
# Встановлення у режимі розробки
pip install -e .

# Запуск тестів (якщо є)
pytest

# Перевірка PEP 8
flake8 src/
```

## Автори

Проєкт розроблено командою goit-pycore-final-group7

