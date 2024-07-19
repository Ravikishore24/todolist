tasks = []
def display_tasks():
    print("To-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = '✓' if task['completed'] else ' '
        print(f"{index}. [{status}] {task['title']} - {task['description']}")

def add_task(title, description):
    tasks.append({'title': title, 'description': description, 'completed': False})
    print("Task added successfully!")

def mark_task_done(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        print("Task marked as done.")
    else:
        print("Invalid task index.")

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task deleted.")
    else:
        print("Invalid task index.")
def main():
    while True:
        print("\nOptions:")
        print("A. Display To-Do List")
        print("B. Add a Task")
        print("C. Mark a Task as Done")
        print("D. Delete a Task")
        print("E. Exit")

        choice = input("Enter your choice: ")

        if choice == 'A':
            display_tasks()
        elif choice == 'B':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == 'C':
            task_index = int(input("Enter task index to mark as done: "))
            mark_task_done(task_index)
        elif choice == 'D':
            task_index = int(input("Enter task index to delete: "))
            delete_task(task_index)
        elif choice == 'E':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    print("Exiting the To-Do List application.")

if _name_ == "_main_":
    main()