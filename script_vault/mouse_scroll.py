import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Scrollable Window Example")
root.geometry("300x300")

# Create a canvas and a scrollbar
canvas = tk.Canvas(root, width=300, height=300)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

# Configure the scrollable frame
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Attach the frame to the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Add widgets (buttons) to the scrollable frame
for i in range(50):
    button = tk.Button(scrollable_frame, text=f"Button {i + 1}")
    button.pack(pady=5)

# Bind the mouse scroll wheel to scroll the canvas
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Pack the widgets
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Start the Tkinter main loop
root.mainloop()
