import sys
import json
import string
import random
import hashlib
from datetime import datetime, timedelta

db_file = "users.json"
todo_file = "todo.json"
logged = False

db:list[dict] = json.load(open(db_file, "r"))
todo:list[dict] = json.load(open(todo_file, 'r'))

def gen_api(length=32) -> string:
    characters = string.ascii_letters + string.digits + '!@#$%^&*()_-+=<>?'
    api_key = ''.join(random.choice(characters) for _ in range(length))
    return api_key

def md5_hash(input_string) -> string:
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))

    return md5_hash.hexdigest()

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
        todo.append({"description": str(task_description), "due_date": due_date, "completed": False})
        json.dump(todo, open(todo_file, 'w'))

    def delete_task(self, task_description):
        # Deleting a task from the TodoList by description
        for index,task in enumerate(todo):
            if task['description'] == task_description:
                todo.pop(index)
                json.dump(todo, open(todo_file, 'w'))
                break

    def complete_task(self, task_description):
        # Marking a task as completed in the TodoList by description
        success = False
        for index,task in enumerate(todo):
            if task['description'] == task_description:
                print(f"Completing task: {task['description']}")
                todo[index]['completed'] = True
                json.dump(todo, open(todo_file, 'w'))
                success = True
                break
        if not success:
            print(f"Task not found: {task_description}")

    def display_tasks(self):
        # Displaying all tasks in the TodoList with optional due dates
        todo = json.load(open(todo_file, 'r'))
        print("Tasks:")
        for task in todo:
            due_date_str = task['due_date'] if task['due_date'] else "No due date"
            print(f"{task['description']} - {due_date_str}")
            

def main():
    # Main function for user interaction
    todo_list = TodoList()
    logged = False
    while True:
        if not logged:
            print("\n1. Login")
            print("2. Register")
            
            login_choice = input("Enter your choice: ")
            logged = False
            
            if login_choice=="1":
                username = input("Username: ")
                password = input("Password: ")
                for i in db:
                    if i['username'] == username:
                        if i['password'] == password:
                            logged = True
                            print(f"Successfully logged in as {username}")
                
            elif login_choice=="2":
                username = input("Username: ")
                password = input("Password: ")
                db.append({"username": username, "password": password, "api_key": md5_hash(gen_api())})
                json.dump(db, open(db_file, 'w'))
                logged = True
            
            if not logged:
                print("Incorrect credentials.")
                sys.exit(1)
        
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
