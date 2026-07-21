# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: EventBoard
def switch_active_profile(event_manager, new_email):
    """Переключить активный пользовательский профиль по email."""
    for profile in event_manager.profiles:
        if profile["email"] == new_email:
            event_manager.active_profile = profile
            print(f"Активный профиль переключен на {new_email}")
            return True
    print(f"Профиль с email={new_email} не найден")
    return False
