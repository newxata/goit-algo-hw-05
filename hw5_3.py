'''не працює фільтр + немає винятків'''
'''треба шлях до логу якось прописати. функція load_logs, шлях: file_path'''


from sys import argv, exit
from pathlib import Path
from collections import Counter


def parse_log_line(line: str) -> dict:
    """Розбирає рядок з логу на компоненти: дата, час, рівень, повідомлення."""
    date, time, level, message = line.split(' ', maxsplit=3)
    return {'date': date, 'time': time, 'level': level, 'message': message}


# Перевірка: якщо шлях до логу не додано
if len(argv) != 2:
    print('Please provide a file path')
    exit()

file_path = Path(argv[1])

# Перевірка: якщо шлях до логу ссилається на папку
if file_path.is_dir():
    print(f'{file_path}  - is FOLDER and we don\'t work with it')
    exit()

# Перевірка: чи існує файл за вказаним шляхом
if not file_path.exists():
    print(f'{file_path}  - file at this path does not exist')
    exit()


def load_logs(file_path: str) -> list:
    """Відкриває лог, читає його, застосовує функцію parse_log_line, та зберігає результат в список."""
    logs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file: # Think about this ---- text.strip().split('\n') ----
            if line.strip():
                logs.append(parse_log_line(line.strip()))
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрація за рівнем логування. Отримуємо всі записи логу для певного рівня логування."""
    filter_level = list(filter(lambda item: item['level'] == level, logs))
    return filter_level


def count_logs_by_level(logs: list) -> dict:
    """Проходить по всім записам та підраховує кількість записів для кожного рівня логування."""
    counts = Counter(entry['level'] for entry in logs)
    return dict(counts)


def display_log_counts(counts: dict):
    """Виведення результатів в читабельній формі."""
    print('\nРівень логування | Кількість')
    print('-' * len('Рівень логування ') + '|' + '-' * len(' Кількість'))
    for level, count in counts.items():
        print(f'{level:<16} | {count}')


def main():
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    if len(argv) == 2:
        display_log_counts(counts)
    elif len(argv) == 3:
        display_log_counts(counts)
        filter_log = filter_logs_by_level(logs, level=argv[2])
        print(f'\nДеталі логів для рівня "{argv[2]}":')
        for entry in filter_log:
            print(f'{entry['date']} {entry['time']} - {entry['message']}')
    else:
        print('Please provide a file path')
    print('')


if __name__ == '__main__':
    main()
