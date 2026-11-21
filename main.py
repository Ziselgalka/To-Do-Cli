import json
import os
import sys

todo_list = []
file_path = "saved_data.json"

def task_add():
    task = input("Input name of the task: ")

    while True:
        print('''The importance of the task:
        1. High
        2. Medium
        3. Low''')
        priority = input("Your choice:").strip()

        match priority:
            case "1":
                priority = 1
                break
            case "2":
                priority = 2
                break
            case "3":
                priority = 3
                break
            case _:
                print("Invalid input")

    ## Sorting by priority
    new_task = {"title": task, "priority": priority, "done": False}
    for i in range(len(todo_list)):
        if priority >= todo_list[i]["priority"]:
            continue
        else:
            todo_list.insert(i, new_task)
            break
    else:
        todo_list.append(new_task)

    saving_data()

def task_show():
    if len(todo_list) > 0:
        print("\n ===List of tasks===")        
        for i in range(len(todo_list)):
            if todo_list[i]["done"]:
                mark = "x"
            else:
                mark = " "
            priority = "*" * (4 - todo_list[i]["priority"])
            print(f"{i + 1}. [{mark}] {priority} {todo_list[i]["title"]}")
    else:
        print("There is no task in the list")

def task_pop(index):
    todo_list.pop(index)
    saving_data()

def task_completed(index):
    if todo_list[index]["done"] == False:
        todo_list[index]["done"] = True
        saving_data()
    else:
        print("Task is already marked as completed")

def task_uncompleted(index):
    if todo_list[index]["done"]:
        todo_list[index]["done"] = False
        saving_data()
    else:
        print("Task is already marked as uncompleted")

## This method passes index to func on each iteration
def ask_task_number(func, prompt):
    if len(todo_list) > 0:
        while True:
            index = input(prompt)
            
            if index in [str(i) for i in range(1, len(todo_list) + 1)]:
                index = int(index) - 1
                func(index)
                break
            else:
                print("Invalid input")
    else:
        print("The list is empty. There is nothing to operate with")

## Saving data in JSON-file
def saving_data():
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(todo_list, f, ensure_ascii=False, indent = 2)

## Loading data from JSON-file
def loading_data():
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            todo_list.clear()
            todo_list.extend(json.load(f))
    except FileNotFoundError:
        saving_data()
    except json.JSONDecodeError:
        os.replace(file_path, f"{file_path}.corrupted")
        print("The file was corrupted, but it will be saved")
        
        saving_data()

def main_menu():
    loading_data()

    while True:
        print('''===Main menu===
        0. Exit
        1. Check the list of tasks
        2. Add task
        3. Delete task
        4. Mark task as completed
        5. Mark task as uncompleted''')
        context_menu_message = input("Your choice:").strip()

        match context_menu_message:
            case "0":
                saving_data()
                sys.exit()
            case "1":
                task_show()
            case "2":
                task_add()
            case "3":
                ask_task_number(task_pop, "Number of the task that you want to delete:")
            case "4":
                ask_task_number(task_completed, "Number of the task that you want to mark as completed:")
            case "5":
                ask_task_number(task_uncompleted, "Number of the task that you want to mark as uncompleted:")
            case _:
                print("Invalid input")
                continue

if __name__ == "__main__":
    main_menu()