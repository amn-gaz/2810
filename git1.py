import os
import subprocess
from datetime import datetime

class GitAutomation:
    def __init__(self, repo_path="."):
        self.repo_path = os.path.abspath(repo_path)
        os.chdir(self.repo_path)
        self.ensure_repo_initialized()

    def run_command(self, command):
        """Выполняет системную команду и возвращает вывод"""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Ошибка при выполнении '{command}':\n{result.stderr}")
        else:
            print(result.stdout.strip())
        return result

    def ensure_repo_initialized(self):
        """Проверяет, инициализирован ли Git-репозиторий, и если нет — выполняет git init"""
        if not os.path.exists(os.path.join(self.repo_path, ".git")):
            print("🪄 Репозиторий не найден. Выполняю git init...")
            self.run_command("git init")
        else:
            print("✅ Репозиторий уже инициализирован.")

    def add_all(self):
        """Добавляет все изменения"""
        print("➕ Добавляю изменения (git add .)...")
        self.run_command("git add .")

    def show_status(self):
        """Показывает текущее состояние репозитория"""
        print("\n📋 Текущее состояние (git status):")
        self.run_command("git status")
        print()

    def commit(self):
        """Перед коммитом показывает статус, затем выполняет git commit"""
        # Показываем git status перед коммитом
        self.show_status()

        # Запрашиваем подтверждение
        confirm = input("Продолжить коммит? (y/N): ").strip().lower()
        if confirm != "y":
            print("❌ Коммит отменён.")
            return

        # Создаём сообщение с днём недели
        weekday = datetime.now().strftime("%A")  # День недели, например 'Tuesday'
        message = input("Введите сообщение для коммита: ")
        full_message = f"{weekday} commit: {message}"
        print(f"💬 Коммит: {full_message}")
        self.run_command(f'git commit -m "{full_message}"')

    def push(self):
        """Отправляет изменения на удалённый репозиторий"""
        print("🚀 Отправка изменений (git push)...")
        result = self.run_command("git push")
        if "No configured push destination" in result.stderr:
            print("\n⚠️ У репозитория не настроен remote.\n"
                  "Добавьте его командой:\n"
                  "git remote add origin <URL>\n"
                  "и затем выполните:\n"
                  "git push -u origin master\n")

# ---------------------------
# Пример использования
# ---------------------------
if __name__ == "__main__":
    git_auto = GitAutomation()

    git_auto.add_all()
    git_auto.commit()
    git_auto.push()
