import tkinter as tk

class DragDropGrid(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Drag-and-Drop Grid with Swapping")

        # Track grid state (stores button references)
        self.grid_state = [[None for _ in range(3)] for _ in range(3)]

        # Create 3x3 grid
        self.frames = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                frame = tk.Frame(self, width=80, height=80, bg="lightgray", relief="solid", borderwidth=1)
                frame.grid(row=row, column=col, padx=5, pady=5)
                self.frames[row][col] = frame

        # Create draggable buttons
        self.buttons = [
            tk.Button(self, text="Card A", bg="red", width=10, height=5),
            tk.Button(self, text="Card B", bg="blue", width=10, height=5),
            tk.Button(self, text="Card C", bg="green", width=10, height=5)
        ]

        # Assign buttons to initial positions
        self.button_positions = {self.buttons[0]: (0, 0), self.buttons[1]: (1, 1), self.buttons[2]: (2, 2)}

        # Place buttons inside frames and bind drag events
        for btn, (r, c) in self.button_positions.items():
            self.grid_state[r][c] = btn
            btn.grid(in_=self.frames[r][c])
            btn.bind("<ButtonPress-1>", self.start_drag)
            btn.bind("<B1-Motion>", self.dragging)
            btn.bind("<ButtonRelease-1>", self.end_drag)

        self.dragging_button = None
        self.target_position = None

    def start_drag(self, event):
        """Start dragging a button."""
        self.dragging_button = event.widget
        self.dragging_button.lift()  # Ensure it's on top visually

    def dragging(self, event):
        """Track mouse movement dynamically."""
        self.dragging_button.place(x=event.x_root - self.winfo_rootx(), y=event.y_root - self.winfo_rooty())

    def end_drag(self, event):
        """Detect drop location and swap buttons if necessary."""
        if not self.dragging_button:
            return

        x, y = event.x_root - self.winfo_rootx(), event.y_root - self.winfo_rooty()

        for row in range(3):
            for col in range(3):
                frame = self.frames[row][col]
                f_x, f_y = frame.winfo_x(), frame.winfo_y()

                # Check if button was dropped inside this frame
                if f_x < x < f_x + frame.winfo_width() and f_y < y < f_y + frame.winfo_height():
                    original_row, original_col = self.button_positions[self.dragging_button]
                    occupying_button = self.grid_state[row][col]

                    # If the slot is occupied, swap positions
                    if occupying_button:
                        self.grid_state[original_row][original_col] = occupying_button
                        self.grid_state[row][col] = self.dragging_button
                        self.button_positions[self.dragging_button] = (row, col)
                        self.button_positions[occupying_button] = (original_row, original_col)

                        occupying_button.grid_forget()
                        occupying_button.grid(in_=self.frames[original_row][original_col])

                    else:
                        # Otherwise, just move the button
                        self.grid_state[original_row][original_col] = None
                        self.grid_state[row][col] = self.dragging_button
                        self.button_positions[self.dragging_button] = (row, col)

                    self.dragging_button.grid_forget()
                    self.dragging_button.grid(in_=self.frames[row][col])

        self.dragging_button = None  # Reset dragging

# Run application
app = DragDropGrid()
app.mainloop()
