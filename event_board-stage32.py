# === Stage 32: Добавь журнал действий пользователя ===
# Project: EventBoard
class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, action_type, description):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "type": action_type,
            "description": description
        }
        self._entries.append(entry)
        return len(self._entries)

    @property
    def entries(self):
        return list(self._entries)


class EventBoard:
    def __init__(self):
        self.events = {}
        self.participants = {}
        self.tasks = []
        self.budget = 0.0
        self.schedule = {}
        self.action_log = ActionLog()

    def add_event(self, name, date=None, budget=0.0):
        if name in self.events:
            return False
        event = {"name": name, "date": date, "budget": budget}
        self.events[name] = event
        if budget > 0:
            self.budget += budget
        self.action_log.log("add_event", f"Создан событие {name}")
        return True

    def add_participant(self, name):
        if name in self.participants:
            return False
        self.participants[name] = {"tasks": []}
        self.action_log.log("add_participant", name)
        return True

    def assign_task(self, event_name, participant, task_desc):
        if event_name not in self.events or participant not in self.participants:
            return False
        self.participants[participant]["tasks"].append(task_desc)
        self.action_log.log("assign_task", f"{participant} -> {event_name}: {task_desc}")
        return True

    def set_schedule(self, event_name, time_slot):
        if event_name not in self.events:
            return False
        self.schedule[event_name] = time_slot
        self.action_log.log("set_schedule", f"{event_name} -> {time_slot}")
        return True


board = EventBoard()
