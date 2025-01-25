# to install this library : pip install tk
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("My First Tkinter App")

# Set window dimensions
root.geometry("400x300")  # Width x Height

# Tkinter provides various widgets to build applications:
# Label: Display text or images.
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Button: Add clickable buttons.
def on_click():
    print("Button clicked!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# Entry: Input field for text.
entry = tk.Entry(root)
entry.pack()

# Text Box: Multi-line text area.

text_box = tk.Text(root, height=5, width=40)
text_box.pack()


# Organizing Widgets
# Use geometry managers to arrange widgets:

# Pack: Simplest way, stacks widgets vertically or horizontally.

# label.pack()
# button.pack()


# # Grid: Use rows and columns for layout.
# label.grid(row=0, column=0)
# entry.grid(row=0, column=1)



# Place: Specify exact positions.
# button.place(x=50, y=100)

# Change Background Color:
root.configure(bg="lightblue")

# Add Menus:
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Exit", command=root.quit)

# Event Handling: Attach functions to handle user actions:

root.bind("<Return>", lambda e: print("Enter key pressed"))
# The line root.bind("<Return>", lambda e: print("Enter key pressed")) is used to bind a specific key (in this case, the Enter key) to an event handler in a Tkinter application.

# root:
# This refers to the main Tkinter application window (tk.Tk()).
# The bind method is called on this window to listen for specific keypresses.

# "<Return>":
# This is the event that the program is listening for.
# <Return> represents the Enter key on the keyboard.

# lambda e: print("Enter key pressed"):
# This is the event handler, which is a function executed when the event occurs.
# e:
# The event object automatically passed to the handler.
# It contains details about the event, such as which key was pressed.
# print("Enter key pressed"):
# Prints a message to the console whenever the Enter key is pressed.

# Run the application
root.mainloop()


# tk.Tk(): Creates the main application window.
# root.mainloop(): Starts the Tkinter event loop to display the window.