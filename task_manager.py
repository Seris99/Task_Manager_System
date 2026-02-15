from task import Task

class TaskManager:
    """
    Manages a collection of tasks.
    """

    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        """Create and add a new task."""
        task = Task(description, due_date)
        self.tasks.append(task)
        return task

    def remove_task(self, description):
        """Remove a task by description."""
        self.tasks = [t for t in self.tasks if t.description != description]

    def list_tasks(self):
        """Return all tasks as strings."""
        return [str(task) for task in self.tasks]

    def find_task(self, keyword):
        """Search tasks by keyword in description."""
        return [t for t in self.tasks if keyword.lower() in t.description.lower()]