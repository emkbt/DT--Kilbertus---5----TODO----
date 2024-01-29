from datetime import datetime, timedelta

class Task:
    def __init__(self, description, due_date=None):
        # Task initialization with a description and an optional due date
        self.description = description
        self.due_date = due_date

class TodoList:
    def __init__(self):
        # TodoList initialization with an empty list of tasks
        self.tasks = []

    def add_task(self, task_description, due_date=None):
        # Adding a task to the TodoList
        new_task = Task(task_description, due_date)
        self.tasks.append(new_task)

    def delete_task(self, task_description):
        # Deleting a task from the TodoList by description
        for task in self.tasks:
            if task.description == task_description:
                self.tasks.remove(task)
                break

    def complete_task(self, task_description):
        # Marking a task as completed in the TodoList by description
        for task in self.tasks:
            if task.description == task_description:
                print(f"Completing task: {task.description}")
                break
        else:
            print(f"Task not found: {task_description}")

    def display_tasks(self):
        # Displaying all tasks in the TodoList with optional due dates
        print("Tasks:")
        for task in self.tasks:
            due_date_info = f" (Due Date: {task.due_date})" if task.due_date else ""
            print(f"- {task.description}{due_date_info}")

def main():
    # Main function for user interaction
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Adding a task with an optional due date
            task_description = input("Enter task description: ")
            due_date_str = input("Enter due date (optional, format: YYYY-MM-DD): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
            todo_list.add_task(task_description, due_date)
            
        elif choice == '2':
            # Deleting a task by description
            task_description = input("Enter task description to delete: ")
            todo_list.delete_task(task_description)
        elif choice == '3':
            # Completing a task by description
            task_description = input("Enter task description to complete: ")
            todo_list.complete_task(task_description)
        elif choice == '4':
            # Displaying all tasks
            todo_list.display_tasks()
        elif choice == '5':
            # Exiting the loop and ending the program
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Automatically calling the main function when the program is run
    main()
