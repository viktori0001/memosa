# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: EventBoard
import time as _time


class EventLog:
    """Откат последних действий в истории событий."""

    def __init__(self):
        self.history = []

    @property
    def last(self):
        return self.history[-1] if self.history else None

    def undo_last(self) -> dict | None:
        """Меняет последнее событие на противоположное. Возвращает удалённый запис."""
        entry = self.last
        if not entry:
            return None
        op, args, ts = entry
        new_entry = (op + "_undo", args, _time.time())
        self.history[-1] = new_entry
        return entry

    def redo_last(self) -> dict | None:
        """Отменяет откат — возвращает событие в исходное состояние."""
        entry = self.last
        if not entry or entry[0].endswith("_undo"):
            return None
        op, args, ts = entry
        new_entry = (op + "_redo", args, _time.time())
        self.history[-1] = new_entry
        return entry

    def log(self, action: str, params: dict) -> dict:
        """Записывает действие и возвращает его."""
        entry = {"action": action, "params": params, "timestamp": _time.time()}
        self.history.append(entry)
        return entry


# Тест отката через EventLog.
log = EventLog()
log.log("add_task", {"name": "Купить билет"})
print(log.last["action"], log.last["params"])

log.undo_last()
print(log.last["action"])  # add_task_undo

log.redo_last()
print(log.last["action"])  # add_task_redo
