# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: EventBoard
def calculate_weekly_stats(events):
    from datetime import date, timedelta
    week_map = {}
    for event in events:
        d = event['date']
        if isinstance(d, str):
            try:
                d = date.fromisoformat(d)
            except ValueError:
                continue
        key = (d.year, d.isocalendar()[1])
        week_map.setdefault(key, []).append(event)

    stats = []
    for (year, week), group in sorted(week_map.items()):
        start_date = date.fromisocalendar(year, week, 1)
        end_date = start_date + timedelta(days=6)
        total_budget = sum(e.get('budget', 0) for e in group)
        task_count = sum(len(e.get('tasks', [])) for e in group)
        stats.append({
            'start': start_date.isoformat(),
            'end': end_date.isoformat(),
            'event_count': len(group),
            'total_budget': total_budget,
            'task_count': task_count
        })

    return stats
