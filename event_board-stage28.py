# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: EventBoard
def print_project_metrics(data):
    participants = data.get("participants", [])
    tasks = data.get("tasks", [])
    budget_items = data.get("budget_items", [])
    events = data.get("events", [])

    total_participants = len(participants)
    unique_tasks = set()
    for t in tasks:
        unique_tasks.add(t["name"])
    total_unique_tasks = len(unique_tasks)

    spent = sum(item.get("spent", 0) for item in budget_items if "spent" in item)
    allocated = sum(item.get("allocated", 0) for item in budget_items)
    remaining_budget = allocated - spent

    completed = sum(1 for e in events if e.get("status") == "completed")
    total_events = len(events)
    completion_rate = (completed / total_events * 100) if total_events else 0

    print(f"=== EventBoard Project Metrics ===")
    print(f"Participants: {total_participants}")
    print(f"Unique Tasks: {total_unique_tasks}")
    print(f"Budget Spent: ${spent:.2f} / ${allocated:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")
    print(f"Events Completed: {completed}/{total_events} ({completion_rate:.1f}%)")
