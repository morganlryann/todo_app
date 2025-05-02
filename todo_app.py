# Simple To-Do List App with Mark as Done feature

# Each task will be stored as a dictionary: {"name": "Do laundry", "done": False}
tasks = []

def add_task(task_name):
    task = {"name": task_name, "done": False}
    tasks.append(task)
    print(f"Added: {task}")

def show_tasks():
    print("\nYour To-Do List:")
    if not tasks:
        print("No tasks yet!")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number!")

# Main menu loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Delete a task")
    print("4. Quit")

    choice = input("What do you want to do? (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        try:
            task_num = int(input("Enter the task number to delete: "))
            delete_task(task_num)
        except ValueError:
            print("Please enter a number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, or 4.")
