# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: EventBoard
def dry_run(operation, payload, state):
    """Execute operation in dry-run mode. If the operation is marked as dry-run,
    perform it on a copy of the state and return the dry-run result without
    modifying the actual state. Otherwise, execute normally."""
    dry_run_mode = state.get("_dry_run", False)
    if dry_run_mode:
        import copy
        state_copy = copy.deepcopy(state)
        result = operation(state_copy, payload)
        state_copy["_dry_run"] = False
        return result, state_copy
    else:
        return operation(state, payload)
