class Task:
    """
    Represents a single task in the system.
    """

    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def edit_description(self, new_description):
        """Update the task description."""
        self.description = new_description

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description} (Due: {self.due_date})"