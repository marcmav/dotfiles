class Todo:
    def add_task(self, task):
        self.task = task
        with open('todo.txt', 'a') as td:
            td.write(task + '\n')

    


new = Todo()
# new.add_task('Write my first task.')
