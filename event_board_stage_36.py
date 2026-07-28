# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: EventBoard
def check_and_repair_data():
    """Проверяет целостность данных и пытается исправить простые проблемы."""
    problems = []
    
    # Проверяем, что все участники уникальны
    if participants and not len(participants) == len(set(p[0] for p in participants)):
        seen = set()
        unique_participants = []
        for p in participants:
            if p[0] not in seen:
                seen.add(p[0])
                unique_participants.append(p)
        problems.append(f"Удалены {len(participants) - len(unique_participants)} дубликатов участников")
        participants = unique_participants
    
    # Проверяем, что все задачи привязаны к участникам
    if tasks:
        valid_tasks = []
        for t in tasks:
            if t[1] and any(p[0] == t[1] for p in participants):
                valid_tasks.append(t)
            else:
                problems.append(f"Задача '{t[2]}' без участника удалена")
        tasks = valid_tasks
    
    # Проверяем, что все задачи в расписании существуют
    if schedule and tasks:
        task_ids = set((t[1], t[0]) for t in tasks)
        valid_schedule = []
        for s in schedule:
            if (s[2], s[3]) in task_ids:
                valid_schedule.append(s)
            else:
                problems.append(f"Запись расписания '{s[4]}' без задачи удалена")
        schedule = valid_schedule
    
    # Проверяем, что бюджет не отрицательный
    if budget and budget < 0:
        problems.append("Бюджет установлен в 0 (не может быть отрицательным)")
        budget = 0
    
    return problems
