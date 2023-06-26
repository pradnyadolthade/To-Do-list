import streamlit as st
import funcations
todos = funcations.get_todos()
st.title("My Todo App")
st.subheader("This is my todo App. ")
st.write("This App is to write TODO")

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    funcations.write_todos(todos)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        funcations.write_todos(todos)
        del st.session_state[todo]
        st._rerun()


st.text_input(label='',placeholder="Add new todo...",on_change=add_todo,key="new_todo")