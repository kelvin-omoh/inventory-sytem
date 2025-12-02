# 📝 Simple Command-Line Todo List

A lightweight, beginner-friendly Python command-line application for managing your daily tasks. No database required – all tasks are stored in a simple text file!

## ✨ Features

- ✅ **Add tasks** – Quickly add new items to your todo list
- ✅ **View tasks** – See all your current tasks in a numbered list
- ✅ **Complete tasks** – Mark tasks as done and remove them from the list
- ✅ **Persistent storage** – Tasks are saved to a text file automatically
- ✅ **Simple & fast** – No installation required, just Python 3

## 🚀 Quick Start

### Prerequisites

- Python 3.x installed on your system
- A terminal or command prompt

### Installation

1. Download or clone this repository
2. Navigate to the project directory:
   ```bash
   cd "todo list"
   ```

That's it! No dependencies to install.

## 📖 Usage

### Basic Syntax

```bash
python3 todo.py <filename> [command] [arguments]
```

### View All Tasks

Display your current todo list:

```bash
python3 todo.py tasks.txt
```

**Example output:**
```
Your Todo List:
----------------------------------------
 1. Buy milk
 2. Learn Python
 3. Go shopping
----------------------------------------
```

If your list is empty, you'll see:
```
Your todo list is empty! 🎉
```

### Add a New Task

Add a task to your list:

```bash
python3 todo.py tasks.txt add "Your task description"
```

**Examples:**
```bash
python3 todo.py tasks.txt add "Buy milk"
python3 todo.py tasks.txt add "Call mom"
python3 todo.py tasks.txt add "Finish Python project"
```

**Note:** Always use quotes around your task description, especially if it contains spaces.

### Mark a Task as Done

Remove a completed task by its number:

```bash
python3 todo.py tasks.txt done <task_number>
```

**Examples:**
```bash
python3 todo.py tasks.txt done 1    # Removes task #1
python3 todo.py tasks.txt done 3    # Removes task #3
```

## 💡 Complete Workflow Example

Here's a typical workflow:

```bash
# Start with an empty list
$ python3 todo.py tasks.txt
Your todo list is empty! 🎉

# Add some tasks
$ python3 todo.py tasks.txt add "Buy groceries"
Added: Buy groceries

Your Todo List:
----------------------------------------
 1. Buy groceries
----------------------------------------

$ python3 todo.py tasks.txt add "Write README"
Added: Write README

Your Todo List:
----------------------------------------
 1. Buy groceries
 2. Write README
----------------------------------------

$ python3 todo.py tasks.txt add "Exercise for 30 minutes"
Added: Exercise for 30 minutes

Your Todo List:
----------------------------------------
 1. Buy groceries
 2. Write README
 3. Exercise for 30 minutes
----------------------------------------

# Complete a task
$ python3 todo.py tasks.txt done 2
Completed and removed: Write README

Your Todo List:
----------------------------------------
 1. Buy groceries
 2. Exercise for 30 minutes
----------------------------------------

# View your updated list
$ python3 todo.py tasks.txt

Your Todo List:
----------------------------------------
 1. Buy groceries
 2. Exercise for 30 minutes
----------------------------------------
```

## 📁 File Structure

```
todo list/
├── todo.py       # Main application script
├── tasks.txt     # Your todo list data (auto-created)
└── README.md     # This file
```

## 🔧 How It Works

1. **Storage**: Tasks are stored in a plain text file (e.g., `tasks.txt`), with one task per line
2. **Auto-creation**: If the file doesn't exist, it's automatically created when you first run the program
3. **Persistence**: All changes are immediately saved to the file
4. **Simplicity**: No database, no complex setup – just a text file and Python

## ⚠️ Error Handling

The application includes helpful error messages:

- **Missing filename**: Reminds you to specify a file
- **Invalid command**: Shows usage instructions
- **Invalid task number**: Alerts you if the task number doesn't exist
- **Non-numeric input**: Catches invalid input for the `done` command

## 🎯 Use Cases

Perfect for:
- Daily task management
- Learning Python file I/O and command-line arguments
- Quick personal todo lists
- Project task tracking
- Shopping lists
- Study schedules

## 🛠️ Customization Ideas

Want to extend this project? Here are some ideas:

- Add task priorities (high, medium, low)
- Add due dates for tasks
- Implement task editing
- Add categories or tags
- Create a search function
- Add task completion statistics
- Export to CSV or JSON format

## 📝 Notes

- Task numbers change when you complete tasks (the list renumbers automatically)
- You can use different filenames for different todo lists (e.g., `work.txt`, `personal.txt`, `shopping.txt`)
- The text file uses UTF-8 encoding, so you can use emojis and special characters in your tasks! 🎉

## 🤝 Contributing

Feel free to fork this project and add your own features! Some suggestions:
- Add color output using `colorama`
- Create a GUI version with `tkinter`
- Add task timestamps
- Implement task archiving instead of deletion

## 📄 License

This is a simple educational project. Feel free to use, modify, and distribute as you wish!

---

**Happy task managing! 📋✨**
