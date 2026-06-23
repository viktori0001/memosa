# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: EventBoard
def search_events(query, fields=None):
    if not query:
        return events.copy()
    q = query.lower().strip()
    if fields is None:
        fields = ['name', 'date', 'location']
    results = []
    for event in events:
        match = False
        for f in fields:
            val = str(event.get(f, '')).lower()
            if q in val:
                match = True
                break
        if match:
            results.append(event)
    return results
