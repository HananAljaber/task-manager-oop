class Task:

    VALID_PRIORITIES = ["Low", "Medium", "High"]

    def __init__(
        self,
        task_id,
        title,
        priority="Medium",
        completed=False
    ):
        self.id = task_id
        self.title = title.strip()
        self.priority = priority
        self.completed = completed

    def complete(self):
        self.completed = True

    def update_title(self, new_title):
        new_title = new_title.strip()

        if new_title == "":
            return False

        self.title = new_title
        return True

    def update_priority(self, new_priority):
        new_priority = new_priority.strip().capitalize()

        if new_priority not in self.VALID_PRIORITIES:
            return False

        self.priority = new_priority
        return True

    def __str__(self):
        if self.completed:
            status = "Completed"
        else:
            status = "Not Completed"

        return (
            f"[{self.id}] {self.title} "
            f"- Priority: {self.priority} "
            f"- Status: {status}"
        )