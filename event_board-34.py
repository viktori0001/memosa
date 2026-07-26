# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: EventBoard
TEMPLATES = {
    "birthday": {"name": "День рождения", "budget": 500, "tasks": ["Купить подарок", "Пригласить гостей"], "schedule": "17:00"},
    "corporate": {"name": "Корпоратив", "budget": 3000, "tasks": ["Подготовить сценарий", "Забронировать зал", "Купить угощения"], "schedule": "20:00"},
}

def get_template(name):
    return TEMPLATES.get(name)
