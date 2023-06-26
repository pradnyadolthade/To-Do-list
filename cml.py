# todos = []
from funcations import get_todos,write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")
should_continue = True
while should_continue:
    user_action = input("Type add, show, edit, complete or exit :")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        # ttodo = input("Enter a todo :") + "\n"
        todos = get_todos() # this will create todos list
        todos.append(todo + '\n')
        write_todos(todos)




    elif user_action.startswith('show'):

        print("----TO-DO List-----")
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(index + 1, item)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            #number = int(input("Enter a number of TO-Do u want to edit :"))

            number = number - 1
            todos = get_todos()
            if number > len(todos) or number<0:
                print("not valid")
            else:
                new_todo = input("Enter a todo :")
                todos[number] = new_todo + '\n'
                write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            print(f"TO-Do {todo_to_remove}  was removed from the TODO list. ")
        except IndexError:
            print("No such Index available ")
            continue

    elif user_action.startswith('exit'):
        should_continue = False
        break
    else:
        print("command is not valid")


