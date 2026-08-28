# === Stage 43: Добавь пагинацию длинных списков ===
# Project: EventBoard
def paginate(items, page_size=10):
    """Compact pagination that yields slices of a list."""
    if not items:
        return
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]
