# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: EventBoard
def generate_summary(events):
    if not events:
        return "Нет данных для сводки."
    
    total_budget = sum(e['budget'] for e in events)
    completed_tasks = sum(sum(1 for t in e.get('tasks', []) if t['done']) for e in events)
    total_tasks = sum(len(e.get('tasks', [])) for e in events)
    completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    upcoming_events = [e for e in events if e['date'] >= datetime.now().date()]
    
    summary_lines = [
        "=== Сводка EventBoard ===",
        f"Всего событий: {len(events)}",
        f"Событий в ближайшие дни: {len(upcoming_events)}",
        f"Общий бюджет: {total_budget} руб.",
        f"Выполнено задач: {completed_tasks}/{total_tasks} ({completion_rate:.1f}%)",
    ]
    
    if upcoming_events:
        summary_lines.append("Ближайшие события:")
        for e in sorted(upcoming_events, key=lambda x: x['date'])[:3]:
            summary_lines.append(f"  - {e['name']} ({e['date']})")
            
    return "\n".join(summary_lines)
