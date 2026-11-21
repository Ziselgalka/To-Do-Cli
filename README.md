# To-Do List CLI

A simple command-line to-do list written in Python. Tasks are sorted by priority and saved to a JSON file, so they are still there the next time you run the program.

## Features

- Add tasks with a priority: high, medium or low
- Tasks are kept sorted by priority (shown as `***`, `**`, `*`)
- Mark tasks as completed or uncompleted
- Delete tasks by number
- Automatic saving to `saved_data.json` after every change
- If the data file is corrupted, it is kept as `saved_data.json.corrupted` and the program starts with an empty list

## Requirements

Python 3.12 or newer, no external libraries.

## How to run

```bash
python main.py
```

## Example

```
1. [ ] *** Buy bread
2. [x] **  Finish dishes
3. [ ] *   Clean the desk
```

## What I practiced

- Functions, including passing a function as an argument
- Working with lists and dictionaries
- JSON serialization and file handling
- Exception handling (`FileNotFoundError`, `JSONDecodeError`)
- Refactoring repeated code into a single helper

PS: My first project