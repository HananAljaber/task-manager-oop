
from task_manager import TaskManager
from task_storage import TaskStorage
def get_valid_task_id(message):
    while True:
        try:
            return int(input(message).strip())
        except ValueError:
            print("Please enter a valid number.")
def show_menu():
    print("\n=== Task Manager ===")
    print("1- Add Task")
    print("2- Show Tasks")
    print("3- Complete Task")
    print("4- Delete Task")
    print("5- Update Task")
    print("6- Update Priority")
    print("7- Search Tasks")
    print("8- Show Statistics")
    print("9- Exit")

def main():
    storage = TaskStorage()
    manager = TaskManager(storage)

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":

            title = input("Enter task title: ").strip()

            priority = input(
                "Enter priority (Low/Medium/High): "
            ).strip()

            task = manager.add_task(title, priority)

            if task is None:
                print("Invalid title or priority.")
                continue

  
            print(f"Task added: {task.title}")

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            task_id = get_valid_task_id("Enter task ID: ")

            if manager.complete_task(task_id):
                print("Task completed.")
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = get_valid_task_id(
                "Enter task ID to delete: "
            )

            if manager.delete_task(task_id):
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == "5":
            task_id = get_valid_task_id(
                "Enter task ID to update: "
            )

            new_title = input(
                "Enter the new task title: "
            ).strip()

            if manager.update_task(task_id, new_title):
                print("Task updated.")
            else:
                print("Task not found or title is invalid.")

        elif choice == "6":
            task_id = get_valid_task_id(
                "Enter task ID to update priority: "
            )

            new_priority = input(
                "Enter new priority (Low/Medium/High): "
            ).strip()

            if manager.update_task_priority(
                task_id,
                new_priority
            ):
                print("Task priority updated.")
            else:
                print("Task not found or priority is invalid.")
        elif choice == "7":
            search_text = input("Enter title to search: ").strip()
            matching_tasks = manager.search_tasks(search_text)

            if len(matching_tasks) == 0:
                print("No matching tasks found.")
                continue
            for task in matching_tasks:
                print(task)
            
        elif choice == "8":
            statistics = manager.get_statistics()

            print("\n=== Task Statistics ===")
            print(f"Total: {statistics['total']}")
            print(f"Completed: {statistics['completed']}")
            print(f"Not completed: {statistics['not_completed']}")
            print(f"Completion: {statistics['percentage']:.1f}%")
        elif choice == "9":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()