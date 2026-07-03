# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: EventBoard
def archive_old_events(events, cutoff_date=None):
    if cutoff_date is None:
        from datetime import datetime, timedelta
        cutoff_date = datetime.now() - timedelta(days=30)
    
    archived_count = 0
    for event in events:
        end_date = event.get('end_date')
        status = event.get('status', 'active')
        
        if (end_date and datetime.fromisoformat(end_date.replace('Z', '+00:00')) < cutoff_date) or \
           status == 'completed':
            event['archived'] = True
            archived_count += 1
    
    return events, archived_count
