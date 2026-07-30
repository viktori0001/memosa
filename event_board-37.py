# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: EventBoard
import unittest


class TestEventBoard(unittest.TestCase):
    def setUp(self):
        from event_board import EventBoard, Participant, Task, ScheduleSlot

        self.board = EventBoard()
        self.participant1 = Participant(name="Alice", role="organizer")
        self.participant2 = Participant(name="Bob", role="volunteer")
        self.task1 = Task(title="Setup stage", assignee=self.participant1)
        self.slot = ScheduleSlot(date="2026-05-01", hour=14, location="Hall A")

    def test_board_creation(self):
        self.assertIsNotNone(self.board)

    def test_add_participant(self):
        self.assertEqual(len(self.board.participants), 1)
        self.assertIn(self.participant1, self.board.participants)

    def test_add_task(self):
        self.board.add_task(self.task1)
        self.assertEqual(len(self.board.tasks), 1)

    def test_add_schedule_slot(self):
        self.board.add_slot(self.slot)
        self.assertEqual(len(self.board.slots), 1)

    def test_budget_tracking(self):
        budget = {"total": 500, "spent": 200}
        self.board.set_budget(budget)
        spent_more = 300
        result = self.board.track_expense(spent_more)
        self.assertEqual(result["remaining"], -100)

    def test_add_participant_invalid_role(self):
        try:
            Participant(name="Eve", role="unknown")
            self.fail("Should raise ValueError for invalid role")
        except ValueError:
            pass


if __name__ == "__main__":
    unittest.main()
