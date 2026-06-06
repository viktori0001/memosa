# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: EventBoard
class ValidationError(Exception):
    pass

def validate_event_name(name: str) -> bool:
    if not name or len(name) > 100:
        raise ValidationError("Имя события должно быть от 1 до 100 символов.")
    return True

def validate_date(date_str: str) -> bool:
    try:
        from datetime import datetime
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValidationError("Дата должна быть в формате YYYY-MM-DD.")

def validate_budget(amount: float) -> bool:
    if amount < 0 or amount > 1_000_000:
        raise ValidationError("Бюджет должен быть от 0 до 1 000 000 рублей.")
    return True

def validate_participant_name(name: str) -> bool:
    if not name or len(name) > 50:
        raise ValidationError("Имя участника должно быть от 1 до 50 символов.")
    return True

def validate_task_description(desc: str) -> bool:
    if not desc or len(desc) > 500:
        raise ValidationError("Описание задачи должно быть от 1 до 500 символов.")
    return True
