# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: EventBoard
def test_edge_cases():
    assert EventBoard().add_event("E1", "2025-12-31", 0, []).event_id == "E1"
    assert EventBoard().add_event("E2", "2026-01-01", 0, []).event_id == "E2"
    e = EventBoard().add_event("E3", "2025-06-15", 0, [])
    assert e.add_participant("P").participant_id is None
    assert e.add_participant(99).participant_id is None
    assert e.add_task("T", "desc", 0) and e.tasks[0].task_id == "T"
    assert e.add_task("", "", 0) is None
    e2 = EventBoard().add_event("E4", "2025-12-31", 0, [])
    e2.add_participant("P")
    assert e2.get_schedule("2025-12-31") == ["E4"]
    assert e2.get_schedule("2026-01-01") is None
    e3 = EventBoard().add_event("E5", "2025-07-01", 0, [])
    e3.add_participant("P").budget = -100
    assert e3.budget_total() == -100
    assert e3.get_report("2024") is None
