import tkinter as tk

class TooltipApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hover Tooltip Example")

        self.button = tk.Button(self, text="Hover over me", width=20, height=2)
        self.button.pack(pady=20)

        # Create a separate window for the tooltip (hidden initially)
        self.tooltip = tk.Toplevel(self)
        self.tooltip.withdraw()  # Start hidden
        self.tooltip.overrideredirect(True)  # Removes title bar for a floating effect
        tk.Label(self.tooltip, text="Hello world", bg="yellow", fg="black", font=("Arial", 10)).pack()

        # Bind hover events
        self.button.bind("<Enter>", self.show_tooltip)
        self.button.bind("<Motion>", self.move_tooltip)
        self.button.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        """Show tooltip window outside the main window."""
        self.tooltip.deiconify()
        self.focus_force()
        self.tooltip.lift()

    def move_tooltip(self, event):
        """Move tooltip dynamically with cursor, even beyond window boundaries."""
        self.tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")

    def hide_tooltip(self, event):
        """Hide tooltip when cursor leaves the button."""
        self.tooltip.withdraw()

app = TooltipApp()
app.mainloop()
