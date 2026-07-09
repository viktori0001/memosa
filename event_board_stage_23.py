# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: EventBoard
def print_table(headers, rows):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if len(str(cell)) > col_widths[i]:
                col_widths[i] = len(str(cell))
    lines = []
    sep = '─' * max(col_widths) + '+'
    header_line = '| ' + ' | '.join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + ' |'
    lines.append(header_line)
    lines.append(sep)
    for row in rows:
        line = '| ' + ' | '.join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)) + ' |'
        lines.append(line)
    lines.append(sep)
    print('\n'.join(lines))

def show_events(events):
    if not events:
        print("Нет событий.")
        return
    headers = ['ID', 'Название', 'Дата', 'Бюджет', 'Статус']
    rows = []
    for ev in events:
        status_map = {'planned': 'Планируется', 'in_progress': 'В процессе', 'completed': 'Завершено'}
        budget_str = f"{ev.get('budget', 0):,.2f}" if isinstance(ev.get('budget'), float) else str(ev.get('budget', 0))
        rows.append([ev['id'], ev['title'], ev['date'], budget_str, status_map.get(ev.get('status', ''), 'Неизвестен')])
    print_table(headers, rows)

def show_participants(participants):
    if not participants:
        print("Нет участников.")
        return
    headers = ['ID', 'Имя', 'Роль']
    rows = [[p['id'], p['name'], p.get('role', '')] for p in participants]
    print_table(headers, rows)

def show_tasks(tasks):
    if not tasks:
        print("Нет задач.")
        return
    headers = ['ID', 'Задача', 'Ответственный', 'Статус']
    status_map = {'todo': 'Ожидается', 'in_progress': 'В процессе', 'done': 'Готово'}
    rows = [[t['id'], t['task'], t.get('assignee', ''), status_map.get(t.get('status', ''), '')] for t in tasks]
    print_table(headers, rows)

def show_budget(budget):
    if not budget:
        print("Нет данных о бюджете.")
        return
    total = sum(item['amount'] for item in budget)
    headers = ['Наименование', 'Сумма', 'Процент от общего']
    rows = []
    grand_total = 0
    for item in budget:
        grand_total += item['amount']
    total_str = f"{grand_total:,.2f}" if isinstance(grand_total, float) else str(grand_total)
    rows.append(['Итого', total_str, '100%'])
    print_table(headers, rows)

def show_schedule(schedule):
    if not schedule:
        print("Нет расписания.")
        return
    headers = ['Время', 'Событие']
    rows = [[slot['time'], slot.get('event', '')] for slot in schedule]
    print_table(headers, rows)

def show_all(data):
    print("=" * 40)
    print("📋 ПЛАНЕР СОБЫТИЙ: EventBoard")
    print("=" * 40)
    show_events(data.get('events', []))
    show_participants(data.get('participants', []))
    show_tasks(data.get('tasks', []))
    show_budget(data.get('budget', None))
    show_schedule(data.get('schedule', []))
