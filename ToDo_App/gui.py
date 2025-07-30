import todo_functions
import FreeSimpleGUI as fsgui

label = fsgui.Text("Type in your To-Do")
input_box = fsgui.InputText(tooltip="Enter todo", key="to_do")

add_button = fsgui.Button("Add")
edit_button = fsgui.Button("Edit")
complete_button = fsgui.Button("Complete")

list_todos = fsgui.Listbox(values=todo_functions.get_todos(), key='selected_to_do',
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
            new_todo = values['to_do'] + "\n"
            todo_functions.add_todos(new_todo)
        # case "Edit":
        #     pass

            # todo_functions.modify_todo(values['to-do'])
        case fsgui.WINDOW_CLOSED:
            break

window.close()


