from task_manager import TaskManager

def main():
    manager = TaskManager()
    manager.add_task("Finish subsystem design", "2026-02-20")
    manager.add_task("Write PyTest cases", "2026-02-21")

    print("All Tasks:")
    for task in manager.list_tasks():
        print(task)

    print("\nSearching for 'design':")
    for task in manager.find_task("design"):
        print(task)

if __name__ == "__main__":
    main()