# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: EventBoard
def reset_demo_data():
    """Сбросить демо-данные в глобальные структуры."""
    global participants, tasks, budget_remaining, schedule
    participants = [
        {"id": 1, "name": "Анна", "role": "организатор"},
        {"id": 2, "name": "Борис", "role": "участник"},
        {"id": 3, "name": "Виктория", "role": "участник"},
    ]
    tasks = [
        {"id": 1, "title": "Подготовить программу", "assigned_to": 1, "done": False},
        {"id": 2, "title": "Забронировать зал", "assigned_to": 1, "done": True},
    ]
    budget_remaining = 5000
    schedule = [
        {"day": 1, "events": ["Регистрация", "Мастер-класс"]},
        {"day": 2, "events": ["Дискуссия", "Нетворкинг"]},
    ]

def clear_state():
    """Полная очистка всех данных."""
    global participants, tasks, budget_remaining, schedule
    participants = []
    tasks = []
    budget_remaining = 0
    schedule = []
