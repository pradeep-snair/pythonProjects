import os
todos_file = './todos.txt'
user_input: str = "Enter add, show, edit , complete todo or exit/q to exit: "
todos = []


def modify_todo(action: str):
    """Get the num of todo to process. makes sure entered todo number is
    in the list of existing todos
    """
    clear_screen()
    show_todos(todos_file)
    todo_num = int(input(f"Enter the number of todo to {action}: "))
    with open(todos_file, 'r') as file_obj:
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
            show_todos(todos_file)


def save_todos(to_dos_lst: list):
    """ Add the argument list of todos in the file todos.txt
        Used when editing/ removing a completed to_do"""
    with open(todos_file, 'w') as file:
        for to_do in to_dos_lst:
            file.write(to_do)


def add_todos(to_do: str):
    """ Add the passed to_do in the file todos.txt"""
    if not to_do.strip():
        print("Looks like you entered an empty todo, Enter a valid string \n")
        return
    with open(todos_file, 'a') as file:
        file.write(to_do)
    print(f"Task {to_do.strip()} added  in Todo list")
    show_todos(todos_file)


def show_todos(filepath: str):
    print("Todo List".center(80, "="))
    with open(filepath, 'r') as file:
        tasks = file.readlines()
    for i, j in enumerate(tasks):
        print(f"{i + 1} - {j.strip()}")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    user_action = (input(user_input)).strip()
    if user_action.startswith('add '):
        add_todos('\n' + user_action[4:])
    elif user_action == 'add':
        to_do = input("Enter todo item to add: ") + "\n"
        add_todos(to_do)
    elif user_action == 'show':
        clear_screen()
        show_todos(todos_file)
    elif user_action == 'complete':
        modify_todo('complete')
    elif user_action == 'edit':
        modify_todo('edit')
    elif user_action == 'exit' or user_action == 'q':
        break
    else:
        print(f"Invalid option '{user_action.strip()}' entered.")


