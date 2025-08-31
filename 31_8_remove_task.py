class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return [task.name + ": " + task.description for task in self.tasks]

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                break


manager = TaskManager()

task1 = Task("Task 1", "This is task 1")
task2 = Task("Task 2", "This is task 2")
task3 = Task("Task 1", "This is task 1111")

status = manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)

manager.remove_task("Task 1")
print(manager.list_tasks())
