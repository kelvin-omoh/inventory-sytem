#!/usr/bin/env python3
"""
Simple Command-Line Todo List
--------------------------------
Usage examples:
    python3 todo.py tasks.txt                     # show all tasks
    python3 todo.py tasks.txt add "Buy milk"      # add a new task
    python3 todo.py tasks.txt done 3              # remove task #3
"""

import sys          # we need this to read command-line arguments
import os           # to check if file exists and to work with the file system


# ------------------------------------------------------------------
# Helper function: show how to use the program (when something is wrong)
# ------------------------------------------------------------------
def print_usage():
    print("Usage:")
    print("  python3 todo.py <filename>                     # show tasks")
    print("  python3 todo.py <filename> add \"Task text\"    # add a task")
    print("  python3 todo.py <filename> done <number>       # remove a task")


# ------------------------------------------------------------------
# Step 1: Make sure the user gave us at least the filename
# ------------------------------------------------------------------
if len(sys.argv) < 2:
    print("Error: You must give the name of the todo file!")
    print_usage()
    sys.exit(1)                     # stop the program with an error code

filename = sys.argv[1]              # the first argument is the file name

# If the file does not exist yet, create an empty one
if not os.path.exists(filename):
    print(f"File '{filename}' not found → creating a new empty todo list.")
    open(filename, 'w').close()     # creates an empty file


# ------------------------------------------------------------------
# Step 2: Read all tasks from the file into a Python list
# ------------------------------------------------------------------
def load_tasks():
    tasks = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()                 # remove \n and extra spaces
            if line:                            # ignore empty lines
                tasks.append(line)
    return tasks


# ------------------------------------------------------------------
# Step 3: Save the list of tasks back to the file
# ------------------------------------------------------------------
def save_tasks(tasks):
    with open(filename, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')


# ------------------------------------------------------------------
# Step 4: Show the current todo list (nice numbered output)
# ------------------------------------------------------------------
def show_tasks(tasks):
    if not tasks:
        print("Your todo list is empty! 🎉")
    else:
        print("\nYour Todo List:")
        print("-" * 40)
        for i, task in enumerate(tasks, start=1):
            print(f"{i:2}. {task}")
        print("-" * 40)


# ------------------------------------------------------------------
# Main program starts here
# ------------------------------------------------------------------
def main():
    # Load current tasks
    tasks = load_tasks()

    # If the user only gave the filename → just show the list and exit
    if len(sys.argv) == 2:
        show_tasks(tasks)
        return

    # Otherwise, look at the second word (command)
    command = sys.argv[2].lower()

    # --------------------- ADD A NEW TASK ---------------------
    if command == "add" and len(sys.argv) >= 4:
        new_task = sys.argv[3]
        # If the user wrote multiple words, join the rest too
        if len(sys.argv) > 4:
            new_task = " ".join(sys.argv[3:])
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Added: {new_task}")
        show_tasks(tasks)

    # --------------------- MARK A TASK AS DONE ---------------------
    elif command == "done" and len(sys.argv) == 4:
        try:
            task_number = int(sys.argv[3])      # convert string → number
            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)   # remove from list
                save_tasks(tasks)
                print(f"Completed and removed: {removed}")
                show_tasks(tasks)
            else:
                print("Error: There is no task with that number.")
        except ValueError:
            print("Error: Please give a valid number after 'done'.")

    # --------------------- UNKNOWN COMMAND ---------------------
    else:
        print("I didn't understand that command.")
        print_usage()


# ------------------------------------------------------------------
# Run the program only when the file is executed directly
# ------------------------------------------------------------------
if __name__ == "__main__":
    main()
