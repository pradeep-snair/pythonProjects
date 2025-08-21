import todo_functions
import FreeSimpleGUI as fsgui

add_button = fsgui.Button("Add")
edit_button = fsgui.Button("Edit")
complete_button = fsgui.Button("Complete")

label = fsgui.Text("Type in your To-Do")
input_box = fsgui.InputText(tooltip="Enter todo", key="key_add_todo")

list_todos = fsgui.Listbox(values=todo_functions.get_todos(), key='highlighted_todo',
                           enable_events=True, size=(45, 10))
window = fsgui.Window('Prad To-Do',
                      layout=[[label], [input_box, add_button],
                              [list_todos, edit_button], [complete_button]],
                      font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            new_todo = values['key_add_todo'] + "\n"
            todo_functions.add_todos(new_todo)
            window['highlighted_todo'].update(values=todo_functions.get_todos())
        case "Edit":
            # t
            print(f"To do to edit is {values['highlighted_todo']}")
            todo_2_edit = values['highlighted_todo']
            todo_functions.modify_todo('edit')
            # pass

            # todo_functions.modify_todo(values['to-do'])
        case fsgui.WINDOW_CLOSED:
            break

window.close()


