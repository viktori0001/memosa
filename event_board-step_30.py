# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: EventBoard
class UserProfile:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def __repr__(self):
        return f"<UserProfile {self.name} ({self.role})>"


profiles_store = []


def add_profile(name, role):
    profiles_store.append(UserProfile(name, role))
    print(f"Профиль добавлен: {name} — роль: {role}")


def list_profiles():
    if not profiles_store:
        print("Список профилей пуст.")
        return
    for i, p in enumerate(profiles_store):
        print(f"{i+1}. {p.name} ({p.role})")


add_profile("Анна", "организатор")
list_profiles()
