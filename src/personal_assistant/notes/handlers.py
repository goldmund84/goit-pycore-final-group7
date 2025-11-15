from .note import Note


# --- ДОПОМІЖНА ФУНКЦІЯ (Критично важлива для edit/delete/tag) ---

def get_note_id(id_str):
    """Допоміжний конвертер ID з обробкою ValueError."""
    try:
        return int(id_str)
    except ValueError:
        raise ValueError("ID має бути цілим числом.")

# --- ОБРОБНИКИ НОТАТОК ТА ТЕГІВ ---


def add_note_handler(args, book, notebook):
    """Додає нову нотатку (однорядковий контент)."""
    if not args:
        raise IndexError("Будь ласка, введіть контент для нотатки.")

    content = " ".join(args)
    note = Note(content)  # Викине ValueError, якщо контент порожній
    note_id = notebook.add_note(note)
    return f"Note added with ID: {note_id}"


def find_notes_handler(args, book, notebook):
    """Шукає нотатки за ключовим словом."""
    if not args:
        raise IndexError("Будь ласка, введіть ключове слово для пошуку.")

    query = args[0]
    found_notes = notebook.find_note(query)

    if not found_notes:
        return f"No notes found containing: '{query}'"

    output_lines = [f"Found {len(found_notes)} notes containing '{query}':"]
    for note_id, note in found_notes.items():
        output_lines.append(f"ID {note_id}: {note}")
    return "\n".join(output_lines)


def show_all_notes_handler(args, book, notebook):
    """Показує всі нотатки."""
    return str(notebook)


def edit_note_handler(args, book, notebook):
    """Редагує існуючу нотатку за ID."""
    if len(args) < 2:
        raise IndexError("Будь ласка, введіть Note ID та новий контент.")

    note_id = get_note_id(args[0])
    new_content = " ".join(args[1:])

    # Викине KeyError, якщо ID не знайдено
    notebook.edit_note(note_id, new_content)
    return f"Note ID {note_id} updated successfully."


def delete_note_handler(args, book, notebook):
    """Видаляє нотатку за ID."""
    if not args:
        raise IndexError("Будь ласка, введіть Note ID.")

    note_id = get_note_id(args[0])

    if notebook.delete_note(note_id):
        return f"Note ID {note_id} deleted successfully."
    else:
        raise KeyError(f"Note with ID {note_id} not found.")


def add_tag_handler(args, book, notebook):
    """Додає тег до нотатки."""
    if len(args) < 2:
        raise IndexError("Будь ласка, вкажіть ID нотатки та тег.")

    note_id = get_note_id(args[0])
    tag = args[1].strip()

    if note_id not in notebook.data:
        raise KeyError(f"Нотатку з ID {note_id} не знайдено.")

    notebook.data[note_id].add_tag(tag)
    return f"Tag '{tag}' added to Note ID {note_id}."


def find_by_tag_handler(args, book, notebook):
    """Шукає нотатки за тегом."""
    if not args:
        raise IndexError("Будь ласка, введіть тег для пошуку.")

    tag_query = args[0]
    found_notes = notebook.find_by_tag(tag_query)

    if not found_notes:
        return f"Нотаток з тегом '{tag_query}' не знайдено."

    output_lines = [f"Found {len(found_notes)} notes with tag '{tag_query}':"]
    for note_id, note in found_notes.items():
        output_lines.append(f"ID {note_id}: {note}")
    return "\n".join(output_lines)
