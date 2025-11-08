import tkinter as tk

# Create window
root = tk.Tk()
root.title("My First GUI")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create a button
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack()

# Run the app
root.mainloop()
