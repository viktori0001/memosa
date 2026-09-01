# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: EventBoard
import json, os

MIGRATION_FILE = os.path.join(os.path.dirname(__file__), "migrations", "v1.json")

def migrate_v1_to_v2():
    if not os.path.exists(MIGRATION_FILE):
        return
    with open(MIGRATION_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    if data.get("version") != 1:
        return
    schema_v1 = {
        "participants": list(data.get("participants", [])),
        "tasks": list(data.get("tasks", [])),
        "budget": data.get("budget", 0),
        "schedule": data.get("schedule", {}),
    }
    schema_v2 = {
        "participants": schema_v1["participants"],
        "tasks": schema_v1["tasks"],
        "budget": schema_v1["budget"],
        "schedule": schema_v1["schedule"],
        "version": 2,
    }
    with open(MIGRATION_FILE, "w", encoding="utf-8") as f:
        json.dump(schema_v2, f, ensure_ascii=False, indent=2)
    print("Migrated v1 -> v2")

def run_migrations():
    migrate_v1_to_v2()

if __name__ == "__main__":
    run_migrations()
