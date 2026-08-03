# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: EventBoard
def run_doc_scenarios():
    """Запуск демонстрации сценариев использования EventBoard.

    Сценарии:
      1) Создание события, добавление участников и задач.
      2) Распределение бюджета по задачам.
      3) Проверка расписания на конфликты.
      4) Вывод итоговой сводки.

    Используется для учебных целей — показывает, как разные части
    системы взаимодействуют друг с другом при типичном планировании.
    """
    from event_board import EventBoard

    board = EventBoard(name="Конференция по AI", date=datetime.date(2026, 10, 5), venue="Zoom")

    # Сценарий 1: участники и задачи
    board.add_participant("Alice", "speaker")
    board.add_participant("Bob", "organizer")
    tasks = [
        {"title": "Подготовить слайды", "assignee": "Alice", "status": "planned"},
        {"title": "Отправить приглашения", "assignee": "Bob", "status": "in_progress"},
        {"title": "Регистрация гостей", "assignee": "Bob", "status": "done"},
    ]
    for t in tasks:
        board.add_task(t)

    # Сценарий 2: бюджет
    budget = {"total": 5000, "spent": 1200}
    board.set_budget(budget)

    # Сценарий 3: расписание (виртуальное — все в Zoom, конфликтов нет)
    schedule = {
        "morning": ["10:00-11:00", "11:30-12:30"],
        "afternoon": ["14:00-15:00", "15:30-16:30"],
    }
    board.set_schedule(schedule)

    # Сценарий 4: сводка
    print(board.summary())
