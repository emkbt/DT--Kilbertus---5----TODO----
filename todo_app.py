class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def complete_task(self, task):
        if task in self.tasks:
            print(f"Completing task: {task}")
        else:
            print(f"Task not found: {task}")

    def display_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            print(f"- {task}")

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
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to delete: ")
            todo_list.delete_task(task)
        elif choice == '3':
            task = input("Enter task to complete: ")
            todo_list.complete_task(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()