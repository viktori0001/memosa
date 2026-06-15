# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: EventBoard
def run_cli():
    while True:
        print("\n=== EventBoard CLI ===")
        print("1. Показать все события")
        print("2. Добавить событие")
        print("3. Редактировать событие")
        print("4. Удалить событие")
        print("5. Выход")
        choice = input("Выберите действие: ").strip()
        
        if not events_db and not tasks_db and not participants_db:
            init_sample_data()

        if choice == "1":
            display_events()
        elif choice == "2":
            add_event()
        elif choice == "3":
            edit_event()
        elif choice == "4":
            delete_event()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
