import tkinter as tk
from tkinter import ttk

class ScrollableButtonFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scrollable Button List")
        self.geometry("300x400")

        # Create a canvas and scrollbar within the main window
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)

        # Configure canvas and scrollbar
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Generate 20-30 buttons with unique text values
        for i in range(1, 31):
            btn = tk.ttk.Button(scroll_frame, text=f"Button {i}", width=20)
            btn.pack(pady=5)

# Run the application
app = ScrollableButtonFrame()
app.mainloop()
