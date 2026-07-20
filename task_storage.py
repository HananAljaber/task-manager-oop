import json
from task import Task

class TaskStorage:

    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name

    def save(self, tasks):
        tasks_data = []

        for task in tasks:
            task_data = {
                "id": task.id,
                "title": task.title,
                "completed": task.completed,"priority": task.priority
            }

            tasks_data.append(task_data)

        with open(
            self.file_name,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                tasks_data,
                file,
                ensure_ascii=False,
                indent=4
            )

    def load(self):
        try:
            with open(
                self.file_name,
                "r",
                encoding="utf-8"
            ) as file:
                tasks_data = json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []

        tasks = []

        for task_data in tasks_data:
            task = Task(
                task_data["id"],
                task_data["title"],
                    task_data.get("priority", "Medium"),
    task_data.get("completed", False)
            )

            tasks.append(task)

        return tasks

