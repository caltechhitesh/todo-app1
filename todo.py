import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a JSON file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("📜 No tasks found. Add one!")
        return
    print("\n📌 To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def remove_task(task_number):
    """Remove a task by its number."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"🗑️ Task removed: {removed_task}")
    else:
        print("❌ Invalid task number!")

if __name__ == "__main__":
    while True:
        print("\n1️⃣ Add Task | 2️⃣ View Tasks | 3️⃣ Remove Task | 4️⃣ Exit")
        choice = input("Select an option: ")

        if choice == "1":
            task = input("Enter your task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_num = int(input("Enter task number to remove: "))
            remove_task(task_num)
        elif choice == "4":
            print("🚀 Exiting To-Do List. Have a productive day!")
            break
        else:
            print("❌ Invalid choice! Try again.")

