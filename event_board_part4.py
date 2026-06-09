# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: EventBoard
def edit_event(event_id, updates):
    if event_id not in events:
        print(f"Событие с ID {event_id} не найдено.")
        return
    
    for key, value in updates.items():
        if key in event_schema and key in events[event_id]:
            events[event_id][key] = value
        else:
            print(f"Недопустимое поле для редактирования: {key}")
    
    print(f"Событие {event_id} успешно обновлено.")

def edit_participant(event_id, participant_id, updates):
    if event_id not in events or participant_id not in events[event_id].get("participants", {}):
        print(f"Участник с ID {participant_id} в событии {event_id} не найден.")
        return
    
    for key, value in updates.items():
        if key in participant_schema and key in events[event_id]["participants"][participant_id]:
            events[event_id]["participants"][participant_id][key] = value
        else:
            print(f"Недопустимое поле для редактирования участника: {key}")
    
    print(f"Участник {participant_id} в событии {event_id} успешно обновлен.")

def edit_task(event_id, task_id, updates):
    if event_id not in events or task_id not in events[event_id].get("tasks", {}):
        print(f"Задача с ID {task_id} в событии {event_id} не найдена.")
        return
    
    for key, value in updates.items():
        if key in task_schema and key in events[event_id]["tasks"][task_id]:
            events[event_id]["tasks"][task_id][key] = value
        else:
            print(f"Недопустимое поле для редактирования задачи: {key}")
    
    print(f"Задача {task_id} в событии {event_id} успешно обновлена.")

def edit_schedule(event_id, slot_id, updates):
    if event_id not in events or slot_id not in events[event_id].get("schedule", {}):
        print(f"Временной слот {slot_id} в событии {event_id} не найден.")
        return
    
    for key, value in updates.items():
        if key in schedule_schema and key in events[event_id]["schedule"][slot_id]:
            events[event_id]["schedule"][slot_id][key] = value
        else:
            print(f"Недопустимое поле для редактирования расписания: {key}")
    
    print(f"Временной слот {slot_id} в событии {event_id} успешно обновлен.")
