import todo_functions
import FreeSimpleGUI as fsgui
label = fsgui.Text("Type in your To-Do")
input_box = fsgui.InputText(tooltip="Enter todo")
add_button = fsgui.Button("Add")
window = fsgui.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()


