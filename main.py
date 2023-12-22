num_of_task = 0
def add():
    print("add task content: ")
    task_text = input(">")
    with open('list.txt', 'a') as file:
        file.write(f"{num_of_task} {task_text}, \n")


def read():
    with open('list.txt', 'r') as file:
        content = file.read()

    if content != "":
        print(content)
        empty = False
    else:
        print("List is empty!")
        empty = True
        return empty


def delete():
    if not read():
        print("Select a number of line you want to delete:")
        num_to_del = input(">")
        num_to_del = int(num_to_del)
        with open("list.txt", 'r') as file:
            lines = file.readlines()
            if 1 <= num_to_del <= len(lines):
                del lines[num_to_del-1]

                with open("list.txt", "w") as file:
                    file.writelines(lines)
                print(f"Line {num_to_del} deleted succesfully")

            else:
                print(f"Error, Invalid line number: {num_to_del}")


while True:
    print("What do you want to do?")
    print("1 - add a task to list")
    print("2 - read a list of tasks")
    print("3 - delete a task")
    decision = input(">")

    if decision == "1":
        num_of_task += 1
        add()
    elif decision == "2":
        read()
    elif decision == "3":
        delete()
    else:
        print("Error")




