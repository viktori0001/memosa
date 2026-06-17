# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: EventBoard
def load_initial_data(json_string):
    import json
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Валидация обязательных полей
        required_fields = ['events', 'participants', 'tasks']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Отсутствует поле {field}")
            
            if not isinstance(data[field], list):
                raise TypeError(f"Поле {field} должно быть списком")
        
        # Валидация структуры событий
        for event in data['events']:
            required_event_fields = ['id', 'name', 'date']
            for field in required_event_fields:
                if field not in event:
                    raise ValueError(f"В событии отсутствует поле {field}")
        
        # Валидация участников
        for participant in data['participants']:
            required_participant_fields = ['id', 'name']
            for field in required_participant_fields:
                if field not in participant:
                    raise ValueError(f"У участника отсутствует поле {field}")
        
        # Валидация задач
        for task in data['tasks']:
            required_task_fields = ['id', 'event_id', 'description']
            for field in required_task_fields:
                if field not in task:
                    raise ValueError(f"В задаче отсутствует поле {field}")
        
        return data
    
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return None

# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    initial_json = """
    {
      "events": [
        {"id": 1, "name": "Конференция", "date": "2024-12-01"},
        {"id": 2, "name": "Воркшоп", "date": "2024-12-15"}
      ],
      "participants": [
        {"id": 1, "name": "Алексей"},
        {"id": 2, "name": "Мария"}
      ],
      "tasks": [
        {"id": 1, "event_id": 1, "description": "Подготовить материалы"},
        {"id": 2, "event_id": 1, "description": "Организовать кофе-брейк"}
      ]
    }
    """
    
    loaded_data = load_initial_data(initial_json)
    if loaded_data:
        print("Данные успешно загружены!")
        print(f"Количество событий: {len(loaded_data['events'])}")
        print(f"Количество участников: {len(loaded_data['participants'])}")
        print(f"Количество задач: {len(loaded_data['tasks'])}")
    else:
        print("Не удалось загрузить данные.")
