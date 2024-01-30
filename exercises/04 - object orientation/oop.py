class Todo:

    def __init__ (self, task_description, due_date, completion_status):
        self.task_description = task_description
        self.due_date = due_date
        self.completion_status = completion_status

    def complete_task(self):
        self.completion_status = True

task1 = Todo("code", 240131, False)
task2 = Todo("help", 240131, False)
task3 = Todo("run", 240131, False)
task4 = Todo("sleep", 240131, False)
task1.complete_task()
all_tasks = [task1,task2,task3,task4]
for task in all_tasks:
    if task.completion_status == True:
        print(task.task_description)



