FILEPATH = 'todo.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as data:
        todos_local = data.readlines()
    return todos_local


def write_todos(todo_arg, filepath=FILEPATH):
    with open(filepath, 'w') as data:
        data.writelines(todo_arg)
