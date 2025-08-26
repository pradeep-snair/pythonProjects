import os
from pathlib import Path

# Get absolute path to todos.txt relative to this script as pytest was failing
BASE_DIR = Path(__file__).resolve().parent
FILEPATH = BASE_DIR / "todos.txt"


def complete_todo_gui(todo_completed: str, filepath=FILEPATH) -> None:
    """ Function to save new todos in web app. Print statement in
    modify_todo written for cli app causes issues. Function is passed the
    completed to_do which is deleted from the file storing todos"""
    with open(filepath, 'r') as file_obj:
        contents = file_obj.readlines()
    contents.remove(todo_completed)
    print(contents)
    save_todos(contents)


def modify_todo(action: str, filepath: str = FILEPATH) -> None:
    """Get the num of to_do to process. makes sure entered to_do number is
    in the list of existing todos
    """
    clear_screen()
    show_todos()
    todo_num = int(input(f"Enter the number of todo to {action}: "))
    with open(filepath, 'r') as file_obj:
        contents = file_obj.readlines()
    if 0 > todo_num or todo_num > len(contents):
        print("Please enter a valid todo number")
        return

    match action.strip():
        case 'complete':
            print(f"Removing completed todo '{contents[todo_num - 1].strip()}'")
            contents.pop(todo_num - 1)
            save_todos(contents, filepath)
        case 'edit':
            new_todo = input(f'Edit existing todo "{contents[todo_num - 1].strip()}" : ') + "\n"
            print(f"Changing '{contents[todo_num - 1].strip()}' to '{new_todo.strip()}' ")
            contents[todo_num - 1] = new_todo
            save_todos(contents, filepath)
            show_todos()


def save_todos(to_dos_lst: list, filepath=FILEPATH) -> None:
    """ Add the argument list of todos in the file todos.txt
        Used when editing/ removing a completed to_do in cli mode"""
    with open(filepath, 'w') as file:
        for to_do in to_dos_lst:
            file.write(to_do)


def check_valid_todo(to_do: str, filepath=FILEPATH) -> bool:
    """ Function checks if the to_do is duplicate or empty string entered."""
    if not to_do.strip():
        print("Looks like you missed to add any todo, Enter a valid todo \n")
        return False
    all_todos = get_todos(filepath)
    # Check for duplicate to_do
    if to_do in all_todos:
        print(f"Task {to_do} already present in your todo list\n")
        return False
    return True


def add_todos(to_do: str, cli_app: bool = False, filepath=FILEPATH) -> bool:
    """ Function to add to_do in the file todos.txt """
    with open(filepath, 'a') as file:
        file.write(to_do)
    if cli_app:
        print(f"Task {to_do.strip()} added  in Todo list")
        show_todos()
    return True


def get_todos(filepath: str = FILEPATH) -> list[str]:
    """ Function to return all current to-do's """
    with open(filepath, 'r') as file:
        tasks = file.readlines()
    return tasks


def show_todos(filepath: str = FILEPATH) -> None:
    """ Function to print all todos for cli app"""
    print("Todo List".center(80, "="))
    all_to_dos = get_todos(filepath)
    for i, j in enumerate(all_to_dos):
        print(f"{i + 1} - {j.strip()}")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
