class TaskManager:
    ALL_TASKS = []

    def __str__(self):
        return f"{self.ALL_TASKS}"

    def add_task(self, name, priority):
        tpl = (name, priority)
        TaskManager.ALL_TASKS.append(tpl)


    @classmethod
    def count_manager(cls):
        return len(cls.ALL_TASKS)


    def remove_task(self, name):
        for tpl in TaskManager.ALL_TASKS:
            for i in tpl:
                if i == name and isinstance(i, str):
                    TaskManager.ALL_TASKS.remove(tpl)
                    print(f"The task '{name}' is deleted")
                elif tpl == TaskManager.ALL_TASKS[-1] and i != name and isinstance(i, str):
                    print("there is no such a task")


    def next_task(self):
        nums = []
        names = []
        for tpl in TaskManager.ALL_TASKS:
            for i in tpl:
                if isinstance(i, str):
                    names.append(i)
                else:
                    nums.append(i)
        d = dict(zip(names, nums))
        for i in names:
            if d[i] == max(nums):
                print({i: max(nums)})

manager = TaskManager()
manager.add_task("Buy milk", 1)
manager.add_task("Walk with a dog", 2)
manager.add_task("Read a book", 5)
manager.add_task("Learn English", 10)


class Tasks:
    def __init__(self, task):
        self.task = task

    def __str__(self):
        return self.task

    @property
    def name(self):
        return self.task

    @name.setter
    def name(self, value):
        self.task = value


manager_1 = Tasks("Fix bug")
manager_2 = Tasks("Deploy")
print(manager_1)
print(manager_2.name)
manager_2.name = "Release"
print(manager_2.name)


