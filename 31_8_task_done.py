class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.done = False;
    
    def mark_done(self):
        self.done = True

    def __str__(self):
        status = ""
        if self.done:
            status = "[x]"
        return f"{status} {self.name}: {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def list_tasks(self):
        return [str(task) for task in self.tasks]
        

task = Task("Test01", "Do something")
print(task)  # "Test: Do something"
task.mark_done()
print(task)  # "[x] Test: Do something"
