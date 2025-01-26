# 1. Animations in Tkinter
# Animations in Tkinter are often implemented using the after() method, which schedules a function to run after a specified time interval.

# Example: Simple Text Animation
import tkinter as tk

def animate_text():
    global index
    if index < len(message):
        text_label.config(text=message[:index])
        index += 1
        root.after(100, animate_text)  # Call the function again after 100ms

root = tk.Tk()
root.title("Text Animation")

message = "Welcome to Tkinter Animations!"
index = 0

text_label = tk.Label(root, font=("Arial", 16), fg="blue")
text_label.pack(pady=20)

animate_text()

root.mainloop()


# Example: Bouncing Ball Animation
import tkinter as tk

def move_ball():
    global dx, dy
    x1, y1, x2, y2 = canvas.coords(ball)
    if x1 <= 0 or x2 >= 400:
        dx = -dx
    if y1 <= 0 or y2 >= 300:
        dy = -dy
    canvas.move(ball, dx, dy)
    root.after(20, move_ball)  # Repeat every 20ms

root = tk.Tk()
root.title("Bouncing Ball")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

ball = canvas.create_oval(10, 10, 50, 50, fill="red")

dx, dy = 2, 3
move_ball()

root.mainloop()


# 2. Advanced Customizations
    # Customizing your Tkinter application can make it more professional and visually appealing.

    # Custom Fonts
    # You can use the font module for custom font styles and sizes.

import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Custom Fonts")

custom_font = font.Font(family="Comic Sans MS", size=20, weight="bold")

label = tk.Label(root, text="Hello, Tkinter!", font=custom_font)
label.pack(pady=20)

root.mainloop()


    # Custom Styles with ttk
    # Use ttk.Style to customize ttk widgets.

from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Custom ttk Style")

style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 14), foreground="white", background="blue")

button = ttk.Button(root, text="Styled Button", style="Custom.TButton")
button.pack(pady=20)

root.mainloop()


# Adding Themes
# Tkinter's ttk module supports themes. You can use the built-in themes or install external ones like ttkthemes.

# Example: Using Built-in Themes

from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Themes Example")

style = ttk.Style()
print("Available themes:", style.theme_names())  # Print all themes
style.theme_use("clam")  # Use the 'clam' theme

button = ttk.Button(root, text="Themed Button")
button.pack(pady=20)

root.mainloop()


# 3. Combining Animations and Customizations
import tkinter as tk

def animate_loading():
    global dot_count
    dot_count = (dot_count + 1) % 4
    loading_label.config(text="Loading" + "." * dot_count)
    root.after(500, animate_loading)  # Update every 500ms

root = tk.Tk()
root.title("Loading Animation")

dot_count = 0

loading_label = tk.Label(root, text="Loading", font=("Arial", 20), fg="green")
loading_label.pack(pady=50)

animate_loading()

root.mainloop()


# 4. Adding Advanced Graphics with Canvas
# You can create advanced graphics like shapes, gradients, and custom drawings using the Canvas widget.

# Example: Gradient Background

import tkinter as tk

def create_gradient(canvas, width, height):
    for i in range(height):
        color = f"#{hex(255 - i % 256)[2:].zfill(2)}00{hex(i % 256)[2:].zfill(2)}"
        canvas.create_line(0, i, width, i, fill=color)

root = tk.Tk()
root.title("Gradient Background")

width, height = 400, 300
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

create_gradient(canvas, width, height)

root.mainloop()


# 5. Advanced Layout with Resizable Widgets
# Use grid_rowconfigure and grid_columnconfigure to make widgets resizable.

import tkinter as tk

root = tk.Tk()
root.title("Resizable Widgets")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = tk.Frame(root, bg="lightblue")
frame.grid(row=0, column=0, sticky="nsew")

label = tk.Label(frame, text="Resizable Layout", bg="lightblue", font=("Arial", 18))
label.pack(expand=True)

root.mainloop()
