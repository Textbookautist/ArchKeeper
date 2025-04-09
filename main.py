# Main

import os
import shutil
import tkinter as tk

finn_encoding = "utf-8"

# Configs and directories:
if True:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    configs_dir = os.path.join(script_dir,"configs")
    items_dir = os.path.join(script_dir,"items")
    spells_dir = os.path.join(script_dir,"spells")
    characters_dir = os.path.join(script_dir,"characters")
    feature_dir = os.path.join(script_dir,"features")

# files in directories:
if True:
    keywords_items_file = os.path.join(configs_dir,"keywords_items")
    types_items_file = os.path.join(configs_dir,"types_items")
    rarity_items_file = os.path.join(configs_dir,"rarity_items")
    settings_file = os.path.join(configs_dir, "Settings")
    color_file = os.path.join(configs_dir,"maincolor")
    charorigin_file = os.path.join(configs_dir,"character_origin")

def item_delete(path):
    shutil.rmtree(path)



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

    def savecolor(self, color):
        with open(color_file, "w") as file:
            file.write(color)


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

        b_confirm = tk.Button(quit_frame, text="Confirm",command=lambda:quit())
        b_confirm.pack(side="left",padx=3)
        self.buttons.append(b_confirm)

        b_decline = tk.Button(quit_frame,text="Decline", command=self.GUI_init)
        b_decline.pack(side="right",padx=3)
        self.buttons.append(b_decline)

    def charcreator_change_val(self, target, value, cplabel, splabel): # Character creator +1 -1 button activation

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
            elif currentval > 0 and value == "-1":
                currentval -= 1
                current_cp += 1
                targettext = f"{targetcontent[0]}: {str(currentval)}"
                target.config(text=targettext)
                cptext = f"Characteristic Points Remaining: {str(current_cp)}"
                cplabel.config(text=cptext)

        else:
            if current_sp > 0 and value == "+1":
                currentval += 1
                current_sp -= 1
                targettext = f"{targetcontent[0]}: {str(currentval)}"
                target.config(text=targettext)
                sptext = f"Characteristic Points Remaining: {str(current_sp)}"
                splabel.config(text=sptext)
            elif currentval > 0 and value == "-1":
                currentval -= 1
                current_sp += 1
                targettext = f"{targetcontent[0]}: {str(currentval)}"
                target.config(text=targettext)
                sptext = f"Characteristic Points Remaining: {str(current_sp)}"
                splabel.config(text=sptext)

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

        SPlabel = tk.Label(pointframe, text = "Skill Points remaining: 5")
        SPlabel.pack(side="right")
        self.buttons.append(SPlabel)

        mainframe = tk.Frame(self,bg=self.settings.back_color)
        mainframe.pack(side="top",pady=5)
        self.buttons.append(mainframe)

        charframe = None
        colors = ["red", "light blue", "yellow"]
        color = None
        

        for line in lines:
            content = line.split("=")
            # frames for the three characteristics
            if content[0] == "name":
                continue
            if content[0] == "body" or content[0] == "mind" or content[0] == "soul":
                charframe = tk.Frame(mainframe,bg=self.settings.back_color)
                charframe.pack(side="left",padx=15)
                self.buttons.append(charframe)
            #buttons for characteristics and their skills
            if content[0] == "body" or content[0] == "mind" or content[0] == "soul":
                color = colors[0]
                colors.remove(color)
                char = content[0].capitalize()
                val = content[1]

                buttonframe = tk.Frame(charframe,bg=self.settings.back_color)
                buttonframe.pack(side="top",pady=5)
                self.buttons.append(buttonframe)

                mainbutton = tk.Button(buttonframe,  text=f"{char}: {val}",width=10, bg=color, font=("Arial Black", 8))
                mainbutton.pack(anchor="center")
                self.buttons.append(mainbutton)

                redu_button = tk.Button(buttonframe, text="-1", command=lambda b=mainbutton: self.charcreator_change_val(b, "-1",CPlabel, SPlabel),width=8)
                redu_button.pack(side="left",padx=2)
                self.buttons.append(redu_button)

                incr_button = tk.Button(buttonframe, text="+1", command=lambda b=mainbutton: self.charcreator_change_val(b, "+1",CPlabel, SPlabel),width=8)
                incr_button.pack(side="right",padx=2)
                self.buttons.append(incr_button)
            else:
                char = content[0].capitalize()
                val = content[1]

                buttonframe = tk.Frame(charframe,bg=self.settings.back_color)
                buttonframe.pack(side="top",pady=2)
                self.buttons.append(buttonframe)

                mainbutton = tk.Button(buttonframe,  text=f"{char}: {val}",width=12, bg=color)
                mainbutton.pack(anchor="center")
                self.buttons.append(mainbutton)

                redu_button = tk.Button(buttonframe, text="-1", command=lambda b=mainbutton: self.charcreator_change_val(b, "-1",CPlabel, SPlabel),width=8)
                redu_button.pack(side="left",padx=2)
                self.buttons.append(redu_button)

                incr_button = tk.Button(buttonframe, text="+1", command=lambda b=mainbutton: self.charcreator_change_val(b, "+1",CPlabel, SPlabel),width=8)
                incr_button.pack(side="right",padx=2)
                self.buttons.append(incr_button)
            

        

        back_main = tk.Button(self, text="Back", font=10, command=self.GUI_init, width=20,bg="red")
        back_main.pack(side="bottom")
        self.buttons.append(back_main)

    def character_loader(self):
        for entity in self.buttons:
            entity.destroy()
        
        mainlabel = tk.Label(self,text="Characters",bg=self.settings.back_color,font=("Arial Black", 30),fg=self.settings.title_color)
        mainlabel.pack(side="top",pady=10)
        self.buttons.append(mainlabel)

        characters = []
        for file in os.listdir(characters_dir):
            characters.append(file)
        if len(characters) == 0:
            label = tk.Label(self, text="You have no characters", fg=self.settings.title_color,bg=self.settings.back_color,font=20)
            label.pack(anchor="center")
            self.buttons.append(label)
        

        

        back_main = tk.Button(self, text="Back", font=10, command=self.GUI_init, width=20,bg="red")
        back_main.pack(side="bottom")
        self.buttons.append(back_main)
    
    def GUI_init(self): # MAIN
        for entity in self.buttons:
            entity.destroy()
        mainframe = tk.Frame(self, bg=self.settings.back_color)
        mainframe.pack(anchor="center")
        self.buttons.append(mainframe)

        mainlabel = tk.Label(mainframe, text="Main Menu", font=("Arial Black", 30), fg=self.settings.title_color,bg=self.settings.back_color)
        mainlabel.pack(side="top",pady=10)
        self.buttons.append(mainlabel)

        newcharacter = tk.Button(mainframe,width=20,text="New Character",command=self.character_creator)
        newcharacter.pack(side="top",pady=2)
        self.buttons.append(newcharacter)

        loadcharacter = tk.Button(mainframe, width=20, text= "Load Character", command=self.character_loader)
        loadcharacter.pack(side="top",pady=2)
        self.buttons.append(loadcharacter)

        itembutton = tk.Button(mainframe,width=20,text="Items Menu", command=self.item_menu)
        itembutton.pack(side="top",pady=2)
        self.buttons.append(itembutton)

        settings_button = tk.Button(mainframe,width=20, text="Settings", command=self.settings_menu)
        settings_button.pack(side="top",pady=2)
        self.buttons.append(settings_button)

        quit_button = tk.Button(self,text="QUIT",command=lambda: self.quitconfirm(quit_button))
        quit_button.pack(side="bottom")
        self.buttons.append(quit_button)

    

    def open_item(self, item_path, itemname):
        print(item_path)
        for entity in self.buttons:
            entity.destroy()
        item_desc = None
        item_keys = None
        item_rarity = None
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
            
            elif property[0] == "keywords":
                with open(property[1], "r", encoding=finn_encoding) as file:
                    for line in file:
                        keywords.append(line.strip())
                keystring = keywords[0]
                keywords.remove(keywords[0])
                for word in keywords:
                    keystring = f"{keystring}, {word}"
                item_keys = keystring
        print(itemname)
        print(item_type)
        print(item_rarity)
        print(item_keys)
        print(item_desc)

        label = tk.Label(self, text=itemname, font=("Arial Black", 20),fg=self.settings.title_color, bg=self.settings.back_color)
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


        keyframe = tk.Frame(self,bg=self.settings.back_color)
        keyframe.pack()
        self.buttons.append(keyframe)

        keydis = tk.Label(keyframe, text = item_keys)
        keydis.pack(anchor=("center"),pady=3)
        self.buttons.append(keydis)

        descframe = tk.Frame(self,bg=self.settings.back_color)
        descframe.pack()
        self.buttons.append(descframe)

        descplay = tk.Label(descframe, text=item_desc,wraplength=300, justify="left",height=20,width=50)
        descplay.pack(anchor="center",pady=3)
        self.buttons.append(descplay)

        bottomframe = tk.Frame(self,bg=self.settings.back_color)
        bottomframe.pack(side="bottom")
        self.buttons.append(bottomframe)

        back_items = tk.Button(bottomframe, text="Back", font=10, command=self.item_menu,width=20,bg="pink")
        back_items.grid(row=0,column=1)
        self.buttons.append(back_items)

        delete_button = tk.Button(bottomframe, text="Delete", bg="red",width=8, command=lambda f = bottomframe, p = item_path: self.item_delete_confirm(delete_button, f, p))
        delete_button.grid(row=0,column=0)
        self.buttons.append(delete_button)

        edit_button = tk.Button(bottomframe, text="Edit", width=8, bg="yellow")
        edit_button.grid(row=0,column=2)
        self.buttons.append(edit_button)
    
    def item_delete_confirm(self, db, f, p):
        db.destroy()
        confirmbutton = tk.Button(f, text="Confirm Deletion", command=lambda p=p:(item_delete(p), self.item_menu()))
        confirmbutton.grid(row=0,column=0)
        self.buttons.append(confirmbutton)

    
    def item_menu(self):
        for entity in self.buttons:
            entity.destroy()

        mainlabel = tk.Label(self, text="Item Menu", font=("Arial Black", 20),bg=self.settings.back_color, fg=self.settings.title_color)
        mainlabel.pack(side="top",pady=10)
        self.buttons.append(mainlabel)

        items_frame = tk.Frame(self,bg=self.settings.back_color)
        items_frame.pack(anchor="center")
        self.buttons.append(items_frame)

        item_display_frame = tk.Frame(items_frame,bg=self.settings.back_color)
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
                itembutton = tk.Button(item_display_frame,width=20, text=itemname, command=lambda this_item=item_path, itemname=itemname: self.open_item(this_item, itemname))
                itembutton.grid(row=X, column=Y)
                self.buttons.append(itembutton)
                if X == 4:
                    X = 0
                    Y += 1
                else:
                    X += 1
        
        back_main = tk.Button(self, text="Back", font=10, command=self.GUI_init,width=20,bg="red")
        back_main.pack(side="bottom")
        self.buttons.append(back_main)

        newitembutton = tk.Button(self, text="Add New Item",width=20,font=10,bg="yellow",command=self.item_creation)
        newitembutton.pack(side="bottom")
        self.buttons.append(newitembutton)

    def item_creation(self):
        for entity in self.buttons:
            entity.destroy()

        creationlabel = tk.Label(self,font=("Arial Black", 10),text="Item Creation",bg=self.settings.back_color,fg=self.settings.font_color)
        creationlabel.pack(side="top",pady=5)
        self.buttons.append(creationlabel)

        inputframe = tk.Frame(self)
        inputframe.pack(anchor="center")
        self.buttons.append(inputframe)

        nameframe = tk.Frame(inputframe)
        nameframe.pack()
        self.buttons.append(nameframe)

        nameentry = tk.Entry(nameframe,width=40, font=("Arial Black", 8))
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

        raritybutton = tk.Button(rarityframe, text="P", command=lambda: self.get_saved_entries("item_rarity", target=rarityentry), height=1,width=2)
        raritybutton.pack(side="right")
        self.buttons.append(raritybutton)

        rarityclear = tk.Button(rarityframe, text="C", command=lambda: rarityentry.delete(0, tk.END))
        rarityclear.pack(side="right")
        self.buttons.append(rarityclear)


        typeframe = tk.Frame(inputframe)
        typeframe.pack()
        self.buttons.append(typeframe)

        typeentry = tk.Entry(typeframe,width=40)
        typeentry.insert(0, "Input item type")
        typeentry.pack(side="left")
        self.buttons.append(typeentry)

        typebutton = tk.Button(typeframe,text="P",command=lambda: self.get_saved_entries("item_type", target=typeentry), height=1, width=2)
        typebutton.pack(side="right")
        self.buttons.append(typebutton)

        typeclear = tk.Button(typeframe,text="C",command=lambda: typeentry.delete(0, tk.END))
        typeclear.pack(side="right")
        self.buttons.append(typeclear)

        keyframe = tk.Frame(inputframe)
        keyframe.pack()
        self.buttons.append(keyframe)

        keyentry = tk.Entry(keyframe, width=40)
        keyentry.insert(0, "Input item keywords (Light, Dark, Life...)")
        keyentry.pack(side="left")
        self.buttons.append(keyentry)

        keybutton = tk.Button(keyframe,text="P",command=lambda: self.get_saved_entries("item_keyword", target=keyentry), height=1, width=2)
        keybutton.pack(side="right")
        self.buttons.append(keybutton)

        keyclear = tk.Button(keyframe,text="C", command=lambda: keyentry.delete(0, tk.END))
        keyclear.pack(side="right")
        self.buttons.append(keyclear)



        ###

        descframe = tk.Frame(self)
        descframe.pack(anchor="center",pady=5)
        self.buttons.append(descframe)

        desclabel = tk.Label(descframe,text="Item Description")
        desclabel.pack(side="top")
        self.buttons.append(desclabel)

        desctext = tk.Text(descframe, width=50,height=5)
        desctext.pack()
        self.buttons.append(desctext)
        
        back_main = tk.Button(self, text="Back", font=10, command=self.item_menu,width=20,bg="red")
        back_main.pack(side="bottom")
        self.buttons.append(back_main)

        save_item = tk.Button(self, text = "Save item", font=10, command=lambda: (
            print(keyentry.get()),  # Print the keys value
            self.save_new_item(
                nameentry, 
                typeentry, 
                rarityentry, 
                keyentry, 
                desctext
            ),
            self.item_menu()
        ))


        save_item.pack(side="bottom")
        self.buttons.append(save_item)


    def get_saved_entries(self, origin, target):
        temp = []
        extracted = []
        used_file = None
        title = ""
        match origin:
            case "item_type":
                used_file = types_items_file
                title = "Type Selection"
            case "item_rarity":
                used_file = rarity_items_file
                title = "Rarity Selection"
            case "item_keyword":
                used_file = keywords_items_file
                title = "Keyword Selection"

        canvas = tk.Canvas(root, width=400, height=400, bg="gray")
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
        X = 0
        Y = 0
        for x in extracted:
            if origin != "item_keyword":
                button = tk.Button(buttonframe, text=x, width=10,height=2, command=lambda insertable=x: (target.delete(0, tk.END), target.insert(0, insertable)))
            else:
                button = tk.Button(buttonframe, text=x, width=10, height=2, command=lambda l=len(target.get()), insertable=(x+", "): target.insert(l, insertable))
            button.grid(row=Y, column=X)
            if X == 3:
                X = 0
                Y += 1
            else:
                X += 1
            temp.append(button)

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

        closebutton = tk.Button(entrycanvas, text="Close", command=lambda: (all(item.destroy() for item in temppu)))
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

        savebuttons = tk.Button(entrycanvas, text="Save", command= lambda: self.save_action(newntry.get(),content, temppu, used_file))
        savebuttons.pack(side="bottom")
        temppu.append(newntry)

    def save_action(self, new, content, temppu, used_file):
        print(new)
        print(temppu)
        print(content)
        content.append(new)  # Append new data to content
        for item in temppu:  # Destroy all items in the temporary list
            item.destroy()
        self.insert_new_list(used_file, content)  # Insert the new list
        self.item_creation()  # Call the item creation method

    def insert_new_list(self, chosenfile, list):
        with open(chosenfile, "w") as file:
            for line in list:
                if line != "" and line != " ":
                    file.write(str(line)+"\n")

    def save_new_item(self, name_entry, type_entry, rarity_entry, keys_entry, desc_entry):
        keys = keys_entry.get() # Tää ilmeisesti ottaa listan, stringin sijaan o.O
        name = name_entry.get()
        rarity = rarity_entry.get()
        type = type_entry.get()
        desc = desc_entry.get("1.0", "end")
        print(keys) # Mut tää sit taas printtaa stringin eikä listaa ? O.o
        name_with_lines = name.replace(" ", "_")
        new_item_path = os.path.join(items_dir, name_with_lines)
        
        stringi = ""
        for i in keys:
            stringi = f"{stringi}, {i}"

        endkeys = []
        keylist = keys.split(", ") # Ja sit tää täällä sanoo et 'list' object has no attribute 'split' ? -_-
        for key in keylist:
            endkeys.append(key)
        print(endkeys)

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

        descpath = os.path.join(new_item_path, "desc")
        with open(descpath, "w", encoding=finn_encoding) as file:
            file.write(desc)
        print("Item successfully saved!")
         

        
        
    
    def settings_menu(self):
        for entity in self.buttons:
            entity.destroy()

        setting_frame = tk.Frame(self, bg=self.settings.back_color)
        setting_frame.pack(anchor="center")
        setting_content = []
        self.buttons.append(setting_frame)
        print("Setting frame created")

        setting_label = tk.Label(setting_frame, text="SETTINGS", font=("Arial Black", 20), bg=self.settings.back_color, fg=self.settings.title_color)
        setting_label.pack(side="top",pady=10)
        self.buttons.append(setting_label)
        print("Setting label created")

        index = 0
        for setting in self.settings.settings_name:
            print(self.settings.settings_name)
            print(setting)
            setting = setting.capitalize()
            set = tk.Frame(setting_frame, bg=self.settings.back_color)
            set.pack(anchor="n",pady=5)
            self.buttons.append(set)


            label = tk.Label(set, text=setting, width=10, bg=self.settings.back_color,fg=self.settings.title_color)
            label.pack(side="left",padx=3)
            self.buttons.append(label)

            entry = tk.Entry(set)
            entry.pack(side="right", padx=3)
            entry.insert(0, self.settings.settings_value[index])
            self.buttons.append(entry)
            setting_content.append(entry)

            index += 1

            
        colorframe = tk.Frame(setting_frame,bg=self.settings.back_color)
        colorframe.pack(side="bottom")
        self.buttons.append(colorframe)

        label = tk.Label(colorframe, bg=self.settings.back_color, fg=self.settings.title_color,text="Color Selection")
        label.pack(side="top")
        self.buttons.append(label)
        
        colors = ["black", "white"]
        for c in colors:
            button = tk.Button(colorframe, bg=c,borderwidth=5,highlightcolor="yellow",highlightthickness=5, command= lambda c=c: (self.update_color(c), self.settings.savecolor(c)),width=2,height=1)
            button.pack(side="left",padx=5)
            self.buttons.append(button)

            
        
        save_button = tk.Button(setting_frame, text="SAVE", command=lambda: self.setting_change(setting_content))
        save_button.pack(side="bottom",pady=5)

        print(setting_content)
        
        back_main = tk.Button(self, text="Back", font=10, command=self.GUI_init, width=20,bg="red")
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
            elif X == 2:
                self.bg(Y)
            X += 1
        self.settings.save(savelist)


            



root = MainWindow()



tk.mainloop()



