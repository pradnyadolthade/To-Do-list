import funcations
import PySimpleGUI as sg
import  time


sg.theme("DarkPurPle4")
clock = sg.Text("",key="clock")
lable = sg.Text("Type a todos ")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_btn = sg.Button("Add",size=10)
list_box = sg.Listbox(values=funcations.get_todos(), key='todos',
                      enable_events=True,
                      size=[45,10])
edit_btn = sg.Button("Edit")
complete_btn = sg.Button("Complete")
exit_btn = sg.Button("Exit")

window = sg.Window('My To-Do List',
                   layout=[[clock],
                           [lable],
                           [input_box,add_btn],
                           [list_box,edit_btn, complete_btn],
                           [exit_btn]],
                   font=("Helvetica",15))

while True:
    event,values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == "Add":
        todos = funcations.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        funcations.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            print(todo_to_edit)
            new_todo = values['todo'] + "\n"
            todos = funcations.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            funcations.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Select an item first.")

    elif event == "Complete":
        try:
            todo_to_complete = values['todos'][0]
            todos = funcations.get_todos()
            todos.remove(todo_to_complete)
            funcations.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value ='')
        except IndexError:
            sg.popup("Select an item first.")

    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])
    elif event == "Exit":
        break
    elif event== sg.WIN_CLOSED:
        break


window.close()