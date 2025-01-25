import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import json
from datetime import datetime
import os

class EnhancedTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced To-Do List")
        self.root.geometry("600x700")

        self.TASKS_FILE = "tasks.json"
        self.todo_list = []
        self.categories = set(["General"])

        self.create_widgets()
        self.load_tasks()
        self.update_task_list()
        self.update_category_menu()

    def create_widgets(self):
        # Task Entry Frame
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Task:").pack(side=tk.LEFT)
        self.task_entry = tk.Entry(entry_frame, font=("Arial", 14), width=30)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        # Category Selection
        tk.Label(entry_frame, text="Category:").pack(side=tk.LEFT)
        self.category_var = tk.StringVar(value="General")
        self.category_dropdown = tk.OptionMenu(entry_frame, self.category_var, *self.categories)
        self.category_dropdown.pack(side=tk.LEFT, padx=5)

        # Add Category Button
        add_category_btn = tk.Button(entry_frame, text="+", command=self.add_new_category)
        add_category_btn.pack(side=tk.LEFT)

        # Add Task Button
        add_button = tk.Button(entry_frame, text="Add Task", command=self.add_task)
        add_button.pack(side=tk.LEFT, padx=5)

        # Task Listbox with Scrollbar
        listbox_frame = tk.Frame(self.root)
        listbox_frame.pack(pady=10, expand=True, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
        self.task_listbox = tk.Listbox(
            listbox_frame,
            font=("Arial", 12),
            selectmode=tk.SINGLE,
            yscrollcommand=self.scrollbar.set
        )
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Button Frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        buttons = [
            ("Mark Done", self.mark_task_done),
            ("Edit Task", self.edit_task),
            ("Delete Task", self.delete_task),
            ("Export", self.export_tasks),
            ("Import", self.import_tasks)
        ]

        for text, command in buttons:
            tk.Button(button_frame, text=text, command=command).pack(side=tk.LEFT, padx=5)

        # Priority Filter
        filter_frame = tk.Frame(self.root)
        filter_frame.pack(pady=5)

        tk.Label(filter_frame, text="Filter by:").pack(side=tk.LEFT)
        
        self.filter_var = tk.StringVar(value="All")
        filter_options = ["All", "Pending", "Completed", "By Category"]
        self.filter_dropdown = tk.OptionMenu(filter_frame, self.filter_var, *filter_options, command=self.update_task_list)
        self.filter_dropdown.pack(side=tk.LEFT, padx=5)

    def add_new_category(self):
        new_category = simpledialog.askstring("New Category", "Enter new category name:")
        if new_category and new_category.strip():
            self.categories.add(new_category.strip())
            self.update_category_menu()

    def update_category_menu(self):
        menu = self.category_dropdown['menu']
        menu.delete(0, 'end')
        for category in sorted(self.categories):
            menu.add_command(label=category, command=tk._setit(self.category_var, category))

    def add_task(self):
        task = self.task_entry.get().strip()
        category = self.category_var.get()
        
        if task:
            new_task = {
                "task": task,
                "category": category,
                "done": False,
                "created_at": datetime.now().isoformat()
            }
            self.todo_list.append(new_task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task_list(self, *args):
        self.task_listbox.delete(0, tk.END)
        filter_mode = self.filter_var.get()
        
        filtered_tasks = self.todo_list
        if filter_mode == "Pending":
            filtered_tasks = [task for task in self.todo_list if not task['done']]
        elif filter_mode == "Completed":
            filtered_tasks = [task for task in self.todo_list if task['done']]
        
        for i, task in enumerate(filtered_tasks, start=1):
            status = "✓" if task["done"] else "✗"
            display = f"{i}. [{task['category']}] {task['task']} [{status}]"
            self.task_listbox.insert(tk.END, display)

    def mark_task_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            filtered_tasks = self.get_filtered_tasks()
            selected_task = filtered_tasks[selected_index]
            
            # Find the actual index in the main list
            for task in self.todo_list:
                if task == selected_task:
                    task['done'] = not task['done']
                    break
            
            self.save_tasks()
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task.")

    def get_filtered_tasks(self):
        filter_mode = self.filter_var.get()
        
        if filter_mode == "Pending":
            return [task for task in self.todo_list if not task['done']]
        elif filter_mode == "Completed":
            return [task for task in self.todo_list if task['done']]
        
        return self.todo_list

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            filtered_tasks = self.get_filtered_tasks()
            selected_task = filtered_tasks[selected_index]
            
            for i, task in enumerate(self.todo_list):
                if task == selected_task:
                    new_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=task['task'])
                    if new_task:
                        self.todo_list[i]['task'] = new_task
                        break
            
            self.save_tasks()
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            filtered_tasks = self.get_filtered_tasks()
            selected_task = filtered_tasks[selected_index]
            
            self.todo_list = [task for task in self.todo_list if task != selected_task]
            
            self.save_tasks()
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def save_tasks(self):
        with open(self.TASKS_FILE, "w") as file:
            json.dump(self.todo_list, file, indent=4)

    def load_tasks(self):
        try:
            with open(self.TASKS_FILE, "r") as file:
                self.todo_list = json.load(file)
                # Extract unique categories
                self.categories = set(task['category'] for task in self.todo_list)
                self.categories.add("General")
        except (FileNotFoundError, json.JSONDecodeError):
            self.todo_list = []

    def export_tasks(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json")
        if filename:
            with open(filename, "w") as file:
                json.dump(self.todo_list, file, indent=4)
            messagebox.showinfo("Export", f"Tasks exported to {filename}")

    def import_tasks(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            try:
                with open(filename, "r") as file:
                    imported_tasks = json.load(file)
                    self.todo_list.extend(imported_tasks)
                    # Update categories
                    self.categories.update(task['category'] for task in imported_tasks)
                    self.update_category_menu()
                    self.save_tasks()
                    self.update_task_list()
                messagebox.showinfo("Import", f"Tasks imported from {filename}")
            except (FileNotFoundError, json.JSONDecodeError):
                messagebox.showerror("Error", "Invalid file or import failed")

def main():
    root = tk.Tk()
    app = EnhancedTodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()