# Main

import os
import sys
import tkinter as tk

# Configs
script_dir = os.path.dirname(os.path.abspath(__file__))
configs_dir = os.path.join(script_dir,"configs")
settings_file = os.path.join(configs_dir, "Settings")
items_dir = os.path.join(script_dir,"items")
spells_dir = os.path.join(script_dir,"spells")
characters_dir = os.path.join(script_dir,"characters")


class Config:
    def __init__(self):
        self.configs = []
        with open(settings_file, "r") as file:
            for line in file:
                self.configs.append(str(line))
        self.settings_name = []
        self.settings_value = []
        for setting in self.configs:
            content = setting.strip()
            content = content.split("=")
            if content[0] == "geometry":
                self.geometry = str(content[1])
            elif content[0] == "title":
                self.title = content[1]
            print(content)
            self.settings_name.append(content[0])
            self.settings_value.append(content[1])
        print(self.settings_name,self.settings_value)
    def save(self, list):
        X = 0
        lines = []
        self.configs = []
        for i in list:
            if X == 0:
                setting = f"geometry="+list[X]
                self.geometry = list[X]
                self.configs.append(setting)
            elif X == 1:
                setting = f"title="+list[X]
                self.title = list[X]
                self.configs.append(setting)
            lines.append(setting)
            X += 1
        with open(settings_file, "w") as file:
            for line in lines:
                file.write(f"{line}\n")
        self.settings_name = []
        self.settings_value = []
        for setting in self.configs:
            content = setting.strip()
            content = content.split("=")
            if content[0] == "geometry":
                self.geometry = str(content[1])
            elif content[0] == "title":
                self.title = content[1]
            print(content)
            self.settings_name.append(content[0])
            self.settings_value.append(content[1])
            


class MainWindow(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.config = Config()

        self.geometry(self.config.geometry)
        self.title(self.config.title)
        self.buttons = []
        self.GUI_init()

    def quitconfirm(self, button):
        button.destroy()
        self.buttons.remove(button)

        quit_frame = tk.Frame(self)
        quit_frame.pack(side="bottom")
        self.buttons.append(quit_frame)

        b_confirm = tk.Button(quit_frame, text="Confirm",command=lambda:quit())
        b_confirm.pack(side="left",padx=3)
        self.buttons.append(b_confirm)

        b_decline = tk.Button(quit_frame,text="Decline", command=self.GUI_init)
        b_decline.pack(side="right",padx=3)
        self.buttons.append(b_decline)
    
    def GUI_init(self):
        for entity in self.buttons:
            entity.destroy()
        mainframe = tk.Frame(self)
        mainframe.pack(anchor="center")
        self.buttons.append(mainframe)

        mainlabel = tk.Label(mainframe, text="Main Menu", font=30)
        mainlabel.pack(side="top",pady=10)
        self.buttons.append(mainlabel)

        settings_button = tk.Button(mainframe, text="Settings", command=self.settings_menu)
        settings_button.pack(side="top")
        self.buttons.append(settings_button)

        quit_button = tk.Button(self,text="QUIT",command=lambda: self.quitconfirm(quit_button))
        quit_button.pack(side="bottom")
        self.buttons.append(quit_button)

        
    
    def settings_menu(self):
        for entity in self.buttons:
            entity.destroy()

        setting_frame = tk.Frame(self)
        setting_frame.pack(anchor="center")
        setting_content = []
        self.buttons.append(setting_frame)

        setting_label = tk.Label(setting_frame, text="SETTINGS", font=20)
        setting_label.pack(side="top",pady=10)
        self.buttons.append(setting_label)

        index = 0
        for setting in self.config.settings_name:
            
            
            setting = setting.capitalize()
            set = tk.Frame(setting_frame)
            set.pack(anchor="n",pady=5)
            self.buttons.append(set)


            label = tk.Label(set, text=setting)
            label.pack(side="left",padx=3)
            self.buttons.append(label)

            entry = tk.Entry(set)
            entry.pack(side="right", padx=3)
            entry.insert(0, self.config.settings_value[index])
            self.buttons.append(entry)
            setting_content.append(entry)

            index += 1
        
        save_button = tk.Button(setting_frame, text="SAVE", command=lambda: self.setting_change(setting_content))
        save_button.pack(side="bottom",pady=5)

        print(setting_content)
        
        back_main = tk.Button(self, text="Back", font=10, command=self.GUI_init)
        back_main.pack(side="bottom")
        self.buttons.append(back_main)
    
    def setting_change(self, inputlist):
        X = 0
        savelist = []
        for i in inputlist:
            Y = i.get()
            savelist.append(Y)
            if X == 0:
                self.geometry(Y)
            elif X == 1:
                self.title(Y)
            X += 1
        self.config.save(savelist)


            



root = MainWindow()



tk.mainloop()



