# === Stage 20: Добавь восстановление записей из архива ===
# Project: EventBoard
def restore_from_archive(archive_path, db):
    import json
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for record_type in ['events', 'participants', 'tasks']:
            if record_type in data and isinstance(data[record_type], list):
                db[record_type].extend(data[record_type])
        print("Архив успешно восстановлен.")
    except FileNotFoundError:
        print(f"Файл архива не найден: {archive_path}")
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON из архива: {e}")
