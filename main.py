class Task:
    def __init__(self, title, description, due_date, priority, numOfTask):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.numOfTask = numOfTask
        self.completed = False

def addTask(tasks_list, numOfTask):
    title = input("Add title: ")
    description = input("Add description: ")
    due_date = input("Add due date: ")
    priority = input("Add priority: ")

    task = Task(title, description, due_date, priority, numOfTask)
    tasks_list.append(task)
    print("Task added succesfully.")

tasks = []
counter = 0

while True:
    decision = input("Add task (a), remove task (r), mark completed (m), View To-Do List (v), exit (e): ")

    if decision == 'a':
        counter += 1
        addTask(tasks, counter)

    elif decision == 'e':
        break

    elif decision == 'v':
        for task in tasks:
            print(f"Task {task.numOfTask}:")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Due Date: {task.due_date}")
            print(f"Priority: {task.priority}")
            print(f"Completed: {'Yes' if task.completed else 'No'}")
            print("---------------------")


    elif decision == 'm':

        number = int(input("Number of task to mark: "))

        if 1 <= number <= len(tasks):
            task_to_mark = tasks[number - 1]
            task_to_mark.completed = True
            print(f"Task {number} marked as completed.")
        else:
            print("Invalid task number. Please choose a valid task.")


    elif decision == 'r':
        number_to_delete = int(input("Enter the number of task to delete: "))
        if 1 <= number_to_delete <= len(tasks):
            task_to_delete = tasks.pop(number_to_delete - 1)
            print(f"Task {task_to_delete.numOfTask} '{task_to_delete.title}' deleted.")
        else:
            print("Invalid task number. Please choose a valid task.")


