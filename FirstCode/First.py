"""
Simple Task Manager Application
This script demonstrates basic Python concepts including:
- Functions
- Lists and dictionaries
- User input handling
- File operations
- Error handling
"""

import json
from datetime import datetime


class TaskManager:
    def __init__(self):
        """Initialize the task manager with an empty task list"""
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from file if it exists"""
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            # If file doesn't exist, start with empty task list
            self.tasks = []

    def save_tasks(self):
        """Save tasks to file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title, description):
        """Add a new task to the list"""
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'date_created': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"\nTask '{title}' added successfully!")

    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("\nNo tasks found.")
            return

        print("\nYour Tasks:")
        print("-" * 50)
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            print(f"{task['id']}. [{status}] {task['title']}")
            print(f"   Description: {task['description']}")
            print(f"   Created: {task['date_created']}")
            print("-" * 50)

    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"\nTask '{task['title']}' marked as completed!")
                return
        print("\nTask not found.")

    def delete_task(self, task_id):
        """Delete a task"""
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"\nTask '{task['title']}' deleted successfully!")
                return
        print("\nTask not found.")


def main():
    """Main function to run the task manager"""
    task_manager = TaskManager()
    
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        try:
            if choice == '1':
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                task_manager.add_task(title, description)
            
            elif choice == '2':
                task_manager.view_tasks()
            
            elif choice == '3':
                task_id = int(input("Enter task ID to mark as completed: "))
                task_manager.complete_task(task_id)
            
            elif choice == '4':
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            
            elif choice == '5':
                print("\nThank you for using Task Manager!")
                break
            
            else:
                print("\nInvalid choice. Please try again.")
                
        except ValueError:
            print("\nPlease enter a valid number.")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")


if __name__ == "__main__":
    main()