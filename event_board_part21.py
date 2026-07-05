# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: EventBoard
import datetime

def check_reminders(events):
    today = datetime.date.today()
    for event in events:
        if event.get('date') and isinstance(event['date'], str):
            try:
                target_date = datetime.datetime.strptime(event['date'], '%Y-%m-%d').date()
                if target_date == today and not event.get('notified'):
                    print(f"НАПОМИНЕНИЕ: {event['title']} ({event['description'][:30]}...) запланировано на сегодня.")
                    event['notified'] = True
            except ValueError:
                pass

# Пример вызова (раскомментируйте при наличии списка событий)
# check_reminders(events_list)
