# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: EventBoard
def generate_monthly_stats(events, start_date):
    from datetime import timedelta
    current = start_date.replace(day=1)
    stats = {}
    while current.month == events[0].month if events else False or current.year != events[-1].year:
        end = min(current + timedelta(days=32), (current.replace(month=current.month+1, day=1)) - timedelta(days=1))
        for event in events:
            if start_date <= event.date <= end:
                stats.setdefault(event.type, 0)
                stats[event.type] += 1
        current = end + timedelta(days=1)
    return stats
