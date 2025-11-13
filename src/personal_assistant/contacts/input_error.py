# --------------------- DECORATOR ---------------------

def input_error(func):
    """Декоратор для обробки помилок користувача."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "No such contact found."
        except IndexError:
            return "Enter correct arguments."
    return inner