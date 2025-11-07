import os
import subprocess
from datetime import datetime

class GitAutomation:
    def __init__(self, repo_path="."):
        # Указываем путь к репозиторию
        self.repo_path = os.path.abspath(repo_path)
        # Переходим в этот путь
        os.chdir(self.repo_path)
        # Проверяем, есть ли .git, если нет — создаём
        self.ensure_repo_initialized()

    def run_command(self, command):
        """Выполняет системную команду"""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # Если ошибка — выводим stderr, иначе stdout
        if result.returncode != 0:
            print(f"Ошибка при выполнении '{command}':\n{result.stderr}")
        else:
            print(result.stdout.strip())
        return result

    def ensure_repo_initialized(self):
        """Проверяет, инициализирован ли репозиторий"""
        if not os.path.exists(os.path.join(self.repo_path, ".git")):
            print("Репозиторий не найден. Выполняю git init...")
            self.run_command("git init")  # создаём новый репозиторий
        else:
            print(" Репозиторий уже инициализирован.")

    def add_all(self):
        """Добавляет все изменения"""
        print(" Добавляю изменения (git add .)...")
        self.run_command("git add .")

    def show_status(self):
        """Показывает текущее состояние репозитория"""
        print("\n Текущее состояние (git status):")
        self.run_command("git status")
        print()

    def commit(self):
        """Создаёт коммит"""
        # Показываем статус перед коммитом
        self.show_status()

        # Спрашиваем подтверждение
        confirm = input("Продолжить коммит? (y/N): ").strip().lower()
        if confirm != "y":
            print(" Коммит отменён.")
            return

        # Получаем день недели
        weekday = datetime.now().strftime("%A")
        # Просим ввести сообщение
        message = input("Введите сообщение для коммита: ")
        # Полное сообщение
        full_message = f"{weekday} commit: {message}"
        print(f" Коммит: {full_message}")
        # Выполняем git commit
        self.run_command(f'git commit -m "{full_message}"')

    def push(self):
        """Отправляет изменения на GitHub"""
        print(" Отправка изменений (git push)...")
        result = self.run_command("git push")
        # Если нет удалённого репозитория — подсказываем как добавить
        if "No configured push destination" in result.stderr:
            print("\n У репозитория не настроен remote.\n"
                  "Добавьте его командой:\n"
                  "git remote add origin <URL>\n"
                  "и затем выполните:\n"
                  "git push -u origin master\n")

# ---------------------------
# Пример использования
# ---------------------------
if __name__ == "__main__":
    git_auto = GitAutomation()  # создаём объект

    git_auto.add_all()   # добавляем все файлы
    git_auto.commit()    # делаем коммит
    git_auto.push()      # отправляем на GitHub
