import os
FILEPATH = './todos.txt'


def modify_todo(action: str):
    """Get the num of todo to process. makes sure entered todo number is
    in the list of existing todos
    """
    clear_screen()
    show_todos()
    todo_num = int(input(f"Enter the number of todo to {action}: "))
    with open(FILEPATH, 'r') as file_obj:
        contents = file_obj.readlines()
    if 0 > todo_num or todo_num > len(contents):
        print("Please enter a valid todo number")
        return

    match action.strip():
        case 'complete':
            print(f"Removing completed todo '{contents[todo_num - 1].strip()}'")
            contents.pop(todo_num - 1)
            save_todos(contents)
        case 'edit':
            new_todo = input(f'Edit existing todo "{contents[todo_num - 1].strip()}" : ') + "\n"
            print(f"Changing '{contents[todo_num - 1].strip()}' to '{new_todo.strip()}' ")
            contents[todo_num - 1] = new_todo
            save_todos(contents)
            show_todos()


def save_todos(to_dos_lst: list, filepath=FILEPATH):
    """ Add the argument list of todos in the file todos.txt
        Used when editing/ removing a completed to_do"""
    with open(filepath, 'w') as file:
        for to_do in to_dos_lst:
            file.write(to_do)


def add_todos(to_do: str):
    """ Add the passed to_do in the file todos.txt"""
    if not to_do.strip():
        print("Looks like you entered an empty todo, Enter a valid string \n")
        return
    with open(FILEPATH, 'a') as file:
        file.write(to_do)
    print(f"Task {to_do.strip()} added  in Todo list")
    show_todos()


def show_todos(filepath: str = FILEPATH):
    print("Todo List".center(80, "="))
    all_to_dos = get_todos()
    # with open(filepath, 'r') as file:
    #     tasks = file.readlines()
    for i, j in enumerate(all_to_dos):
        print(f"{i + 1} - {j.strip()}")


def get_todos(filepath: str = FILEPATH):
    """ Function to get all current to-do's """
    with open(filepath, 'r') as file:
        tasks = file.readlines()
    return tasks


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')