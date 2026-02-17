# gui_task_manager.py
import tkinter as tk
from tkinter import ttk, messagebox
from task_manager import TaskManager

class TaskManagerGUI:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("600x400")

        # --- Input Frame ---
        input_frame = ttk.Frame(root, padding="10")
        input_frame.pack(fill="x")

        ttk.Label(input_frame, text="Description:").grid(row=0, column=0, sticky="w")
        self.desc_entry = ttk.Entry(input_frame, width=40)
        self.desc_entry.grid(row=0, column=1, padx=5)

        ttk.Label(input_frame, text="Due Date:").grid(row=0, column=2, sticky="w")
        self.date_entry = ttk.Entry(input_frame, width=15)
        self.date_entry.grid(row=0, column=3, padx=5)

        ttk.Button(input_frame, text="Add Task", command=self.add_task).grid(row=0, column=4, padx=5)

        # --- Task List ---
        self.tree = ttk.Treeview(root, columns=("Description", "Due Date", "Status"), show="headings")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Due Date", text="Due Date")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # --- Action Buttons ---
        action_frame = ttk.Frame(root, padding="10")
        action_frame.pack(fill="x")

        ttk.Button(action_frame, text="Mark Complete", command=self.mark_complete).pack(side="left", padx=5)
        ttk.Button(action_frame, text="Remove Task", command=self.remove_task).pack(side="left", padx=5)

        ttk.Label(action_frame, text="Search:").pack(side="left", padx=5)
        self.search_entry = ttk.Entry(action_frame, width=20)
        self.search_entry.pack(side="left", padx=5)
        ttk.Button(action_frame, text="Find", command=self.search_task).pack(side="left", padx=5)

    def add_task(self):
        desc = self.desc_entry.get().strip()
        date = self.date_entry.get().strip()
        if not desc:
            messagebox.showwarning("Input Error", "Description cannot be empty.")
            return
        task = self.manager.add_task(desc, date)
        self.tree.insert("", "end", values=(task.description, task.due_date, "✗"))
        self.desc_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def mark_complete(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("No Selection", "Select a task to mark complete.")
            return
        for item in selected:
            desc = self.tree.item(item, "values")[0]
            for task in self.manager.tasks:
                if task.description == desc:
                    task.mark_complete()
                    self.tree.item(item, values=(task.description, task.due_date, "✓"))

    def remove_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("No Selection", "Select a task to remove.")
            return
        for item in selected:
            desc = self.tree.item(item, "values")[0]
            self.manager.remove_task(desc)
            self.tree.delete(item)

    def search_task(self):
        keyword = self.search_entry.get().strip()
        if not keyword:
            messagebox.showwarning("Input Error", "Enter a keyword to search.")
            return
        results = self.manager.find_task(keyword)
        self.tree.delete(*self.tree.get_children())
        for task in results:
            status = "✓" if task.completed else "✗"
            self.tree.insert("", "end", values=(task.description, task.due_date, status))

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()