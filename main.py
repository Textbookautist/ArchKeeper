# Main

import os # Used to find the script and create paths for file management
import shutil # Used to remove items, (characters, features, spells, kind of anything really. Not yet implemented)
import tkinter as tk # Runs the GUI
from PIL import Image, ImageTk

finn_encoding = "utf-8" # Used for file storing and reading with Ä Ö and Ås

# Configs and directories:
if True:
    script_dir = os.path.dirname(os.path.abspath(__file__)) # Finds script itself, 
    #                                                       used to construct further paths
    configs_dir = os.path.join(script_dir,"configs") # Stores settings
    items_dir = os.path.join(script_dir,"items") # Stores items
    spells_dir = os.path.join(script_dir,"spells") # Stores spells (Unimplemented)
    characters_dir = os.path.join(script_dir,"characters") # Stores characters (Started)
    feature_dir = os.path.join(script_dir,"features") # Stores character features (Unimplemented)
    dev_dir = os.path.join(script_dir, "developer") # Contains changelog and other micellaneous development related stuff
    changelog_dir = os.path.join(dev_dir, "changelogs")
    devnotes_dir = os.path.join(dev_dir, "notes")
    arts_dir = os.path.join(script_dir, "arts")

# files in directories:
if True:
    keywords_items_file = os.path.join(configs_dir,"keywords_items") # Stores keywords like "Cheap" and "Heavy"
    types_items_file = os.path.join(configs_dir,"types_items") # Stores types like "Consumable" and "Weapon"
    rarity_items_file = os.path.join(configs_dir,"rarity_items") # Stores rarities like "Rare" and "Cosmic"
    settings_file = os.path.join(configs_dir, "Settings") # Stores screen geometry and title-text
    color_file = os.path.join(configs_dir,"maincolor") # Stores theme
    charorigin_file = os.path.join(configs_dir,"character_origin") # Stores starting characteristics for creation

# icon directories
if True:
    icon_item_dir = os.path.join(arts_dir,"items")
    icon_stuff_dir = os.path.join(icon_item_dir,"stuff")
    icon_wearables_dir = os.path.join(icon_item_dir, "wearables")
    icon_weapons_dir = os.path.join(icon_item_dir, "weapons")



class Config:
    def __init__(self):
        self.configs = []
        with open(settings_file, "r") as file:
            for line in file:
                self.configs.append(str(line))

        print(f"Self configs: {self.configs}")
        self.settings_name = []
        self.settings_value = []
        self.color = ""

        for setting in self.configs:
            print(f"Accessing setting {setting}")
            content = setting.strip()
            content = content.split("=")
            if content[0] == "geometry":
                self.geometry = str(content[1])
            elif content[0] == "title":
                self.title = content[1]
            self.settings_name.append(content[0])
            self.settings_value.append(content[1])
        
        with open(color_file, "r") as file:
            coloringbook = file.read()
            colori = coloringbook.strip()
            self.color = colori

        if self.color == "black":
            self.back_color = "black"
            self.font_color = "black"
            self.title_color = "red"
        elif self.color == "white":
            self.back_color = "white"
            self.font_color = "black"
            self.title_color = "black"
                
            
        print(self.settings_name,
              self.settings_value)

    # Saves list of settings
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

    # Saves color to file.
    def savecolor(self, color):
        with open(color_file, "w") as file:
            file.write(color)

