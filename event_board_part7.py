# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: EventBoard
def sort_events(events, key='date'):
    if not events: return []
    reverse = False
    if key == 'priority': reverse = True
    elif key == 'name': reverse = False
    def get_sort_key(e):
        val = e.get(key) or ''
        try:
            if isinstance(val, str):
                return (0, val.lower())
            else:
                return (1, 0)
        except TypeError:
            return (2, '')
    return sorted(events, key=get_sort_key, reverse=reverse)
