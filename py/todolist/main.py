class Todo:
    def add_task(self, task):
        self.task = task
        with open('todo.txt', 'a') as td:
            td.write(task + '\n')

    def read_tasks(self):
        with open('todo.txt', 'r') as td:
            print(td.read())

    


new = Todo()
# new.read_tasks()
