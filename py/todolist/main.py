class Todo:
    def add_task(self, task=''):
        self.task = task
        with open('TODO_List.txt', 'a') as do:
            do.write(task + '\n')


new = Todo()
# new.add_task('Write my first task.')
