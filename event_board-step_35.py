# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: EventBoard
def get_next_action(event):
    """Returns a suggested next action based on the current event state."""
    if not event.get("tasks"):
        return "Create at least one task for this event."
    
    tasks = event["tasks"]
    urgent_tasks = [t for t in tasks if not t.get("done")]
    if urgent_tasks:
        return f"Complete the pending tasks: {', '.join(t['name'] for t in urgent_tasks)}"

    if not event.get("participants"):
        return "Add participants to this event."

    budget = event.get("budget", 0)
    spent = sum(p.get("spent", 0) for p in event["participants"])
    remaining_budget = budget - spent
    if remaining_budget < 0:
        return "Review spending — you've exceeded the budget."
    
    schedule_slots = len(event.get("schedule", []))
    max_participants = event.get("max_participants", 1)
    participant_count = len([p for p in event["participants"] if not p.get("done")])

    if participant_count < max_participants:
        return "Add more participants to reach the group size."

    if schedule_slots == 0:
        return "Set a schedule or timeline for this event."

    return f"Event {event['name']} is well-structured. Consider adding a description or notes."
