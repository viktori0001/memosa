# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: EventBoard
def load_from_json(file_path):
    try:
        import json
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        return {k: v for k, v in data.items() if isinstance(v, (list, dict))}
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return {}
