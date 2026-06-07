# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: EventBoard
class EventBoard:
    def __init__(self):
        self.events = []
        self.participants = {}
        self.tasks = []
        self.budgets = {}
        self.schedule = []

    def add_event(self, name, date, budget=None):
        event_id = len(self.events) + 1
        event = {
            "id": event_id,
            "name": name,
            "date": date,
            "budget": budget if budget else 0
        }
        self.events.append(event)
        if budget:
            self.budgets[event_id] = budget
        return event

    def add_participant(self, event_id, name):
        if not self.participants.get(event_id):
            self.participants[event_id] = []
        self.participants[event_id].append(name)

    def add_task(self, event_id, description, deadline=None):
        task_id = len(self.tasks) + 1
        task = {
            "id": task_id,
            "event_id": event_id,
            "description": description,
            "deadline": deadline
        }
        self.tasks.append(task)

    def add_schedule_item(self, event_id, time_slot):
        item = {
            "event_id": event_id,
            "time_slot": time_slot
        }
        self.schedule.append(item)
