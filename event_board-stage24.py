# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: EventBoard
def print_entry(self):
        """Print a compact summary of one event entry."""
        e = self.entries[-1] if self.entries else None
        if not e:
            return
        print(f"\n{'='*40}")
        print("  Event Board — Latest Entry")
        print(f"{'='*40}")
        print(f"  Title     : {e.title}")
        print(f"  Date      : {e.date.strftime('%Y-%m-%d') if e.date else 'N/A'}")
        print(f"  Budget    : ${e.budget:,.2f} / {e.funds:,.2f}")
        print(f"  Status    : {'✅' if e.status == 'done' else '🔵' if e.status == 'planned' else '⚠️'}")
        print()

        # Participants summary
        p_sum = sum(p.hours for p in e.participants)
        print("  Attendees:")
        for i, p in enumerate(e.participants, 1):
            tag = "✓" if p.confirmed else "-"
            print(f"    {i}. {p.name} — {tag}, {p.role or 'attendee'}, {p.hours:.1f}h")

        # Tasks summary
        t_sum = sum(t.status == 'done' for t in e.tasks) / len(e.tasks) if e.tasks else 0
        print(f"  Tasks     : {t_sum:.0%} done ({e.tasks[0].status if e.tasks else 'none'})")

        # Notes
        if e.notes:
            print(f"  Note      : {e.notes}")
