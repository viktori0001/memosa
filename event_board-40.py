# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: EventBoard
import argparse

def main():
    parser = argparse.ArgumentParser(description="EventBoard CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    cmd_plan = subparsers.add_parser("plan", help="Создать план события")
    cmd_plan.add_argument("--name", required=True, help="Название события")
    cmd_plan.add_argument("--date", required=False, default=None)
    
    cmd_add_task = subparsers.add_parser("add-task", help="Добавить задачу к событию")
    cmd_add_task.add_argument("--event", required=True, help="ID или название события")
    cmd_add_task.add_argument("--description", required=True, help="Описание задачи")
    
    cmd_list_events = subparsers.add_parser("list-events", help="Показать все события")
    
    args = parser.parse_args()
    if not hasattr(args, "command"):
        print("Укажите команду: plan, add-task или list-events")
        return
    
    commands = {
        "plan": lambda a: create_event(a.name, a.date),
        "add-task": lambda a: add_task_to_event(a.event, a.description),
        "list-events": lambda _: list_events(),
    }
    
    func = commands.get(args.command)
    if func is None or args.command not in ["plan", "add-task", "list-events"]:
        print("Неизвестная команда")
        return
    
    try:
        result = func(args)
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
