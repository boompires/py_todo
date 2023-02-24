FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of todo items
    """
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write todos to a text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# print(__name__)

if __name__ == "__main__":
    print("Hello from the functions module")
    print(get_todos())
