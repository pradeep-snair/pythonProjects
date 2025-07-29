from todo_functions import *
from time import strftime
now = strftime("%b %d, %Y %H:%M:%S ")
print(f"It's {now}")

# todos_file = './todos.txt'
user_input: str = "Enter add, show, edit , complete todo or exit/q to exit: "

while True:
    user_action = (input(user_input)).strip()
    if user_action.startswith('add '):
        add_todos(user_action[4:] + '\n')
    elif user_action == 'add':
        to_do = input("Enter todo item to add: ") + "\n"
        add_todos(to_do)
    elif user_action == 'show':
        clear_screen()
        show_todos()
    elif user_action == 'complete':
        modify_todo('complete')
    elif user_action == 'edit':
        modify_todo('edit')
    elif user_action == 'exit' or user_action == 'q':
        break
    else:
        print(f"Invalid option '{user_action.strip()}' entered.")