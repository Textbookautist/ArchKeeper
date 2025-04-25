import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Notebook Example")
root.geometry("400x300")

# Create a Notebook widget
notebook = ttk.Notebook(root)

# Page 1: Mineral names with larger font
page1 = tk.Frame(notebook)
notebook.add(page1, text="Minerals")
minerals = ["Quartz", "Feldspar", "Mica", "Calcite", "Gypsum"]
for mineral in minerals:
    tk.Label(page1, text=mineral, font=("Helvetica", 12)).pack()

# Page 2: Text widget with a background color
page2 = tk.Frame(notebook, bg="lightblue")
notebook.add(page2, text="Text Widget")
text_widget = tk.Text(page2, width=40, height=10)
text_widget.pack()

# Page 3: Hello World with a different font
page3 = tk.Frame(notebook)
notebook.add(page3, text="Hello World")
tk.Label(page3, text="Hello, World!", font=("Comic Sans MS", 16)).pack()

# Page 4: Empty page with custom color and font
page4 = tk.Frame(notebook, bg="lightgreen")
notebook.add(page4, text="Empty")
tk.Label(page4, text="This is an empty page", font=("Courier", 10)).pack()

# Pack the Notebook widget
notebook.pack(expand=True, fill="both")

# Start the Tkinter main loop
root.mainloop()
