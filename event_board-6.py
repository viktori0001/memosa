# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: EventBoard
def filter_events(events, filters=None):
    if not filters:
        return events
    filtered = []
    for event in events:
        match_status = filters.get('status') is None or event['status'] == filters['status']
        match_category = filters.get('category') is None or event['category'] == filters['category']
        match_tags = all(tag in event.get('tags', []) for tag in filters.get('tags', []))
        if match_status and match_category and match_tags:
            filtered.append(event)
    return filtered
