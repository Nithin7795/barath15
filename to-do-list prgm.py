import sys

# Define a class for the To-Do List
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]["task"]
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Updated task {task_number}: {old_task} to {new_task}")
        else:
            print("Invalid task number.")

    def mark_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Marked task {task_number} as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task description: ")
            todo_list.update_task(task_number, new_task)
        elif choice == "4":
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == "5":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "6":
            print("Exiting the To-Do List application.")
            sys.exit()
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
