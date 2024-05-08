tasks = []
def enter_task():
    task_enter = input("Enter the task that you want to add :\t")
    tasks.append(task_enter)
    print(f"Task entered is : {task_enter}")
    print(tasks)

def listTasks():
    if not tasks:
        print("There are no tasks")
    else:
        print("Current tasks: ")
        for index, t in tasks:
            print(f"Task : {index} is {t}")

def delete_task():
    try:
        index_input = int(input("Enter the task you want to delete"))
        if index_input>=0 and index_input<len(tasks):
            tasks.pop(index_input)
            print(tasks)
        else:
            print("Task not found")
    except:
        print("Invalid input")

while True:
    ask_user = input("Kindly enter the operation you want to perform \n 1. Enter a task \n 2. Delete a task \n 3. List tasks \n 4. Quit \n")

    if ask_user == "1":
        enter_task()

    elif ask_user == "2":
        delete_task()

    elif ask_user == "3":
        listTasks()

    else:
        break

print("GoodBye!!!!")