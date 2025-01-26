# Widgets are the building blocks of a Tkinter GUI application. They are used to build the user interface and interact with users.

# Commonly Used Widgets
# Below is a list of common widgets and their purposes:

    #  Label: Displays static text or images.
    # Button: Creates clickable buttons.
    # Entry: Allows single-line text input.
    # Text: Allows multi-line text input.
    # Frame: A container for organizing widgets.
    # Listbox: Displays a list of items.
    # Scrollbar: Adds scrollbars to other widgets.
    # Radiobutton: Lets users select one option from a group.
    # Checkbutton: Allows multiple options to be selected.
    # Canvas: Used for drawing shapes or custom graphics.
    # Menu: Creates menus (like File, Edit, etc.).
    # Combobox: A dropdown list for selection (requires ttk).

# Widget Syntax
# The general syntax for adding a widget:

# widget = WidgetClass(parent, options...)
# widget.pack()  # or use grid() or place()

    # parent: The widget in which the new widget is placed (e.g., root).
    # options: Configuration options like text, color, font, etc.
    # pack(), grid(), or place(): Position the widget.


# Example 1: Basic Widgets
# Let’s create a GUI with a Label, Button, and Entry.

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic Widgets")
root.geometry("300x200")

# Add a Label
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=10)

# Add an Entry
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Add a Button
def show_message():
    user_input = entry.get()
    label.config(text=f"Hello, {user_input}!")

button = tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=10)

# Run the application
root.mainloop()


# Explanation:
    # Label: Displays the static text "Welcome to Tkinter!".
    # Entry: Lets the user input their name.
    # Button: Updates the label with the input text when clicked.


# Example 2: Using Frames for Layout
# Frames are used to group and organize widgets.

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Frames Example")
root.geometry("300x300")

# Create a Frame
frame = tk.Frame(root, bg="lightblue", relief=tk.RAISED, borderwidth=2)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Add Widgets to the Frame
label = tk.Label(frame, text="Inside the Frame", bg="lightblue", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(frame, text="Click Me", command=lambda: print("Button clicked!"))
button.pack(pady=10)

# Run the application
root.mainloop()

# Explanation:
    # Frame: A container with a raised border.
    # Widgets in Frame: Both the label and button are placed inside the frame.



# Homework
    # Create a simple login GUI with:

    # Two Entry widgets for username and password.
    # A Button to submit the login.
    # A Label to show whether login is successful.
    # Experiment with different widget options like bg, fg, font, and relief.

