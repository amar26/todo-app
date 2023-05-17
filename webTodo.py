import streamlit as sl
import function as f

todos = f.get_todos()

def add_todo():
    todo = sl.session_state["new_todo"]
    todos.append(todo)
    f.write_todos(todos)

sl.title("My Todo App")
sl.subheader("This app will track the todo items")
sl.write("This is a print text")


for index, t in enumerate(todos):
    checkbox = sl.checkbox(t, key=t)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del sl.session_state[t]
        sl._rerun()

sl.text_input(label="Enter Todo item", placeholder="add new todo",
              on_change=add_todo, key='new_todo')

# sl.write(sl.session_state)
