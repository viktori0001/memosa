# === Stage 17: Добавь группировку записей по категориям ===
# Project: EventBoard
from collections import defaultdict

def group_by_category(records, key_field='category'):
    grouped = defaultdict(list)
    for record in records:
        if isinstance(record.get(key_field), list):
            for cat in record[key_field]:
                grouped[cat].append(record.copy())
        else:
            grouped[record[key_field]].append(record.copy())
    return dict(grouped)
