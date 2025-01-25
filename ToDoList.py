import tkinter as tk
from tkinter import messagebox

# Initialize the todo list
todo_list = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task.strip():
        todo_list.append({"task": task, "done": False})
        task_entry.delete(0, tk.END)
        update_task_list()
        messagebox.showinfo("Success", f"Task '{task}' added!")
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(todo_list, start=1):
        status = "✓" if task["done"] else "✗"
        task_listbox.insert(tk.END, f"{i}. {task['task']} [{status}]")

# Function to mark a task as done
def mark_task_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        todo_list[selected_task_index]["done"] = True
        update_task_list()
        messagebox.showinfo("Success", "Task marked as done!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        removed_task = todo_list.pop(selected_task_index)
        update_task_list()
        messagebox.showinfo("Success", f"Task '{removed_task['task']}' deleted!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# Task Entry Frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, font=("Arial", 14), width=25)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(entry_frame, text="Add Task", font=("Arial", 12), command=add_task)
add_button.pack(side=tk.LEFT)

# Task Listbox
task_listbox = tk.Listbox(root, font=("Arial", 14), height=15, width=35, selectmode=tk.SINGLE)
task_listbox.pack(pady=20)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

mark_done_button = tk.Button(button_frame, text="Mark Done", font=("Arial", 12), command=mark_task_done)
mark_done_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", font=("Arial", 12), command=delete_task)
delete_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12), command=root.quit)
exit_button.grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()
