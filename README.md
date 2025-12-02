# 📝 Simple Command-Line Todo List

A simple Python command-line application for managing your tasks.

## Files

- **todo.py** - Main application script
- **tasks.txt** - Text file where your tasks are stored

## Usage

### View all tasks
```bash
python3 todo.py tasks.txt
```

### Add a task
```bash
python3 todo.py tasks.txt add "Your task here"
```

### Mark a task as done (removes it)
```bash
python3 todo.py tasks.txt done 1
```

## Example

```bash
# Add tasks
python3 todo.py tasks.txt add "Buy milk"
python3 todo.py tasks.txt add "Learn Python"

# View tasks
python3 todo.py tasks.txt

# Complete task #1
python3 todo.py tasks.txt done 1
```

## Author

Created by **Ifeoluwa Afolabi**
