# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: EventBoard
import json
import os
from datetime import datetime

def backup_data_file(data_file_path, backup_dir="backups"):
    """Создаёт резервную копию файла данных с автоматическим переименованием по дате."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    if not data_file_path or not os.path.isfile(data_file_path):
        return None
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}_{os.path.basename(data_file_path)}")
    try:
        with open(data_file_path, "rb") as src, open(backup_path, "wb") as dst:
            dst.write(src.read())
        return backup_path
    except Exception as e:
        print(f"Ошибка резервного копирования: {e}")
        return None
