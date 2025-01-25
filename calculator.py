import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def on_click(button_text):
    if button_text == "=":
        try:
            # Evaluate the expression in the entry widget
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input!")
    elif button_text == "C":
        # Clear the entry widget
        entry.delete(0, tk.END)
    else:
        # Append the clicked button text to the entry widget
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Create the entry widget for input/output
entry = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10, padx=10)

# Define button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create and place buttons
row, col = 1, 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 14), command=lambda bt=button_text: on_click(bt))
    button.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the Tkinter event loop
root.mainloop()
