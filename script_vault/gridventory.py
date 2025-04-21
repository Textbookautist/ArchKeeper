import tkinter as tk

class DraggableRotatableButton(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OOOO")
        self.geometry("400x400")

        # Define cell size
        self.cell_size = 40
        self.grid_size = 8

        # Create canvas for grid lines
        self.canvas = tk.Canvas(self, width=self.grid_size * self.cell_size, height=self.grid_size * self.cell_size)
        self.canvas.place(x=40, y=40)

        # Draw grid lines
        for i in range(self.grid_size + 1):
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.grid_size * self.cell_size, fill="black")
            self.canvas.create_line(0, i * self.cell_size, self.grid_size * self.cell_size, i * self.cell_size, fill="black")

        # Create draggable button
        self.button = tk.Button(self, text="Drag Me", bg="blue", fg="white")
        self.button.place(x=40, y=40, width=80, height=40)  # Initial size and position

        self.x_offset, self.y_offset = 0, 0
        self.vertical = True  # Track rotation state

        # Bind dragging & rotation
        self.button.bind("<ButtonPress-1>", self.start_drag)
        self.button.bind("<B1-Motion>", self.drag)
        self.button.bind("<ButtonRelease-1>", self.end_drag)
        self.button.bind("<Button-3>", self.rotate)  # Right-click to rotate

    def start_drag(self, event):
        """Capture initial mouse offset."""
        self.x_offset = event.x
        self.y_offset = event.y

    def drag(self, event):
        """Move button smoothly without disrupting the grid."""
        new_x = self.button.winfo_x() + (event.x - self.x_offset)
        new_y = self.button.winfo_y() + (event.y - self.y_offset)
        self.button.place(x=new_x, y=new_y)

    def end_drag(self, event):
        """Snap button to the nearest grid position after dragging."""
        snap_x = round((self.button.winfo_x() - 40) / self.cell_size) * self.cell_size + 40
        snap_y = round((self.button.winfo_y() - 40) / self.cell_size) * self.cell_size + 40
        self.button.place(x=snap_x, y=snap_y)

    def rotate(self, event):
        """Rotate button between 2×1 and 1×2 visually."""
        if self.vertical:
            self.button.place(width=40, height=80)  # Rotate to 1×2
        else:
            self.button.place(width=80, height=40)  # Rotate back to 2×1
        self.vertical = not self.vertical

# Run the application
app = DraggableRotatableButton()
app.mainloop()
