# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: EventBoard
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

def load_demo_data() -> Dict[str, Any]:
    return {
        "event_name": "Технический митап",
        "date": datetime(2024, 11, 15, 18, 0),
        "budget": 50000,
        "participants": [
            {"name": "Алексей", "role": "Спикер", "tasks": ["Подготовить доклад"], "spent": 0},
            {"name": "Мария", "role": "Организатор", "tasks": ["Заказать кейтеринг"], "spent": 2500}
        ],
        "schedule": [
            {"time": "18:00", "title": "Регистрация"},
            {"time": "19:00", "title": "Открытие"}
        ]
    }

def print_event_summary(event_data: Dict[str, Any]) -> None:
    print(f"Событие: {event_data['event_name']}")
    print(f"Дата: {event_data['date'].strftime('%d.%m.%Y %H:%M')}")
    print(f"Бюджет: {event_data['budget']} руб.")
    print("\nУчастники:")
    for p in event_data['participants']:
        print(f"  - {p['name']} ({p['role']})")
        if p['tasks']:
            print(f"    Задачи: {', '.join(p['tasks'])}")
        if p['spent']:
            print(f"    Расход: {p['spent']} руб.")
    print("\nРасписание:")
    for s in event_data['schedule']:
        print(f"  - {s['time']}: {s['title']}")

if __name__ == "__main__":
    demo = load_demo_data()
    print_event_summary(demo)
