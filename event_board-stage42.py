# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: EventBoard
import sys

def colorize(text, color_code, reset=''):
    if sys.stdout.isatty():
        return f'{color_code}{text}{reset}'
    return text

def print_header(title, color_code='\033[1;36'):
    reset = '\033[0m'
    print(colorize(f'\n{color_code}┌─────────────────────────────────────────{reset}', color_code))
    print(colorize(f'{color_code}│ {title}{reset}', color_code))
    print(colorize(f'{color_code}└─────────────────────────────────────────{reset}', color_code))

def print_section(title, color_code='\033[1;32'):
    reset = '\033[0m'
    print(colorize(f'\n{color_code}═══ {title} ═══{reset}', color_code))

def print_success(msg, color_code='\033[1;32'):
    reset = '\033[0m'
    print(colorize(f'{color_code}✓ {msg}{reset}', color_code))

def print_error(msg, color_code='\033[1;31'):
    reset = '\033[0m'
    print(colorize(f'{color_code}✗ {msg}{reset}', color_code))

def print_warning(msg, color_code='\033[1;33'):
    reset = '\033[0m'
    print(colorize(f'{color_code}⚠ {msg}{reset}', color_code))

def print_info(msg, color_code='\033[1;34'):
    reset = '\033[0m'
    print(colorize(f'{color_code}i {msg}{reset}', color_code))

def print_budget_used(current, total, color_code='\033[1;33'):
    reset = '\033[0m'
    pct = current / total * 100 if total else 0
    if pct > 80:
        color_code = '\033[1;31'
    elif pct > 50:
        color_code = '\033[1;33'
    print(colorize(f'Использовано: {color_code}{current:.1f} / {total:.1f} ({pct:.1f}%) {reset}', color_code))

def print_task_item(name, status, due, color_code='\033[1;32'):
    reset = '\033[0m'
    if status == 'done':
        color_code = '\033[1;32'
    elif status == 'overdue':
        color_code = '\033[1;31'
    elif status == 'pending':
        color_code = '\033[1;33'
    print(colorize(f'{color_code}• {name} [{status.upper()}] {reset}', color_code))
    print(colorize(f'  {color_code}⏰ До: {due}{reset}', color_code))
