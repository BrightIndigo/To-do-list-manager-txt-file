num_of_task = 0
completed = []

def add():
    global num_of_task
    print("add task content: ")
    task_text = input(">")
    completed.append(False)
    with open('list.txt', 'a') as file:
        file.write(f"{num_of_task+1} {task_text} {completed[num_of_task]}\n")
    num_of_task += 1

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
        try:
            num_to_del = int(num_to_del)
            with open("list.txt", 'r') as file:
                lines = file.readlines()
                if 1 <= num_to_del <= len(lines):
                    del lines[num_to_del - 1]
                    with open("list.txt", "w") as file:
                        file.writelines(lines)
                    print(f"Line {num_to_del} deleted successfully")
                else:
                    print(f"Error, Invalid line number: {num_to_del}")
        except ValueError:
            print("Error, please enter a valid number.")

def mark_comp():
    if not read():
        print("Enter number of task you want to mark as completed: ")
        mark_comple = input(">")
        try:
            mark_comple = int(mark_comple)
            if 1 <= mark_comple <= len(completed):
                completed[mark_comple - 1] = True
                print(f"Task {mark_comple} marked as completed.")
            else:
                print(f"Error, Invalid task number: {mark_comple}")
        except ValueError:
            print("Error, please enter a valid number.")

while True:
    print("What do you want to do?")
    print("1 - add a task to list")
    print("2 - read a list of tasks")
    print("3 - delete a task")
    print("4 - mark as completed")
    print("5 - Exit")
    decision = input(">")

    if decision == "1":
        add()
    elif decision == "2":
        read()
    elif decision == "3":
        delete()
    elif decision == "4":
        mark_comp()
    elif decision == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Error: Invalid choice. Please enter a number between 1 and 5.")



