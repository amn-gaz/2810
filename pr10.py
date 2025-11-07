import subprocess
import sys
import os

# Настраиваем вывод UTF-8 для Windows
sys.stdout.reconfigure(encoding='utf-8')

# Выполняем команду git status в коротком формате
result = subprocess.run(
    ["git", "status", "--porcelain"],
    capture_output=True, text=True
)

if result.returncode != 0:
    print("Ошибка при выполнении git status:")
    print(result.stderr)
else:
    lines = result.stdout.strip().splitlines()
    if not lines:
        print("Нет изменённых файлов.")
    else:
        print("Изменённые .py файлы:")
        for line in lines:
            status = line[:2].strip()      # статус (M, A, D, ??)
            filename = line[3:].strip()    # имя файла

            # Пропускаем неотслеживаемые файлы
            if status == "??":
                continue

            # Показываем только .py файлы
            if filename.endswith(".py"):
                print(f"{status}: {filename}")
