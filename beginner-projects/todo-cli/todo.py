import json
import os

FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks! You're all caught up.")
        return
    for i, task in enumerate(tasks):
        status = '✔️' if task['done'] else '❌'
        print(f"{i+1}. {task['title']} [{status}]")

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]

def main():
    tasks = load_tasks()

    while True:
        print("\n1. View\n2. Add\n3. Complete\n4. Delete\n5. Exit")
        choice = input("Choose: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            title = input("Task: ")
            add_task(tasks, title)
        elif choice == '3':
            idx = int(input("Task number to complete: ")) - 1
            complete_task(tasks, idx)
        elif choice == '4':
            idx = int(input("Task number to delete: ")) - 1
            delete_task(tasks, idx)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
