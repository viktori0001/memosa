# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: EventBoard
def demo():
    """Показывает основной пользовательский сценарий EventBoard."""
    board = EventBoard("Конференция по AI")
    board.set_budget(10000)

    # Участники
    board.add_participant("Анна", "Организатор")
    board.add_participant("Борис", "Спикер")
    board.add_participant("Виктория", "Спикер")

    # Задачи
    board.add_task("Заказать аудиторию", "Анна", 2000)
    board.add_task("Подготовить слайды", "Борис", 0)
    board.add_task("Написать пресс-релиз", "Анна", 500)

    # Расписание
    board.add_schedule("Регистрация", "09:00-10:00", "Анна")
    board.add_schedule("Приветственное слово", "10:00-10:30", "Анна")
    board.add_schedule("Спикер: Борис", "10:30-11:30", "Борис")
    board.add_schedule("Спикер: Виктория", "11:30-12:30", "Виктория")
    board.add_schedule("Свободный вопрос", "12:30-13:00", "Анна")

    print("=== EventBoard Demo ===")
    print(f"Событие: {board.name}")
    print(f"Бюджет: {board.budget} руб.")
    print(f"Участников: {len(board.participants)}")
    print(f"Задач: {len(board.tasks)}")
    print(f"Событий в расписании: {len(board.schedule)}")
    print(f"Заключено задач: {board.get_completed_count()}")
    print(f"Свободный бюджет: {board.get_remaining_budget()} руб.")
