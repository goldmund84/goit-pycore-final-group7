from collections import UserDict
from datetime import datetime

class Note:
    """
    Представляє окрему нотатку з контентом та тегами.
    """
    
    def __init__(self, content, tags=None):
        self.content = content 
        # Теги зберігаємо як множину (set) для унікальності та швидкого пошуку
        self.tags = set(tags) if tags else set()
        self.date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # --- @property та @setter для валідації контенту ---
    @property
    def content(self):
        return self._content
        
    @content.setter
    def content(self, new_content):
        # Валідація: контент не може бути порожнім
        if not new_content or not new_content.strip():
            raise ValueError("Note content cannot be empty.")
        self._content = new_content
        
    # --- Логіка керування тегами ---
    def add_tag(self, tag):
        """Додає один тег до нотатки, перетворюючи його на нижній регістр."""
        self.tags.add(tag.strip().lower())
        
    def __str__(self):
        tags_info = f" (Tags: {', '.join(self.tags)})" if self.tags else ""
        return f"[{self.date_added}] Note: {self.content}{tags_info}"

class NoteBook(UserDict):
    """
    Контейнер для об'єктів Note.
    """
    
    def __init__(self):
        super().__init__()
        self._next_id = 1 

    # --- CRUD: ДОДАВАННЯ ---
    def add_note(self, note):
        """Додає нову нотатку і повертає її ID."""
        self.data[self._next_id] = note
        self._next_id += 1
        return self._next_id - 1

    # --- CRUD: РЕДАГУВАННЯ ---
    def edit_note(self, note_id, new_content):
        """Редагує зміст нотатки за її ID."""
        if note_id not in self.data:
            raise KeyError(f"Note with ID {note_id} not found.")
        self.data[note_id].content = new_content
        return True
    
    # --- CRUD: ВИДАЛЕННЯ ---
    def delete_note(self, note_id):
        """Видаляє нотатку за ID."""
        if note_id in self.data:
            del self.data[note_id]
            return True
        return False

    # --- ПОШУК (Базовий) ---
    def find_note(self, query):
        """Здійснює пошук за ключовими словами в тексті нотатки."""
        found_notes = {}
        query = query.lower()
        for note_id, note in self.data.items():
            if query in note.content.lower():
                found_notes[note_id] = note
        return found_notes
    
    # --- ПОШУК ЗА ТЕГАМИ (Бонусне завдання) ---
    def find_by_tag(self, tag_query):
        """Знаходить нотатки, що містять заданий тег."""
        found_notes = {}
        tag_query = tag_query.strip().lower()
        for note_id, note in self.data.items():
            if tag_query in note.tags:
                found_notes[note_id] = note
        return found_notes
    
    def __str__(self):
        if not self.data:
            return "No notes saved."
        
        output_lines = ["--- Note Book ---"]
        for note_id in sorted(self.data.keys()):
            output_lines.append(f"ID {note_id}: {self.data[note_id]}")
        return "\n".join(output_lines)