# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: EventBoard
def parse_event_date(date_str):
    """Парсит дату в формате 'YYYY-MM-DD'. Возвращает datetime.date или None."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

def format_error(msg):
    """Возвращает понятное сообщение об ошибке с иконкой."""
    return f"❌ Ошибка: {msg}"

def is_valid_date(date_str):
    """Проверяет, корректна ли строка даты. Возвращает True/False."""
    return parse_event_date(date_str) is not None
