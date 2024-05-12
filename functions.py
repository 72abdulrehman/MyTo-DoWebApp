FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        for item in todos_args:
            item = item.title()
            file.writelines(item)