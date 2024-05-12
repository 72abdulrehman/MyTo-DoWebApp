import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    if todo_local not in todos:
        todos.append(todo_local)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""
    
st.title("My To-Do App")
st.subheader("This is my to-do app.")
st.write("This app allows to manage to-do items.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", 
              placeholder="Add new to-do item here...",
              on_change=add_todo, key="new_todo")

