import os

FILEPATH = "todo.txt"

def check_file(filepath=FILEPATH):
    if not os.path.exists(filepath):
        with open(filepath, 'w'):
            pass

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    todos_local = [i.replace("\n", "") for i in todos_local]
    return todos_local

def write_todos(todos_local, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        for i in todos_local:
            file.writelines(i + "\n")
