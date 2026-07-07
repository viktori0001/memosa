# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: EventBoard
def check_overdue_reminders():
    today = datetime.date.today()
    overdue = []
    for event in events:
        if event['deadline'] and isinstance(event['deadline'], date) and event['deadline'] < today:
            if not event.get('reminded'):
                overdue.append(event)
    return overdue
