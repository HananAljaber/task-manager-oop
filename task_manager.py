from task import Task
class TaskManager:

    def __init__(self,storage):
        self.storage =storage
        self.tasks =storage.load()






    def get_next_id(self):
        highest_id = 0

        for task in self.tasks:
            if task.id > highest_id:
                highest_id = task.id

        return highest_id + 1

    def add_task(self, title, priority="Medium"):
        title = title.strip()
        priority = priority.strip().capitalize()

        if title == "":
            return None

        if priority not in Task.VALID_PRIORITIES:
            return None

        new_task = Task(
            self.get_next_id(),
            title,
            priority
        )

        self.tasks.append(new_task)
        self.storage.save(self.tasks)
        return new_task

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
            return

        for task in self.tasks:
            print(task)

    def complete_task(self, task_id):
        task = self.find_task_by_id(task_id)

        if task is None:
            return False

        task.complete()
        self.storage.save(self.tasks)
        return True

    def delete_task(self, task_id):
        task = self.find_task_by_id(task_id)

        if task is None:
            return False

        self.tasks.remove(task)
        self.storage.save(self.tasks)
        return True

    def update_task(self, task_id, new_title):
        task = self.find_task_by_id(task_id)

        if task is None:
            return False

        updated = task.update_title(new_title)
        if not updated:
            return False

        self.storage.save(self.tasks)
        return True
    def search_tasks(self, search_text):
        search_text = search_text.strip().lower()

        if search_text == "":
            return []

        matching_tasks = []

        for task in self.tasks:
            if search_text in task.title.lower():
                matching_tasks.append(task)

        return matching_tasks


    def get_statistics(self):
        total = len(self.tasks)
        completed = 0

        for task in self.tasks:
            if task.completed:
                completed += 1

        not_completed = total - completed

        if total == 0:
            percentage = 0
        else:
            percentage = (completed / total) * 100

        return {
            "total": total,
            "completed": completed,
            "not_completed": not_completed,
            "percentage": percentage
        }


    def update_task_priority(self, task_id, new_priority):
        task = self.find_task_by_id(task_id)

        if task is None:
            return False

        updated = task.update_priority(new_priority)

        if not updated:
            return False

        self.storage.save(self.tasks)
        return True