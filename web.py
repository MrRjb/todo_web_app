import streamlit
import functions

todos = functions.get_todo()

def add_todo():
    todo = streamlit.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todo(todos)    

streamlit.title("My To-Do App")
streamlit.subheader("A Minimalistic Todo App.")
streamlit.write("This app is designed to boost your productivity!")

for index, todo in enumerate(todos):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()
        
    
streamlit.text_input(label="", placeholder="Type in a new todo here ...", 
                     on_change=add_todo, key='new_todo')

