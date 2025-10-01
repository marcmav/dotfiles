class Todo:
    def add_task(self, task):
        self.task = task
        with open('todo', 'a') as f:
            f.write(task + '\n')

    def read_tasks(self):
        with open('todo', 'r') as f:
            print(f.read())

    def remove_task(self, line):
        self.line = line
        with open('todo', 'r') as f:
            td = f.read()
            count = 0
            new_f = []
            for l in td:
                count += 1
                if count == self.line:
                    continue
                else:
                    new_f.append(l)
            
        print(new_f)
new = Todo()
new.remove_task(5)