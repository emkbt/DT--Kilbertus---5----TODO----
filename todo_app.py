from datetime import datetime

class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description, due_date=None):
        new_task = Task(task_description, due_date)
        self.tasks.append(new_task)

    def delete_task(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                self.tasks.remove(task)
                break

    def complete_task(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                print(f"Completing task: {task.description}")
                break
        else:
            print(f"Task not found: {task_description}")

    def display_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            due_date_str = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
            print(f"{task.description} - {due_date_str}")
            

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            due_date_str = input("Enter due date (optional, format: YYYY-MM-DD): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
            todo_list.add_task(task_description, due_date)
            
        elif choice == '2':
            task_description = input("Enter task description to delete: ")
            todo_list.delete_task(task_description)
        elif choice == '3':
            task_description = input("Enter task description to complete: ")
            todo_list.complete_task(task_description)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
