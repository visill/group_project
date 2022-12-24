import sys


def is_migration():
    # Проверка аргументов командной строки на наличие миграции
    return "makemigrations" in sys.argv or "migrate" in sys.argv
