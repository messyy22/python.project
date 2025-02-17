---

# To-Do List Application

This is a simple command-line To-Do List application written in Python. It allows users to:

- View tasks
- Add new tasks
- Remove tasks
- Save tasks to a file and load them back on startup

## Features

1. **View Tasks**: Display all the tasks saved in the list.
2. **Add Task**: Allows users to add a new task to the list.
3. **Remove Task**: Users can remove a task by entering its number.
4. **Save Tasks**: All tasks are saved to a file (`tasks.txt` by default) to persist between sessions.

## Requirements

- Python 3.x

## Files

- `tasks.txt`: A text file where tasks are saved and loaded from (if it exists).

## How to Run

1. Clone the repository or download the script file.
2. Make sure Python 3 is installed on your machine.
3. Open a terminal and navigate to the directory where the script is located.
4. Run the script using:

   ```bash
   python todo_list.py
   ```

5. The application will display a menu to interact with the To-Do list.

## Functions

### `load_tasks(filename="tasks.txt")`

- Loads tasks from a file (`tasks.txt` by default).
- Returns an empty list if the file doesn't exist.

### `save_tasks(filename="tasks.txt")`

- Saves the current tasks to a file.

### `view_tasks()`

- Displays the list of all tasks.

### `add_task()`

- Prompts the user to add a new task to the list.

### `remove_task()`

- Prompts the user to remove a task by selecting its number.

### `main()`

- The main function that runs the application, displaying the menu and accepting user inputs.

## Notes

- Tasks are stored in memory during the session and will be saved to `tasks.txt` when exiting.
- If `tasks.txt` is missing, the program will create it once tasks are saved.

---
