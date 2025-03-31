class Task:
    def __init__(self, description, deadlines, status=False):
        # Инициализация отдельной задачи
        self.description = description
        self.deadlines = deadlines
        self.status = status

class TaskManager():
    def __init__(self):
        self.tasks = []

    def adding(self, description, deadlines, status=False):
        new_task = Task(description, deadlines, status)
        self.tasks.append(new_task)
        print(f"Задача добавлена: {description}! Срок выполнения до: {deadlines}")

    def completed(self, task):
        task.status = True

    def mark_task(self, description):
        for task in self.tasks:
            if task.description == description and not task.status:
                self.completed(task)
                print(f"Задача {description} выполнена")
                return
        print(f"Задача {description} не найдена или уже выполнена")

    def tasks_list(self):
        current_tasks = [task for task in self.tasks if not task.status]
        if not current_tasks:
            print("Нет текущих задач.")
        else:
            print("Текущие задачи (не выполненные):")
            for task in current_tasks:
                print(f"- {task.description} (до {task.deadlines})")



tm = TaskManager()
tm.adding("Купить молока", "02.04.2025")
tm.adding("Прочитать книгу", "10.04.2025")
tm.adding("Просмотреть урок", "05.04.2025")

tm.tasks_list()

tm.mark_task("Купить молока")

tm.tasks_list()