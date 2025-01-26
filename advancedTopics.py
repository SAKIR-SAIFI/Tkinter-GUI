# Advanced Topics in Tkinter
    # Event Handling
    # Geometry Managers (pack, grid, place)
    # Customizing Widgets
    # Using ttk for Enhanced Widgets
    # Canvas and Drawing
    # Adding Menus

# 1. Event Handling
# Tkinter allows you to handle events like key presses, mouse clicks, or window resizing. You can bind functions to specific events.

# Example: Binding Events
import tkinter as tk

def key_pressed(event):
    label.config(text=f"Key Pressed: {event.keysym}")

def mouse_clicked(event):
    label.config(text=f"Mouse clicked at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Event Handling")

label = tk.Label(root, text="Press a key or click anywhere!", font=("Arial", 14))
label.pack(pady=20)

# Bind key press and mouse click events
root.bind("<KeyPress>", key_pressed)
root.bind("<Button-1>", mouse_clicked)

root.mainloop()

# Key Points:
    # <KeyPress>: Handles keyboard events.
    # <Button-1>: Handles left mouse clicks.
    # event.keysym: Captures the key name.
    # event.x, event.y: Get mouse click coordinates.

# 2. Geometry Managers
# Tkinter provides three geometry managers:

    # pack: Places widgets in blocks (top, bottom, left, right).
    # grid: Places widgets in a grid (row-column format).
    # place: Places widgets at specific coordinates.

# Example: Using grid
import tkinter as tk

root = tk.Tk()
root.title("Grid Layout")

# Add widgets in a grid
for i in range(3):
    for j in range(3):
        tk.Button(root, text=f"({i}, {j})", font=("Arial", 12)).grid(row=i, column=j, padx=5, pady=5)

root.mainloop()

# Key Points:
    # Use row and column to position widgets.
    # Add padding with padx and pady.

# 3. Customizing Widgets
# You can style widgets using options like bg, fg, font, and relief.

# Example: Custom Button Styles
import tkinter as tk

root = tk.Tk()
root.title("Custom Buttons")

# Add styled buttons
btn1 = tk.Button(root, text="Flat", font=("Arial", 12), relief=tk.FLAT)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Raised", font=("Arial", 12), relief=tk.RAISED, bg="lightblue")
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Sunken", font=("Arial", 12), relief=tk.SUNKEN, fg="white", bg="black")
btn3.pack(pady=5)

root.mainloop()

# 4. Using ttk for Enhanced Widgets
# The ttk module provides modern-looking widgets, such as ttk.Button and ttk.Combobox.

# Example: ttk.Combobox
from tkinter import ttk
import tkinter as tk

def show_selection():
    selected_item = combobox.get()
    label.config(text=f"Selected: {selected_item}")

root = tk.Tk()
root.title("ttk Combobox")

label = tk.Label(root, text="Select an item", font=("Arial", 14))
label.pack(pady=10)

# Create a Combobox
combobox = ttk.Combobox(root, values=["Item 1", "Item 2", "Item 3"])
combobox.pack(pady=10)

button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack(pady=10)

root.mainloop()

# 5. Canvas and Drawing
# The Canvas widget allows drawing shapes, images, or custom graphics.

# Example: Drawing Shapes
import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw shapes
canvas.create_line(50, 50, 300, 50, fill="blue", width=3)
canvas.create_rectangle(50, 100, 300, 200, outline="red", width=2)
canvas.create_oval(100, 100, 250, 200, fill="green")

root.mainloop()




# 6. Adding Menus
# Menus are essential for creating dropdown menus like File, Edit, etc.

# Example: Adding a Menu
import tkinter as tk

def new_file():
    label.config(text="New File Created!")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Menu Example")

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Add the File menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Display the menu bar
root.config(menu=menu_bar)

label = tk.Label(root, text="Use the File menu", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()
