# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: EventBoard
APP_CONFIG = {
    "app_name": "EventBoard",
    "version": 29,
    "max_events_per_day": 10,
    "default_budget_currency": "USD",
    "budget_warning_threshold_pct": 80,
    "task_priority_levels": ["critical", "high", "normal", "low"],
    "notification_channels": ["console", "email"],
    "date_format": "%Y-%m-%d",
    "time_format": "%H:%M",
}
