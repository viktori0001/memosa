# === Stage 45: Добавь восстановление из резервной копии ===
# Project: EventBoard
import json, os

def load_backup(file_path):
    if not file_path:
        return None
    if not os.path.exists(file_path):
        print(f"Резервная копия не найдена: {file_path}")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка загрузки резервной копии: {e}")
        return None
