# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: EventBoard
def export_to_json():
    import json
    data = {
        "event": event_name,
        "participants": participants_list,
        "tasks": tasks_dict,
        "budget": budget_total,
        "schedule": schedule_items
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
