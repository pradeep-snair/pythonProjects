import streamlit as st
import time
import todo_functions

all_todos = todo_functions.get_todos()
print(all_todos)
st.title("Prad's Basic To Do App")


def add_todo():
    new_todo = st.session_state["new_todo"]
    status = todo_functions.add_todos(f"{new_todo}\n")
    if not status:
        st.session_state['new_todo'] = ''
        st.write("Looks like you entered a duplicate task")
    else:
        st.session_state['new_todo'] = ''
        st.toast(f"✅ Todo '{new_todo}' Added!")
        # Notification is hiding the title, implement as column layout
        # notification = st.empty()  # Placeholder for notification
        # notification.success(f"✅ Todo '{new_todo}' Added!")  # Display success message
        # time.sleep(2)  # Keep message visible for 2 seconds
        # notification.empty()  # Clear the notification


for todo in all_todos:
    state = st.checkbox(todo, key=todo)
    if state:
        # st.write(f"To do '{todo}'  selected ")
        todo_functions.complete_todo_gui(todo)
        st.rerun()
    # st.checkbox(todo, key=todo)

st.text_input(label='Add Todo', label_visibility='hidden', placeholder="Enter your new todo",
              on_change=add_todo, key='new_todo')
# st.session_state
