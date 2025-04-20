import tkinter as tk
import random



class MainWindow(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("200x200")
        self.title("Woah")
        self.config(bg="black")
        self.buttons = []
        self.main()
    
    def clear(self):
        for item in self.buttons:
            item.destroy()

    def add(self, object):
        self.buttons.append(object)

    def remove(self, object):
        self.buttons.remove(object)

    def main(self):
        self.clear()

        mainframe = tk.Frame(self,bg="black",height=20)
        mainframe.pack(pady=10)
        self.add(mainframe)

        btns = ["Math", "History", "P.E."]
        colors = ["red", "yellow", "blue"]
        fcolors = ["white", "black", "yellow"]
        X = 0
        Y = 0
        for btn in btns:
            button = tk.Button(mainframe, bg=colors[0], text=btn, width=2,height=8,fg=fcolors[0])
            button.grid(row=X,column=Y)
            colors.remove(colors[0])
            fcolors.remove(fcolors[0])
            self.add(button)
            button.bind("<Enter>", lambda event, b=button: self.show_info(b))
            button.bind("<Leave>", lambda event, b=button: self.close_info(b))
            Y += 1

    def show_info(self, button):
        stuff = button.cget("text")
        value = random.randint(0,5)
        values = ["A", "B", "C", "D", "E", "F"]
        totalval = values[value]
        button.config(width=10,height=10,text=f"{stuff}\n{totalval}")

    def close_info(self, button):
        stuff = button.cget("text")
        stuff = stuff.split("\n")
        content = stuff[0]
        button.config(width=2,height=8,text=content)

root = MainWindow()

tk.mainloop()