# Mainwindow class is for the user GUI and all its scenes.
# Creates itself as a tkinter window.
class MainWindow(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.settings = Config()
        try:
            self.geometry(self.settings.geometry)
        except:
            self.geometry("500x500")
        self.title(self.settings.title)
        self.config(bg=self.settings.color)
        self.buttons = []

        self.tooltipwin = tk.Toplevel(self)
        self.tooltipwin.withdraw()  # Start hidden
        self.tooltipwin.overrideredirect(True)  # Removes title bar for a floating effect
        self.tooltipframe = tk.Frame(self.tooltipwin, bg="black", bd=3)
        self.tooltipframe.pack()
        self.tooltip =  tk.Label(self.tooltipframe, text="Hello world", bg="white", fg="black", font=("Arial", 10), borderwidth=5,border=True)
        self.tooltip.pack()

        self.GUI_init()
    
    def update_color(self, color):
        self.config(bg=color)

        if color == "black":
            self.settings.back_color = "black"
            self.settings.font_color = "black"
            self.settings.title_color = "red"
        elif color == "white":
            self.settings.back_color = "white"
            self.settings.font_color = "black"
            self.settings.title_color = "black"
        self.settings_menu()




    def quitconfirm(self, button):
        button.destroy()
        self.buttons.remove(button)

        quit_frame = tk.Frame(self,bg=self.settings.back_color)
        quit_frame.pack(side="bottom")
        self.buttons.append(quit_frame)

        b_confirm = tk.Button(quit_frame, text="Confirm",command=lambda:quit(),width=10,bg="red")
        b_confirm.pack(side="left",padx=3)
        self.buttons.append(b_confirm)
        b_confirm.bind("<Enter>", lambda event: b_confirm.config(bg="yellow"))
        b_confirm.bind("<Leave>", lambda event: b_confirm.config(bg="red"))

        b_decline = tk.Button(quit_frame,text="Decline", command=self.GUI_init,width=10,bg="red")
        b_decline.pack(side="right",padx=3)
        self.buttons.append(b_decline)
        b_decline.bind("<Enter>", lambda event: b_decline.config(bg="yellow"))
        b_decline.bind("<Leave>", lambda event: b_decline.config(bg="red"))




    def charcreator_change_val(self, target, childlist,parent, value, cplabel, splabel): 
        # Character creator +1 -1 button activation

        # Extract values
        cpval = cplabel.cget("text")
        cpcontent = cpval.split(": ")
        current_cp = int(cpcontent[1])
        spval = splabel.cget("text")
        spcontent = spval.split(": ")
        current_sp = int(spcontent[1])
        targetval = target.cget("text")
        targetcontent = targetval.split(": ")
        currentval = int(targetcontent[1])

        # Check values
        print(f"Current value {currentval}, SP remaining {current_sp}, CP remaining {current_cp}")
        print(targetcontent[0])

        # Check type
        targetskill = targetcontent[0]
        if targetskill == "Body" or targetskill == "Mind" or targetskill == "Soul":
            if current_cp > 0 and value == "+1":
                currentval += 1
                current_cp -= 1
                targettext = f"{targetcontent[0]}: {str(currentval)}"
                target.config(text=targettext)
                cptext = f"Characteristic Points Remaining: {str(current_cp)}"
                cplabel.config(text=cptext)
                for btn in childlist:
                    btnval = btn.cget("text")
                    btnval = btnval.split(": ")
                    print(btnval)
                    valval = int(btnval[1])
                    valval += 1
                    newtext = f"{btnval[0]}: {valval}"
                    btn.config(text=newtext)
            elif currentval > 0 and value == "-1":
                currentval -= 1
                current_cp += 1
                targettext = f"{targetcontent[0]}: {str(currentval)}"
                target.config(text=targettext)
                cptext = f"Characteristic Points Remaining: {str(current_cp)}"
                cplabel.config(text=cptext)
                for btn in childlist:
                    btnval = btn.cget("text")
                    btnval = btnval.split(": ")
                    print(btnval)
                    valval = int(btnval[1])
                    valval -= 1
                    newtext = f"{btnval[0]}: {valval}"
                    btn.config(text=newtext)

        else:
            parentbtn = parent
            parentval = parentbtn.cget("text")
            parentval = parentval.split(": ")
            valval = int(parentval[1])
            if current_sp > 0 and value == "+1":
                currentval += 1
                current_sp -= 1
                targettext = f"{targetcontent[0]}: {str(currentval)}"
                target.config(text=targettext)
                sptext = f"Skill Points Remaining: {str(current_sp)}"
                splabel.config(text=sptext)
            elif (currentval > 0 and value == "-1") and currentval > valval:
                currentval -= 1
                current_sp += 1
                targettext = f"{targetcontent[0]}: {str(currentval)}"
                target.config(text=targettext)
                sptext = f"Skill Points Remaining: {str(current_sp)}"
                splabel.config(text=sptext)

    def change_popup(self, action):
        t = None
        match action:
            case "body":
                t = "Characteristic: Body\nWeak against Soul\nStrong against Mind"
            case "mind":
                t = "Characteristic: Mind\nWeak against Body\nStrong against Soul"
            case "soul":
                t = "Characteristic: Soul\nWeak against Mind\nStrong against Body"
            case "constitution":
                t= "Skill: Constitution\nIncreases Hit Points\nIncreases resistance against poisons and germs"
            case "endurance":
                t= "Skill: Endurance\nLong term muscle strength\nIncreases lung capacity"
            case "cunning":
                t= "Skill: Cunning\nIncreases stealth and movement\nAids in slippery actions"
            case "might":
                t= "Skill: Might\nShort term physical prowess\nPhysical damage, raw power"
            case "size":
                t= "Skill: Size\nIncreases your size attributes\nAffects carrying capacity"
            case "academics":
                t= "Skill: Academics\nOverall knowledge\nIncreases number of proficiencies"
            case "creativity":
                t= "Skill: Creativity\nCrafting recipes and opportunities\nHelps in some puzzles"
            case "focus":
                t= "Skill: Focus\nIncreases attempts that require focus\nResistance against distractions"
            case "resilience":
                t= "Skill: Resilience\nStrength of mind\nDefends against manipulation"
            case "tactics":
                t= "Skill: Tactics\nUsed for traps, bombs and schemes\nUsed to grant tactical support"
            case "arcana":
                t= "Skill: Arcana\nIncreases the number of your spells\nIncreases spell power"
            case "connection":
                t= "Skill: Connection\nRead others like a book\nManipulate both the world of beast and man"
            case "spirit":
                t= "Skill: Spirit\nUsed for out-of-body activities\nConnects you to the dead"
            case "faith":
                t= "Skill: Faith\nUnion with both the divine and the unholy\nUsed for both healing and necromancy"
            case "sense":
                t= "Skill: Sense\nEnhances your senses by arcane means\nIncreases defense against brutal attacks"
        self.tooltip.config(text=t)
            
    # Tooltip stuff
    def show_tooltip(self, action):
        self.change_popup(action)
        self.tooltipwin.deiconify()
        self.focus_force()
        self.tooltipwin.lift()
    
    def move_tooltip(self, event):
        self.tooltipwin.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
    
    def hide_tooltip(self, event):
    
        self.tooltipwin.withdraw()
    ###

    def character_creator(self): # Enter character creator
        for button in self.buttons:
            button.destroy()

        lines = []
        with open(charorigin_file, "r") as file:
            for line in file:
                if line != "\n":
                    line = line.strip()
                    lines.append(str(line))
        
        for line in lines:
            print(line)
        print(lines)



        label = tk.Label(self,text="Character Creator", font=30)
        label.pack(side="top", pady=5)
        self.buttons.append(label)

        pointframe = tk.Frame(self,bg=self.settings.back_color)
        pointframe.pack(side="top")
        self.buttons.append(pointframe)


        CPlabel = tk.Label(pointframe, text="Characteristic Points Remaining: 2")
        CPlabel.pack(side="left")
        self.buttons.append(CPlabel)

        SPlabel = tk.Label(pointframe, text = "Skill Points Remaining: 5")
        SPlabel.pack(side="right")
        self.buttons.append(SPlabel)

        mainframe = tk.Frame(self,bg=self.settings.back_color)
        mainframe.pack(side="top",pady=5)
        self.buttons.append(mainframe)

        charframe = None
        colors = ["red", "light blue", "yellow"]
        color = None
        
        bodybuttons = []
        mindbuttons = []
        soulbuttons = []
        parentbuttons = []

        buttonsets = [bodybuttons, mindbuttons, soulbuttons]
        phase = 0
        for line in lines:
            content = line.split("=")

            # frames for the three characteristics
            if content[0] == "name":
                continue
            if content[0] == "body" or content[0] == "mind" or content[0] == "soul":
                if content[0] == "mind":
                    phase = 1
                elif content[0] == "soul":
                    phase = 2
                charframe = tk.Frame(mainframe,bg=self.settings.back_color)
                charframe.pack(side="left",padx=15)
                self.buttons.append(charframe)

            #buttons for characteristics and their skills
            if content[0] == "body" or content[0] == "mind" or content[0] == "soul":
                color = colors[0]
                colors.remove(color)
                char = content[0].capitalize()
                val = content[1]

                buttonframe = tk.Frame(charframe,
                                       bg=self.settings.back_color)
                buttonframe.pack(side="top",pady=5)
                self.buttons.append(buttonframe)

                mainbutton = tk.Button(buttonframe, 
                                       text=f"{char}: {val}",
                                       width=10,
                                       bg=color,
                                       font=("Arial Black", 8),command=lambda c=content[0]: show_popup(c))
                mainbutton.bind("<Enter>",lambda event, c=content[0]: self.show_tooltip(c))
                mainbutton.bind("<Motion>", self.move_tooltip)
                mainbutton.bind("<Leave>", self.hide_tooltip)
                mainbutton.pack(anchor="center")
                self.buttons.append(mainbutton)
                parentbuttons.insert(phase, mainbutton)

                redu_button = tk.Button(buttonframe,
                                        text="-1",
                                        command=lambda b=mainbutton, l=buttonsets[phase]: self.charcreator_change_val(b,l,None, "-1", CPlabel, SPlabel),
                                        width=8)
                redu_button.pack(side="left",padx=2)
                self.buttons.append(redu_button)

                incr_button = tk.Button(buttonframe,
                                        text="+1",
                                        command=lambda b=mainbutton, l=buttonsets[phase]: self.charcreator_change_val(b,l,None, "+1",CPlabel, SPlabel),
                                        width=8)
                incr_button.pack(side="right",padx=2)
                self.buttons.append(incr_button)
            else:
                char = content[0].capitalize()
                val = content[1]

                buttonframe = tk.Frame(charframe,
                                       bg=self.settings.back_color)
                buttonframe.pack(side="top",pady=2)
                self.buttons.append(buttonframe)

                mainbutton = tk.Button(buttonframe, 
                                       text=f"{char}: {val}",
                                       width=12, 
                                       bg=color,
                                       command=lambda c=content[0]: show_popup(c))
                mainbutton.bind("<Enter>",lambda event, c=content[0]: self.show_tooltip(c))
                mainbutton.bind("<Motion>", self.move_tooltip)
                mainbutton.bind("<Leave>", self.hide_tooltip)
                mainbutton.pack(anchor="center")
                self.buttons.append(mainbutton)

                buttonsets[phase].append(mainbutton)

                redu_button = tk.Button(buttonframe,
                                        text="-1",
                                        command=lambda b=mainbutton, p=parentbuttons[phase]: self.charcreator_change_val(b,None,p, "-1",CPlabel, SPlabel),
                                        width=8)
                redu_button.pack(side="left",padx=2)
                self.buttons.append(redu_button)

                incr_button = tk.Button(buttonframe, text="+1",
                                        command=lambda b=mainbutton, p=parentbuttons[phase]: self.charcreator_change_val(b,None,p, "+1",CPlabel, SPlabel),
                                        width=8)
                incr_button.pack(side="right",padx=2)
                self.buttons.append(incr_button)
            

        

        self.create_back_btn("main")




    def character_loader(self):
        for entity in self.buttons:
            entity.destroy()
        
        mainlabel = tk.Label(self,text="Characters",
                             bg=self.settings.back_color,
                             font=("Arial Black", 30),
                             fg=self.settings.title_color)
        mainlabel.pack(side="top",pady=10)
        self.buttons.append(mainlabel)

        characters = []
        for file in os.listdir(characters_dir):
            characters.append(file)
        if len(characters) == 0:
            label = tk.Label(self, text="You have no characters",
                             fg=self.settings.title_color,
                             bg=self.settings.back_color,
                             font=20)
            label.pack(anchor="center")
            self.buttons.append(label)
        

        

        self.create_back_btn("main")
    
    def create_back_btn(self, type):
        match type:
            case "main":
                back_main = tk.Button(self,
                              text="Back",
                              font=10,
                              command=self.GUI_init,
                              width=20,
                              bg="red")
                back_main.pack(side="bottom")
                self.buttons.append(back_main)
                back_main.bind("<Enter>", lambda event: back_main.config(bg="yellow"))
                back_main.bind("<Leave>", lambda event: back_main.config(bg="red"))


    def devnotes(self):
        for entity in self.buttons:
            entity.destroy()

        label = tk.Label(self,text="Notes", font=("Arial Black", 30), fg=self.settings.title_color,bg=self.settings.back_color)
        label.pack(side="top")
        self.buttons.append(label)

        noteframe = tk.Frame(self,bg=self.settings.back_color)
        noteframe.pack(expand=True)
        self.buttons.append(noteframe)

        for file in os.listdir(devnotes_dir):
            print(file)
            filepath = os.path.join(devnotes_dir,file)
            filebutton = tk.Button(noteframe, text=f"Note: {file}",width=20,height=2, command=lambda f=filepath, o=self.devnotes:self.read_dev_file(f, o))
            filebutton.pack()
            self.buttons.append(filebutton)

        back_main = tk.Button(self,
                              text="Back",
                              font=10,
                              command=self.devlogs,
                              width=20,
                              bg="red")
        back_main.pack(side="bottom")
        self.buttons.append(back_main)

    def read_dev_file(self, path, origin):
        lines = []
        for entity in self.buttons:
            entity.destroy()

        textframe = tk.Frame(self,bg="gray")
        textframe.pack(anchor="center")
        self.buttons.append(textframe)

        with open(path, "r") as file:
            for line in file:
                lines.append(str(line))
        text = ""
        for line in lines:
            text += line+"\n"
        
        label = tk.Label(textframe, text=text, bg=self.settings.back_color, fg=self.settings.title_color, wraplength=500)
        label.pack()
        self.buttons.append(label)


        back_main = tk.Button(self,
                              text = "Back",
                              font = 10,
                              command = origin,
                              width = 20,
                              bg = "red")
        back_main.pack(side = "bottom")
        self.buttons.append(back_main)

    def changelog(self):
        for entity in self.buttons:
            entity.destroy()

        label = tk.Label(self,text = "Changelogs",
                         font = ("Arial Black", 30),
                         fg = self.settings.title_color,
                         bg = self.settings.back_color)
        label.pack(side="top")
        self.buttons.append(label)

        logframe = tk.Frame(self,
                            bg = self.settings.back_color)
        logframe.pack(expand = True)
        self.buttons.append(logframe)

        for file in os.listdir(changelog_dir):
            print(file)
            filepath = os.path.join(changelog_dir,file)
            filebutton = tk.Button(logframe,
                                   text = f"Version {file}",
                                   width = 20,
                                   height = 2,
                                   command = lambda f = filepath,
                                   o = self.changelog:self.read_dev_file(f, o))
            filebutton.pack()
            self.buttons.append(filebutton)

        back_main = tk.Button(self,
                              text = "Back",
                              font = 10,
                              command=self.devlogs,
                              width = 20,
                              bg = "red")
        back_main.pack(side = "bottom")
        self.buttons.append(back_main)

    def devlogs(self):
        for entity in self.buttons:
            entity.destroy()
        
        label = tk.Label(self,text = "Devlogs",
                         font = ("Arial Black", 30),
                         fg = self.settings.title_color,
                         bg = self.settings.back_color)
        label.pack(side="top")
        self.buttons.append(label)

        frame = tk.Frame(self,
                         bg = self.settings.back_color)
        frame.pack()
        self.buttons.append(frame)

        notebut = tk.Button(frame,
                            text = "Notes",
                            command = self.devnotes)
        notebut.pack()
        self.buttons.append(notebut)

        changebut = tk.Button(frame, text = "Changelog",
                              command = self.changelog)
        changebut.pack()
        self.buttons.append(changebut)

        back_main = tk.Button(self,
                              text = "Back",
                              font = 10,
                              command = self.GUI_init,
                              width = 20,
                              bg = "red")
        back_main.pack(side = "bottom")
        self.buttons.append(back_main)


    def GUI_init(self): # MAIN
        # Cleanup
        for entity in self.buttons:
            entity.destroy()
        

        mainframe = tk.Frame(self, bg = self.settings.back_color)
        mainframe.pack(anchor="center")
        self.buttons.append(mainframe)

        mainlabel = tk.Label(mainframe,
                             text = "Main Menu",
                             font = ("Arial Black", 30),
                             fg = self.settings.title_color,
                             bg = self.settings.back_color)
        mainlabel.pack(side = "top",pady = 10)
        self.buttons.append(mainlabel)

        newcharacter = tk.Button(mainframe,width=20,
                                 text="New Character",
                                 command=self.character_creator)
        newcharacter.pack(side="top",pady=2)
        self.buttons.append(newcharacter)
        newcharacter.bind("<Enter>", lambda event: newcharacter.config(bg="yellow"))
        newcharacter.bind("<Leave>", lambda event: newcharacter.config(bg="white"))
        

        loadcharacter = tk.Button(mainframe, width=20,
                                  text= "Load Character",
                                  command=self.character_loader)
        loadcharacter.pack(side="top",pady=2)
        self.buttons.append(loadcharacter)
        loadcharacter.bind("<Enter>", lambda event: loadcharacter.config(bg="yellow"))
        loadcharacter.bind("<Leave>", lambda event: loadcharacter.config(bg="white"))

        featurebutton = tk.Button(mainframe,width=20,
                                  text="Features Menu",
                                  command=self.features_menu)
        featurebutton.pack(side="top",pady=2)
        self.buttons.append(featurebutton)
        featurebutton.bind("<Enter>", lambda event: featurebutton.config(bg="yellow"))
        featurebutton.bind("<Leave>", lambda event: featurebutton.config(bg="white"))

        itembutton = tk.Button(mainframe,width=20,
                               text="Items Menu",
                               command=self.item_menu)
        itembutton.pack(side="top",pady=2)
        self.buttons.append(itembutton)
        itembutton.bind("<Enter>", lambda event: itembutton.config(bg="yellow"))
        itembutton.bind("<Leave>", lambda event: itembutton.config(bg="white"))

        settings_button = tk.Button(mainframe,width=20,
                                    text="Settings",
                                    command=self.settings_menu)
        settings_button.pack(side="top",pady=2)
        self.buttons.append(settings_button)
        settings_button.bind("<Enter>", lambda event: settings_button.config(bg="yellow"))
        settings_button.bind("<Leave>", lambda event: settings_button.config(bg="white"))

        devbut = tk.Button(mainframe,width=20,
                           text="Developer Logs",
                           command=self.devlogs)
        devbut.pack(side="top",pady=2)
        self.buttons.append(devbut)
        devbut.bind("<Enter>", lambda event: devbut.config(bg="yellow"))
        devbut.bind("<Leave>", lambda event: devbut.config(bg="white"))

        quit_button = tk.Button(self,text="QUIT",
                                command=lambda: self.quitconfirm(quit_button),
                                bg="red",font=10)
        quit_button.pack(side="bottom")
        self.buttons.append(quit_button)

    def clear(self):
        for item in self.buttons:
            item.destroy()
    
    def eliminate(self, object):
        self.buttons.remove(object)
        object.destroy()

    def add(self, object):
        self.buttons.append(object)

    def feature_creation(self):
        self.clear()

        back_feature = tk.Button(self,
                              text="Back",
                              font=10,
                              command=self.features_menu,
                              width=20,
                              bg="red")
        back_feature.pack(side="bottom")
        self.buttons.append(back_feature)


    def features_menu(self):
        for item in self.buttons:
            item.destroy()

        features = []

        for feat in os.listdir(feature_dir):
            item = []
            featpath = os.path.join(feature_dir, feat)
            total = feat, featpath
            features.append(total)
            print(f"Feature found in path {featpath}")
        print("Inspecting all found features by name and path")
        for item in features:
            print(item)
        
        label = tk.Label(self, text="Feature Menu",
                         font=("Arial Black", 20),
                         bg=self.settings.back_color,
                         fg=self.settings.title_color)
        label.pack(side="top")
        self.buttons.append(label)

        mainframe = tk.Frame(self, bg=self.settings.back_color)
        mainframe.pack(anchor="center")
        self.buttons.append(mainframe)

        featureframe = tk.Frame(mainframe)
        featureframe.grid(row=0,column=1,padx=5)
        self.add(featureframe)

        nextpage = tk.Button(mainframe, text="NEXT",
                             command=lambda: print("FEATURES NEXT-PAGE not yet implemented"))
        nextpage.grid(row=0,column=2)
        self.add(nextpage)

        prevpage = tk.Button(mainframe, text="PREV",
                             command=lambda: print("FEATURES PREV-PAGE not yet implemented"))
        prevpage.grid(row=0,column=0)
        self.add(prevpage)

        if len(features) == 0:
            infolabel = tk.Label(featureframe, text="No Features In Memory")
            infolabel.pack()
            self.add(infolabel)
        else:
            for item in features:
                name = item[0].replace("_", " ")
                name = name.capitalize()
                btn = tk.Button(featureframe, text=name,
                                command=lambda p=item[1],n=item[0]: self.codex_open("feature", p, n))
                btn.pack()
                self.add(btn)

        self.create_back_btn("main")

    def codex_open(self, type, path, name):
        self.clear()


        if type == "feature":
            name = name.replace("_", " ")
            name = name.capitalize()

            label = tk.Label(self, text=name.capitalize(),
                             bg=self.settings.back_color,
                             fg=self.settings.title_color, font=("Arial Black", 20))
            label.pack()
            self.add(label)

            sublabel = tk.Label(self,text=type.capitalize(),
                                bg=self.settings.back_color,
                                font=("Arial Black", 10),
                                fg=self.settings.title_color)
            sublabel.pack()
            self.add(sublabel)

            lorepaths = []
            requirements = []
            effects = []
            for content in os.listdir(path):
                contentpath = os.path.join(path, content)
                if content == "prerequisites":
                    requirements.append(contentpath)
                elif content == "effects":
                    effects.append(contentpath)
                else:
                    lorepaths.append(contentpath)
            print(f"Thingpaths: {lorepaths}")

            reqlabel = tk.Label(self,bg=self.settings.back_color, fg=self.settings.title_color,text="-= Prerequisites =-")
            reqlabel.pack()
            self.add(reqlabel)

            reqframe = tk.Frame(self, bg=self.settings.back_color)
            reqframe.pack()
            self.add(reqframe)

            for path in requirements:
                content = []
                with open(path, "r") as file:
                    for line in file:
                        content.append(line.strip())
                X = 0
                Y = 0
                for item in content:
                    item = item.split("=")
                    label = tk.Label(reqframe, text=f"{item[0].capitalize()}: {item[1]}")
                    label.grid(row=Y,column=X,padx=3)
                    if X <= 3:
                        X += 1
                    else:
                        X = 0
                        Y += 1
                    self.add(label)
            
            charlabel = tk.Label(self,bg=self.settings.back_color,fg=self.settings.title_color,text="-= Characteristic & Skill -Effects =-")
            charlabel.pack()
            self.add(charlabel)

            pointframe = tk.Frame(self,bg=self.settings.back_color)
            pointframe.pack()
            self.add(pointframe)

            traitlabel = tk.Label(self,bg=self.settings.back_color,fg=self.settings.title_color,text="-= Traits =-")
            traitlabel.pack()
            self.add(traitlabel)

            traitframe = tk.Frame(self,bg=self.settings.back_color)
            traitframe.pack()
            self.add(traitframe)

            for path in effects:
                content = []
                with open(path, "r") as file:
                    for line in file:
                        content.append(line.strip())
                chareffect = []
                skilleffect = []
                traiteffect = []
                for item in content:
                    item = item.split("=")
                    if item[0] != "trait":
                        if item[0] != "body" and item[0] != "mind" and item[0] != "soul":
                            skilleffect.append(item)
                        else:
                            chareffect.append(item)
                    else:
                        traiteffect.append(item)
                X = 0
                Y = 0
                for item in chareffect:
                    print(item)
                    t1 = item[0].capitalize()
                    t2 = item[1]
                    label = tk.Label(pointframe, text=f"{t1}: {t2}",bg=self.settings.back_color)
                    label.grid(row=Y, column=X, padx=3)
                    self.add(label)
                    if X <= 3:
                        X += 1
                    else:
                        X = 0
                        Y += 1

                for item in skilleffect:
                    print(item)
                    t1 = item[0].capitalize()
                    t2 = item[1]
                    label = tk.Label(pointframe, text=f"{t1}: {t2}")
                    label.grid(row=Y, column=X, padx=3)
                    self.add(label)
                    if X <= 3:
                        X += 1
                    else:
                        X = 0
                        Y += 1
                print("Moving on to traiteffects")
                for item in traiteffect:
                    print(item)
                    texti = item[1].capitalize()
                    label = tk.Label(traitframe, text=f"-{texti}", wraplength=1000)
                    label.pack(pady=3)
                    self.add(label)



        back_feature = tk.Button(self,
                              text="Back",
                              font=10,
                              command=self.features_menu,
                              width=20,
                              bg="red")
        back_feature.pack(side="bottom")
        self.buttons.append(back_feature)

    def open_item(self, item_path, itemname):
        print(item_path) # Debugging

        # Cleanup
        for entity in self.buttons:
            entity.destroy()

        item_desc = None
        item_keys = None
        item_rarity = None
        item_value = None
        item_weight = None
        item_type = None
        stuff_on_file = []
        keywords = []

        for file in os.listdir(item_path):
            print(item_path)
            print(file)
            stuff_path = os.path.join(item_path,file)
            print(stuff_path)
            stuff_name = file
            property = [stuff_name, stuff_path]
            stuff_on_file.append(property)

        for property in stuff_on_file:
            if property[0] == "type":
                with open(property[1], "r", encoding=finn_encoding) as file:
                    item_type = file.read()
            elif property[0] == "rarity":
                with open(property[1], "r", encoding=finn_encoding) as file:
                    item_rarity = file.read()
            elif property[0] == "desc":
                with open(property[1], "r", encoding=finn_encoding) as file:
                    item_desc = file.read()
            elif property[0] == "weight":
                with open(property[1], "r", encoding=finn_encoding) as file:
                    getgot = file.read()
                    if getgot != " " and getgot != "":
                        item_weight = getgot
            elif property[0] == "value":
                with open(property[1], "r", encoding=finn_encoding) as file:
                    getgot = file.read()
                    if getgot != " " and getgot != "":
                        item_value = getgot
            
            elif property[0] == "keywords":
                with open(property[1], "r", encoding=finn_encoding) as file:
                    for line in file:
                        keywords.append(line.strip())
                keystring = keywords[0]
                keywords.remove(keywords[0])
                for word in keywords:
                    keystring = f"{keystring}, {word}"
                item_keys = keystring

        print(itemname) # Debugging
        print(item_type)
        print(item_rarity)
        print(item_keys)
        print(item_desc)

        label = tk.Label(self, text=itemname,
                         font=("Arial Black", 20),
                         fg=self.settings.title_color,
                         bg=self.settings.back_color)
        label.pack(side="top",pady=10)
        self.buttons.append(label)

        rarityframe = tk.Frame(self,bg=self.settings.back_color)
        rarityframe.pack()
        self.buttons.append(rarityframe)

        raritydisplay = tk.Label(rarityframe, text=item_rarity)
        raritydisplay.pack(anchor="center",pady=3)
        self.buttons.append(raritydisplay)

        typeframe = tk.Frame(self,bg=self.settings.back_color)
        typeframe.pack()
        self.buttons.append(typeframe)

        typedisplay = tk.Label(typeframe, text=item_type)
        typedisplay.pack(anchor="center",pady=3)
        self.buttons.append(typedisplay)


        keyframe = tk.Frame(self,
                            bg = self.settings.back_color)
        keyframe.pack()
        self.buttons.append(keyframe)

        keydis = tk.Label(keyframe, text = item_keys)
        keydis.pack(anchor = ("center"),
                    pady = 3)
        self.buttons.append(keydis)

        if item_weight != None:
            weightframe = tk.Frame(self,
                                   bg=self.settings.back_color)
            weightframe.pack()
            self.buttons.append(weightframe)

            weightdis = tk.Label(weightframe, text = f"Weight: {item_weight}")
            weightdis.pack(anchor="center",
                           pady=3)
            self.buttons.append(weightdis)

        if item_value != None:
            valueframe = tk.Frame(self,
                                  bg=self.settings.back_color)
            valueframe.pack()
            self.buttons.append(valueframe)

            valuedis = tk.Label(valueframe, text = f"Value: {item_value}")
            valuedis.pack(anchor="center",
                          pady=3)
            self.buttons.append(valuedis)

        descframe = tk.Frame(self,
                             bg = self.settings.back_color)
        descframe.pack()
        self.buttons.append(descframe)

        descplay = tk.Label(descframe,
                            text=item_desc,
                            wraplength = 300,
                            justify = "left",
                            height = 15,
                            width = 50)
        descplay.pack(anchor="center",pady=3)
        self.buttons.append(descplay)

        bottomframe = tk.Frame(self,
                               bg = self.settings.back_color)
        bottomframe.pack(side="bottom")
        self.buttons.append(bottomframe)

        back_items = tk.Button(bottomframe,
                               text="Back",
                               font = 10,
                               command=self.item_menu,
                               width = 20,
                               bg ="pink")
        back_items.grid(row=0,column=1)
        self.buttons.append(back_items)

        delete_button = tk.Button(bottomframe,
                                  text = "Delete",
                                  bg = "red",
                                  width = 8,
                                  command=lambda f = bottomframe, p = item_path: self.item_delete_confirm(delete_button, f, p))
        delete_button.grid(row=0,column=0)
        self.buttons.append(delete_button)

        edit_button = tk.Button(bottomframe, text="Edit", width=8, bg="yellow")
        edit_button.grid(row=0,column=2)
        self.buttons.append(edit_button)
    

    # Destroy delete-button, replace with confirm button
    def item_delete_confirm(self, db, f, p):
        db.destroy() 

        confirmbutton = tk.Button(f, text="Confirm Deletion",
                                  command=lambda p=p:(item_delete(p), 
                                                      self.item_menu()))
        confirmbutton.grid(row=0,column=0)
        self.buttons.append(confirmbutton)


    # Item menu where items are displayed. Leads to item creation menu.
    def item_menu(self):
        for entity in self.buttons:
            entity.destroy()

        mainlabel = tk.Label(self, text="Item Menu",
                             font=("Arial Black", 20),
                             bg=self.settings.back_color,
                             fg=self.settings.title_color)
        mainlabel.pack(side="top",pady=10)
        self.buttons.append(mainlabel)

        items_frame = tk.Frame(self,bg=self.settings.back_color)
        items_frame.pack(anchor="center")
        self.buttons.append(items_frame)

        item_display_frame = tk.Frame(items_frame,
                                      bg=self.settings.back_color)
        item_display_frame.pack(anchor="center")
        self.buttons.append(items_frame)

        X = 0
        Y = 0
        for item in os.listdir(items_dir):
            item_path = os.path.join(items_dir, item)
            print(item)
            print(item_path)
            itemname = item.strip()
            itemname = itemname.replace("_", " ")
            if os.path.isdir(item_path):
                itembutton = tk.Button(item_display_frame,width=20,
                                       text=itemname,
                                       command=lambda this_item=item_path, itemname=itemname: self.open_item(this_item, itemname))
                itembutton.grid(row=X, column=Y)
                self.buttons.append(itembutton)
                if X == 4:
                    X = 0
                    Y += 1
                else:
                    X += 1
        
        self.create_back_btn("main")

        newitembutton = tk.Button(self, text="Add New Item",
                                  width=20,font=10,bg="yellow",
                                  command=self.item_creation)
        newitembutton.pack(side="bottom")
        self.buttons.append(newitembutton)


    # Menu for item creation
    def item_creation(self):
        for entity in self.buttons:
            entity.destroy()

        creationlabel = tk.Label(self,font=("Arial Black", 10),
                                 text="Item Creation",
                                 bg=self.settings.back_color,
                                 fg=self.settings.font_color)
        creationlabel.pack(side="top",pady=5)
        self.buttons.append(creationlabel)

        inputframe = tk.Frame(self)
        inputframe.pack(anchor="center")
        self.buttons.append(inputframe)

        nameframe = tk.Frame(inputframe)
        nameframe.pack()
        self.buttons.append(nameframe)

        nameentry = tk.Entry(nameframe,width=40, 
                             font=("Arial Black", 8))
        nameentry.insert(0, "Input item name")
        nameentry.pack(side="left")
        self.buttons.append(nameentry)
        
        rarityframe = tk.Frame(inputframe)
        rarityframe.pack()
        self.buttons.append(rarityframe)


        rarityentry = tk.Entry(rarityframe,width=40)
        rarityentry.insert(0, "Input item rarity")
        rarityentry.pack(side="left")
        self.buttons.append(rarityentry)

        raritybutton = tk.Button(rarityframe, text="P",
                                 command=lambda: self.get_saved_entries("item_rarity", target=rarityentry),
                                 height=1,width=2)
        raritybutton.pack(side="right")
        self.buttons.append(raritybutton)

        rarityclear = tk.Button(rarityframe, text="C",
                                command=lambda: rarityentry.delete(0, tk.END))
        rarityclear.pack(side="right")
        self.buttons.append(rarityclear)


        typeframe = tk.Frame(inputframe)
        typeframe.pack()
        self.buttons.append(typeframe)

        typeentry = tk.Entry(typeframe,width=40)
        typeentry.insert(0, "Input item type")
        typeentry.pack(side="left")
        self.buttons.append(typeentry)

        typebutton = tk.Button(typeframe,text="P",
                               command=lambda: self.get_saved_entries("item_type", target=typeentry),
                               height=1, width=2)
        typebutton.pack(side="right")
        self.buttons.append(typebutton)

        typeclear = tk.Button(typeframe,text="C",
                              command=lambda: typeentry.delete(0, tk.END))
        typeclear.pack(side="right")
        self.buttons.append(typeclear)

        keyframe = tk.Frame(inputframe)
        keyframe.pack()
        self.buttons.append(keyframe)

        keyentry = tk.Entry(keyframe, width=40)
        keyentry.insert(0, "Input item keywords (Light, Dark, Life...)")
        keyentry.pack(side="left")
        self.buttons.append(keyentry)

        keybutton = tk.Button(keyframe,text="P",
                              command=lambda: self.get_saved_entries("item_keyword", target=keyentry),
                              height=1, width=2)
        keybutton.pack(side="right")
        self.buttons.append(keybutton)

        keyclear = tk.Button(keyframe,text="C",
                             command=lambda: keyentry.delete(0, tk.END))
        keyclear.pack(side="right")
        self.buttons.append(keyclear)

        weightframe = tk.Frame(inputframe)
        weightframe.pack()
        self.buttons.append(weightframe)

        weightentry = tk.Entry(weightframe, width=40)
        weightentry.insert(0, "Input item weight, or leave empty")
        weightentry.pack(side="right")
        self.buttons.append(weightentry)

        priceframe = tk.Frame(inputframe)
        priceframe.pack()
        self.buttons.append(priceframe)
        priceentry = tk.Entry(priceframe, width=40)
        priceentry.insert(0, "Input item value")
        priceentry.pack(side="right")
        self.buttons.append(priceentry)


        descframe = tk.Frame(self)

        descframe.pack(anchor="center",pady=5)
        self.buttons.append(descframe)

        desclabel = tk.Label(descframe,text="Item Description")
        desclabel.pack(side="top")
        self.buttons.append(desclabel)

        desctext = tk.Text(descframe, width=50,height=5)
        desctext.pack()
        self.buttons.append(desctext)

        iconlabel = tk.Label(self)

        iconbutton = tk.Button(self, text="ICON", command=lambda l=iconlabel: self.get_icon(l))
        iconbutton.pack()
        self.buttons.append(iconbutton)
        
        iconlabel.pack()
        self.buttons.append(iconlabel)
        
        back_main = tk.Button(self, text="Back",
                              font=10,
                              command=self.item_menu,width=20,bg="red")
        back_main.pack(side="bottom")
        self.buttons.append(back_main)

        back_main.bind("<Enter>", lambda event: back_main.config(bg="yellow"))
        back_main.bind("<Leave>", lambda event: back_main.config(bg="red"))

        save_item = tk.Button(self, text = "Save item", font=10, command=lambda: (
            print(keyentry.get()),  # Print the keys value for debugging
            self.save_new_item(
                nameentry, 
                typeentry, 
                rarityentry, 
                keyentry,
                weightentry,
                priceentry,
                desctext
            ),
            self.item_menu()
        ))
        save_item.pack(side="bottom")
        self.buttons.append(save_item)
    
    def get_icon(self, target):
        temp = []
        displayed = []

        canvas = tk.Toplevel(self)
        canvas.geometry("300x300")
        canvas.title("Icon Selection")
        temp.append(canvas)

        categories = tk.Frame(canvas)
        categories.pack()
        temp.append(categories)

        showables = tk.Frame(canvas)
        showables.pack()
        temp.append(showables)

        for icontype in os.listdir(icon_item_dir):
            iconpath = os.path.join(icon_item_dir,icontype)
            text = icontype.capitalize()
            button = tk.Button(categories, 
                               text=text, 
                               command=lambda i=iconpath: self.display_icons(i, showables, displayed, target))
            button.pack(side="left")

        closebutton = tk.Button(canvas,text="Close", 
                                command=lambda x=temp: ([item.destroy() for item in x], target.configure(image=y)))
        closebutton.pack(side="bottom")
        temp.append(closebutton)

    def display_icons(self, path, target, list, label):
        for item in list:
            item.destroy()
        
        icons = []
        X = 0
        Y = 0
        for icon in os.listdir(path):
            print(path)
            iconpath = os.path.join(path,icon)
            print(iconpath)
            o_image = Image.open(iconpath)
            image = o_image.resize((32,32), 
                                   Image.LANCZOS)
            imagee = ImageTk.PhotoImage(image)
            icons.append(imagee)
            
            button = tk.Button(target, 
                               image=imagee, 
                               command=lambda p=imagee, l=label: self.setimage(p,l))
            button.grid(row=Y,column=X)
            list.append(button)
            if X == 5:
                Y += 1
                X = 0
            else:
                X += 1

    def setimage(self, image, label):
        label.image_ref = image
        label.config(image=image)

    # When user presses "P"-button, this function runs fetching data of the selected type
    def get_saved_entries(self, origin, target):
        temp = [] # Instead of clearing the scene as usual, this is used to clean the canvas
        extracted = [] # Data extracted from file
        list_of_contentlists = []
        used_file = None
        title = ""

        match origin: # Matches the selected type to the correct file
            case "item_type":
                used_file = types_items_file
                title = "Type Selection"
            case "item_rarity":
                used_file = rarity_items_file
                title = "Rarity Selection"
            case "item_keyword":
                used_file = keywords_items_file
                title = "Keyword Selection"
        quicktest = tk.Toplevel(root)
        quicktest.geometry("200x200")
        quicktest.title("UWU")
        temp.append(quicktest)

        canvas = tk.Canvas(quicktest, width=400, height=400, bg="gray")
        canvas.pack(fill="both",expand=True)
        temp.append(canvas)

        label = tk.Label(canvas, text=title)
        label.pack(side="top")
        temp.append(label)

        closebutton = tk.Button(canvas,text="Close",command=lambda x=temp: [item.destroy() for item in x])
        closebutton.pack(side="bottom")
        temp.append(closebutton)

        new_ = tk.Button(canvas, text="Add New", command=lambda: self.append_new_entry(used_file, temp))
        new_.pack(side="bottom")
        temp.append(new_)

        buttonframe = tk.Frame(canvas)
        buttonframe.pack(side="bottom")
        
        temp.append(buttonframe)
        
        with open(used_file, "r") as file:
            for line in file:
                extracted.append(str(line))
        extracted.sort()
        if len(extracted) > 8:
            newlist = []
            X = 0
            for entry in extracted:
                newlist.append(entry)
                X += 1
                if X == 8:
                    list_of_contentlists.append(newlist)
                    newlist = []
                    X = 0
        X = 0
        Y = 0
        Z = 0

        for entry in list_of_contentlists[Z]:
            print(entry)

        for x in extracted:
            if origin != "item_keyword": # Keywords act a bit differently than type and rarity, as they are separated with ", "s
                button = tk.Button(buttonframe, text=x, width=10,height=2,
                                   command=lambda insertable=x: (target.delete(0, tk.END), target.insert(0, insertable)))
            else:
                button = tk.Button(buttonframe, text=x, width=10, height=2,
                                   command=lambda l=len(target.get()), insertable=(x+", "): target.insert(l, insertable))
            button.grid(row=Y, column=X)
            if X == 3:
                X = 0
                Y += 1
            else:
                X += 1
            temp.append(button)


    # Honstly I can't remember what this was for.
    def append_new_entry(self, used_file, temp):
        for item in temp:
            item.destroy()
        temppu = []
        content = []
        save_these = []
        with open(used_file, "r") as file:
            for line in file:
                content.append(str(line).strip())

        entrycanvas = tk.Canvas(self, width=400, height=400, bg="light blue")
        entrycanvas.pack(side="top",fill="both",expand=True)
        temppu.append(entrycanvas)

        label = tk.Label(entrycanvas, text="New Entries")
        label.pack(side="top")
        temppu.append(label)

        closebutton = tk.Button(entrycanvas,
                                text="Close",
                                command=lambda: (all(item.destroy() for item in temppu)))
        closebutton.pack(side="bottom")
        temppu.append(closebutton)

        entryframes = tk.Entry(entrycanvas, bg="light blue")
        entryframes.pack(anchor="center")
        temppu.append(entryframes)
        X = 0
        Y = 0
        for entry in content:
            entrance = tk.Entry(entryframes,width=15)
            entrance.insert(0, entry)
            entrance.grid(row=X,column=Y)
            temppu.append(entrance)
            if X ==3:
                X = 0
                Y += 1
            else:
                X += 1
        newntry = tk.Entry(entryframes,width=15)
        newntry.grid(row=X, column=Y)
        temppu.append(newntry)

        savebuttons = tk.Button(entrycanvas,
                                text="Save",
                                command= lambda: self.save_action(newntry.get(),content, temppu, used_file))
        savebuttons.pack(side="bottom")
        temppu.append(newntry)


    # Creates the new entry to the selected list, be it type, rarity or keyword.
    def save_action(self, new, content, temppu, used_file):
        print(new)
        print(temppu)
        print(content)
        content.append(new)  # Append new data to content
        for item in temppu:  # Destroy all items in the temporary list
            item.destroy()
        self.insert_new_list(used_file, content)  # Insert the new list
        self.item_creation()  # Call the item creation method


    # Saves the new list content to their own file
    def insert_new_list(self, chosenfile, list):
        with open(chosenfile, "w") as file:
            for line in list:
                if line != "" and line != " ":
                    file.write(str(line)+"\n")


    def save_new_item(self, name_entry, type_entry, rarity_entry, keys_entry, weight_entry, value_entry, desc_entry):

        # Get variables from entries
        keys = keys_entry.get()
        name = name_entry.get()
        rarity = rarity_entry.get()
        type = type_entry.get()
        weight = weight_entry.get()
        value = value_entry.get()
        desc = desc_entry.get("1.0", "end")
        print(keys)
        name_with_lines = name.replace(" ", "_")
        new_item_path = os.path.join(items_dir, name_with_lines)
        
        stringi = ""
        for i in keys:
            stringi = f"{stringi}, {i}"

        endkeys = []
        keylist = keys.split(", ")
        for key in keylist:
            endkeys.append(key)
        print(endkeys)

        # Finalize item saving process
        os.makedirs(new_item_path, exist_ok=True)
        name_path = os.path.join(new_item_path, "name")
        with open(name_path, "w", encoding=finn_encoding) as file:
            file.write(str(name))

        raritypath = os.path.join(new_item_path, "rarity")
        with open(raritypath, "w", encoding=finn_encoding) as file:
            file.write(str(rarity))

        key_path = os.path.join(new_item_path, "keywords")
        with open(key_path, "w", encoding=finn_encoding) as file:
            for i in endkeys:
                file.write(i+"\n")
        
        type_path = os.path.join(new_item_path, "type")
        with open(type_path, "w", encoding=finn_encoding) as file:
            file.write(type)
        
        value_path = os.path.join(new_item_path, "value")
        with open(value_path, "w", encoding=finn_encoding) as file:
            file.write(value)
        
        weight_path = os.path.join(new_item_path, "weight")
        with open(weight_path, "w", encoding=finn_encoding) as file:
            file.write(weight)

        descpath = os.path.join(new_item_path, "desc")
        with open(descpath, "w", encoding=finn_encoding) as file:
            file.write(desc)
        print("Item successfully saved!")
         

        
        
    # Scene for settings display. 
    def settings_menu(self):
        # Clean previous scene
        for entity in self.buttons:
            entity.destroy()
        
        # Settings are shown in this frame vvvvv
        setting_frame = tk.Frame(self, bg=self.settings.back_color)
        setting_frame.pack(anchor="center")
        setting_content = []
        self.buttons.append(setting_frame)
        print("Setting frame created")

        setting_label = tk.Label(setting_frame, text="SETTINGS",
                                 font=("Arial Black", 20),
                                 bg=self.settings.back_color,
                                 fg=self.settings.title_color)
        setting_label.pack(side="top",pady=10)
        self.buttons.append(setting_label)
        print("Setting label created")

        # Fetch settings geometry and title
        index = 0
        for setting in self.settings.settings_name:
            print(self.settings.settings_name)
            print(setting)
            setting = setting.capitalize()
            #Setting frame
            set = tk.Frame(setting_frame, bg=self.settings.back_color)
            set.pack(anchor="n",pady=5)
            self.buttons.append(set)
            # Setting label
            label = tk.Label(set,
                             text=setting,
                             width=10,
                             bg=self.settings.back_color,
                             fg=self.settings.title_color)
            label.pack(side="left",padx=3)
            self.buttons.append(label)
            # Setting entry
            entry = tk.Entry(set)
            entry.pack(side="right", padx=3)
            entry.insert(0, self.settings.settings_value[index])
            self.buttons.append(entry)
            setting_content.append(entry)

            index += 1

        # Fetch setting color
        colorframe = tk.Frame(setting_frame,
                              bg=self.settings.back_color)
        colorframe.pack(side="bottom")
        self.buttons.append(colorframe)

        label = tk.Label(colorframe,
                         bg=self.settings.back_color,
                         fg=self.settings.title_color,
                         text="Color Selection")
        label.pack(side="top")
        self.buttons.append(label)
        
        colors = ["black", "white"]
        for c in colors:
            button = tk.Button(colorframe,
                               bg=c,
                               borderwidth=5,
                               highlightcolor="yellow",
                               highlightthickness=5, 
                               command= lambda c=c: (self.update_color(c), # Updates current theme color
                                                     self.settings.savecolor(c)), # Saves current theme color
                                                     width=2,
                                                     height=1)
            button.pack(side="left",padx=5)
            self.buttons.append(button)

        # Throws the values to be activated and saved.
        save_button = tk.Button(setting_frame, text="SAVE", command=lambda: self.setting_change(setting_content))
        save_button.pack(side="bottom",pady=5)

        # Return to main menu scene
        self.create_back_btn("main")


    # Inputs come from the settings menu, and affect the screen geometry, title and background color. Through here they move to configs class to be saved on file.
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
        self.settings.save(savelist)


def show_popup(source):
    global root
    
    popup = tk.Toplevel(root, bg=root.settings.back_color)
    popup.geometry("400x400")
    popup.title(f"CODEX POPUP: {source.capitalize()}")

    
    l_text = None
    d_text = None
    d_text2 = None
    match source:
        case "body": # All the 'beat em up'-stuff goes here.
            l_text = "Characteristic: Body"
            d_text = "Body is the main characteristic for those who use and manipulate the environment through pure muscle and might."
            d_text2 = "It allows for breaking things with hands, moving things so heavy no-one else could, and instilling respect with mere presence."
            r_text = "Represents the total greatness of your physical temple. Weak against: Soul. Strong against: Mind"
        case "constitution":
            l_text = "Skill: Constitution"
            d_text = "This skill allows you to withstand poisons and germs."
            d_text2 = "In addition, increased constitution also grants you bonus HP."
            r_text = "Represents your body-health and well-being."
        case "endurance":
            l_text = "Skill: Endurance"
            d_text = "With endurance you can withstand under physical pressure and strife."
            d_text2 = "Unlike with might that touches on more short-term execution, endurance focuses on long-term stability and balance."
            r_text = "Represents your lung-capacity and muscle-strength under long-term duress."
        case "cunning":
            l_text = "Skill: Cunning"
            d_text = "With a cunning body you can slip through narrow spaces and move faster in shadows without being seen."
            d_text2 = "Useful for scoundrels and rogues of all types."
            r_text = "Represents your stealth, fine hand-eye coordination and ability to not be seen."
        case "might":
            l_text = "Skill: Might"
            d_text = "A raw short-term burst of power is granted by might. Used to operate cannons by yourself, or violently tear open steel-doors."
            d_text2 = "Might also affects how much damage you deal with physical attacks."
            r_text = "Represents your capacity to perform short-term actions requiring physical prowess."
        case "size":
            l_text = "Skill: Size"
            d_text = "Your carrying capacity is affected by how great a body you have, but increased size also increases the capacity by quite the margin."
            d_text2 = "With size your presence is also greatly affected, making you seem like the bigger threat. Useful when taunting your enemies."
            r_text = "Represents your height, weight and mass. Can easily be turned into a tool of intimidation."
        ####
        case "mind": # All the guns, traps and explosives go here
            l_text = "Characteristic: Mind"
            d_text = "Strategists and tacticians use their minds to construct the most deceitful traps and plans. With great mind comes great responsibility."
            d_text2 = "Your mind characteristic determines how much you know, how much you learn, and how well you can analyze."
            r_text = "Represents the strength of your mind. Weak against: Body. Strong against: Soul."
        case "academics":
            l_text = "Skill: Academics"
            d_text = "An important skill for historians and lifelong learners. Academics grants you the passive ability to know random tidbits of information."
            d_text2 = "The higher your academics-score, the more in-depth information about subjects you can muster."
            r_text = "Represents your body of knowledge, affecting the number of proficiencies you can have."
        case "creativity":
            l_text = "Skill: Creativity"
            d_text = "With creativity you can build items like weapons and armor, find alternative uses for objects and solve problems pure logic cannot."
            d_text2 = "With increased creativity you can craft, maintain and upgrade better items, both for yourself and your team."
            r_text = "Represents your creative mind, granting more crafting opportunities."
        case "focus":
            l_text = "Skill: Focus"
            d_text = "With focus you can delve into your mind-palace during lockpicking, puzzle-solving and problem-analysis."
            d_text2 = "The greater your focus, the harder puzzles you can attempt, the harder you are to distract, the easier to determine weaknesses."
            r_text = "Represents your ability to not be distracted, and number of attempts you can try something."
        case "resilience":
            l_text = "Skill: Resilience"
            d_text = "The resilience of mind is your gift against mind-control and manipulation."
            d_text2 = "With resilience you are less likely to fall victim to mindgames, under effects of emotions like fear, charm and so on."
            r_text = "Represents your resistance against spells and effects that affect mind."
        case "tactics":
            l_text = "Skill: Tactics"
            d_text = "Tactics opens up a new alley of advancement. You are able to create and use traps, bombs and schemes."
            d_text2 = "Each point in tactics opens new heights for pyromanic and dangerous activities."
            r_text = "Represents your tactical mind and capabilities"
        ####
        case "soul": # All the magic and religious stuff is here.
            l_text = "Characteristic: Soul"
            d_text = "While others use muscles to break doors, and mind to find a way around it, you walk through it."
            d_text2 = "Soul opens up paths of arcane, granting you the ability to not just bend it, but weave it."
            r_text = "Represents the strength of your soul. Weak against: Mind. Strong against: Body"
        case "arcana":
            l_text = "SKill: Arcana"
            d_text = "Your aptitude to magic, the Arcana, is the key to how many spells you can know, how strong ones you can know."
            d_text2 = "Points in arcana determine the strength of your spells, what rituals you can perform, and so on. Extremely important for mages."
            r_text = "Represents your magical abilities."
        case "connection":
            l_text = "Skill: Connection"
            d_text = "With connection you can sense the feelings, emotions, even thoughts of others. It is both a skill of great good, and great evil."
            d_text2 = "You can manipulate others. You can use their fears, or calm them. You can make friends, or break friendships of others."
            r_text = "Represents your connection with not just the emotions of others, but also with nature itself."
        case "spirit":
            l_text = "Skill: Spirit"
            d_text = "With spirit you can separate your soul from your body for short periods of time. In this form, you are able to do things others consider impossible."
            d_text2 = "The higher your spirit, the greater the acts you can perform outside your body."
            r_text = "Represents your ability to interact with objects outside your mortal shell."
        case "faith":
            l_text = "Skill: Faith"
            d_text = "You understand and feel the presence of divinity and those unholy. With faith, one can turn the tide of battle through miracles of prayer."
            d_text2 = "Clerics and priests, through faith alone have access to spells and rituals that grant communication with and summoning of holy and unholy beings."
            r_text = "Represents your connection with the heights of divinity, and depths of the unholy."
        case "sense":
            l_text = "Skill: Sense"
            d_text = "Your soul acts as a sixth sense, providing you benefits for each other sense."
            d_text2 = "You can sense patterns in others, you can see the movement and know what happens next. You can feel the change."
            r_text = "Represents your ability to survive against brutal attacks, and bonus to your overall senses."

    wrappi = 200

    label = tk.Label(popup,text=l_text, bg=root.settings.back_color, fg=root.settings.title_color, font=("Arial Black", 10))
    label.pack(side="top",pady=5)

    displayframe1 = tk.Frame(popup)
    displayframe1.pack(pady=5)

    textplay1 = tk.Label(displayframe1, text=d_text,wraplength=wrappi)
    textplay1.pack()

    disframe2 = tk.Frame(popup)
    disframe2.pack(pady=5)

    ddisplay = tk.Label(disframe2, text=d_text2,wraplength=wrappi)
    ddisplay.pack()

    disframe3 = tk.Frame(popup)
    disframe3.pack(pady=5)

    textlast = tk.Label(disframe3, text=r_text, wraplength=wrappi)
    textlast.pack()

    infotext = tk.Label(popup,text="This popup is closed after 30 seconds.",  bg=root.settings.back_color, fg=root.settings.title_color)
    infotext.pack(side="bottom")

    popup.after(30000, popup.destroy)


    
# Used to delete items from the items directory, through item profiles.
def item_delete(path):
    shutil.rmtree(path)



root = MainWindow() # Creates the main window during startup



tk.mainloop()



