import os

tasks = []

def load_tasks(filename="tasks.txt"):
    """Load tasks from a file if it exists."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks(filename="tasks.txt"):
    """Save tasks to a file."""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print(f"Tasks saved to '{filename}'.")

def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    """Add a new task."""
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    """Remove a task by its number."""
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number you want to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the application."""
    global tasks
    tasks = load_tasks() 

    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save and Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            save_tasks()
            print("\nExiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if _name_ == "_main_":
    main()
