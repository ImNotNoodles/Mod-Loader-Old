from NoodleLoaderExtensions import *

app = Tk()
app.geometry("478x443")
app.configure(background='#2e2e2e')
app.title('Noodles Mod Assistant')
app.resizable(False, False)
app.overrideredirect(0)
app.eval('tk::PlaceWindow . center')
try:
    app.iconbitmap("./Images/appico.ico")
except:
    pass

try:
    logo = PhotoImage(file = "./Images/logo.png")
    border = PhotoImage(file = "./Images/border.png")
    discordLogo = PhotoImage(file = "./Images/Discord.png")
except:
    pass


###########################
# Function Area 
GameLocationDir = ""
ModLocate = ""
def getGameLocation():
    global GameLocationDir
    
    GameLocationDir = filedialog.askdirectory()
    if GameLocationDir is not None:
        for letter in GameLocationDir.splitlines():
            ShorterGameDir = (letter[:30]+"...")
        ModdingGameFileEntryText.config(text=f"{ShorterGameDir}")    
def ModLocation():
    global ModLocate
    ModLocate = filedialog.askopenfilename()
    if ModLocate is not None:
        for letter in ModLocate.splitlines():
            ShorterModLocate = (letter[:30]+"...")
        ModdingFileEntryText.config(text=f"{ShorterModLocate}") 

    
    
        
def Install():
    if GameLocationDir:
        print(GameLocationDir)
        if ModLocate:

            def InitiateInstall():
                try:
                    print(f"{ModLocate} Moved To{GameLocationDir}")
                    shutil.move(ModLocate, GameLocationDir)
                except:
                    InstallMod.config(state=DISABLED, text="File/Dir Not Found!")
                    app.update_idletasks()
                    time.sleep(1)
                    InstallMod.config(state=DISABLED, text="File/Dir Not Found!")
                    app.update_idletasks()
                    time.sleep(1)
                    InstallMod.config(state=DISABLED, text="File/Dir Not Found!")
                    app.update_idletasks()
                    time.sleep(1)
                    InstallMod.config(state=DISABLED, text="Installing...")
                    time.sleep(1)
                    InstallMod.config(state=NORMAL, text="Install")
                    app.update_idletasks()
                    Settings.config(state=NORMAL, fg="#bdbdbd")
                    app.update_idletasks()
                    Automatic.config(state=NORMAL, fg="#bdbdbd")
                    app.update_idletasks()
                InstallMod.config(state=DISABLED, text="Installing...")
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=DISABLED, text="Installing..")
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=DISABLED, text="Installing.")
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=DISABLED, text="Installing...")
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=DISABLED, text="Installing..")
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=DISABLED, text="Installing.")
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=DISABLED, text="Done!")
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=DISABLED, text="Done!")
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=NORMAL, text="Install")
                app.update_idletasks()
                Settings.config(state=NORMAL, fg="#bdbdbd")
                app.update_idletasks()
                Automatic.config(state=NORMAL, fg="#bdbdbd")
                app.update_idletasks()
            Modding.config(state=DISABLED, disabledforeground="#ff0000")
            Settings.config(state=DISABLED, disabledforeground="#363636")
            Automatic.config(state=DISABLED, disabledforeground="#363636")
            InitiateInstall()
        else:
            def InitiateNothing():
                InstallMod.config(state=DISABLED, text="Please Select Your Files!")
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=DISABLED, text="Please Select Your Files!")
                app.update_idletasks()
                time.sleep(1)
                app.update_idletasks()
                time.sleep(1)
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=NORMAL, text="Install")
                Settings.config(state=NORMAL, fg="#bdbdbd")
                Automatic.config(state=NORMAL, fg="#bdbdbd")
            Modding.config(state=DISABLED, disabledforeground="#ff0000")
            Settings.config(state=DISABLED, disabledforeground="#363636")
            Automatic.config(state=DISABLED, disabledforeground="#363636")
            InitiateNothing()
    else:
            def InitiateNothing():
                InstallMod.config(state=DISABLED, text="Please Select Your Files!")
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=DISABLED, text="Please Select Your Files!")
                app.update_idletasks()
                time.sleep(1)
                app.update_idletasks()
                time.sleep(1)
                app.update_idletasks()
                time.sleep(1)
                InstallMod.config(state=NORMAL, text="Install")
                Settings.config(state=NORMAL, fg="#bdbdbd")
                Automatic.config(state=NORMAL, fg="#bdbdbd")
            Modding.config(state=DISABLED, disabledforeground="#ff0000")
            Settings.config(state=DISABLED, disabledforeground="#363636")
            Automatic.config(state=DISABLED, disabledforeground="#363636")
            InitiateNothing()    
###########################


###########################
# Modding Tab Area

def ModdingMenu():
    global ModdingGameFileLabel, ModdingGameFileButton, ModdingGameFileEntry, ModdingGameFileEntryText, ModdingFileLabel, ModdingFileButton, ModdingFileEntry, ModdingFileEntryText, InstallMod
    try:
        AutoTemp.destroy()
    except:
        pass
    try:
        
        SettingsTemp.destroy()
        #####
    except:
        pass
    Modding.config(state=DISABLED, disabledforeground="#ff0000")
    Settings.config(state=NORMAL, fg="#bdbdbd")
    Automatic.config(state=NORMAL, fg="#bdbdbd")

    #Game File
    ModdingGameFileLabel = Label(app, text="Game Location:", font=('@Kozuka Gothic Pr6N L',10, 'bold'), bg='#2e2e2e', fg='#bdbdbd', borderwidth=0)
    ModdingGameFileLabel.place(anchor = CENTER, relx = .16, rely = .6)

    ModdingGameFileButton = Button(app, text="Locate", font=('@Kozuka Gothic Pr6N L',10, 'bold'), bg='#2e2e2e', fg='#bdbdbd', command=getGameLocation)
    ModdingGameFileButton.place(anchor = CENTER, relx = .32, rely = .6)

    ModdingGameFileEntry = Entry(app, text="Test",disabledbackground='#2e2e2e', disabledforeground="#bdbdbd", width=40, state=DISABLED)
    #ModdingGameFileEntry.insert(0,"Pick Your Game Modding Location")
    ModdingGameFileEntry.place(anchor = CENTER, relx = .66, rely = .6)

    ModdingGameFileEntryText = Label(app, text="Select Game File Modding Location",bg='#2e2e2e', fg="#bdbdbd", borderwidth=0)
    ModdingGameFileEntryText.place(anchor = CENTER, relx = .66, rely = .6)

    #Mod File
    ModdingFileLabel = Label(app, text="Mod Location:", font=('@Kozuka Gothic Pr6N L',10, 'bold'), bg='#2e2e2e', fg='#bdbdbd', borderwidth=0)
    ModdingFileLabel.place(anchor = CENTER, relx = .16, rely = .75)

    ModdingFileButton = Button(app, text="Locate", font=('@Kozuka Gothic Pr6N L',10, 'bold'), bg='#2e2e2e', fg='#bdbdbd', command=ModLocation)
    ModdingFileButton.place(anchor = CENTER, relx = .32, rely = .75)

    ModdingFileEntry = Entry(app, text="Test",disabledbackground='#2e2e2e', disabledforeground="#bdbdbd", width=40, state=DISABLED)
    #ModdingGameFileEntry.insert(0,"Pick Your Game Modding Location")
    ModdingFileEntry.place(anchor = CENTER, relx = .66, rely = .75)

    ModdingFileEntryText = Label(app, text="Select Mod File Location",bg='#2e2e2e', fg="#bdbdbd", borderwidth=0)
    ModdingFileEntryText.place(anchor = CENTER, relx = .66, rely = .75)

    InstallMod = Button(app, text="Install", width=50, height=2, font=('@Kozuka Gothic Pr6N L',10, 'bold'), command=Install)
    InstallMod.place(anchor = CENTER, relx = .5, rely = .85)
###########################


###########################
# Settings Tab Area
def SettingsButton():
    global SettingsTemp
    Settings.config(state=DISABLED, disabledforeground="#ff0000")
    Modding.config(state=NORMAL, fg="#bdbdbd")
    Automatic.config(state=NORMAL, fg="#bdbdbd")
    try:
        #####
        ModdingGameFileLabel.destroy()
        ModdingGameFileButton.destroy()
        ModdingGameFileEntry.destroy()
        ModdingGameFileEntryText.destroy()
        ModdingFileLabel.destroy()
        ModdingFileButton.destroy()
        ModdingFileEntry.destroy()
        ModdingFileEntryText.destroy()
        InstallMod.destroy()
        #####
        AutoTemp.destroy()
        #####
    except:
        pass
    SettingsTemp = Label(app, text="Settings Coming Soon!", font=('@Kozuka Gothic Pr6N L',15, 'bold'), bg='#2e2e2e', fg='#bdbdbd', borderwidth=0)
    SettingsTemp.place(anchor = CENTER, relx = .5, rely = .6)
###########################

###########################
# Settings Tab Area
def AutoModButton():
    global AutoTemp
    Automatic.config(state=DISABLED, disabledforeground="#ff0000")
    Modding.config(state=NORMAL, fg="#bdbdbd")
    Settings.config(state=NORMAL, fg="#bdbdbd")
    try:
        #####
        ModdingGameFileLabel.destroy()
        ModdingGameFileButton.destroy()
        ModdingGameFileEntry.destroy()
        ModdingGameFileEntryText.destroy()
        ModdingFileLabel.destroy()
        ModdingFileButton.destroy()
        ModdingFileEntry.destroy()
        ModdingFileEntryText.destroy()
        InstallMod.destroy()
        #####
        SettingsTemp.destroy()
        #####
    except:
        pass
    AutoTemp = Label(app, text="Automatic Mod Loader\nComing Soon!", font=('@Kozuka Gothic Pr6N L',15, 'bold'), bg='#2e2e2e', fg='#bdbdbd', borderwidth=0)
    AutoTemp.place(anchor = CENTER, relx = .5, rely = .6)
###########################


AppLogo = Label(app, text="Image Couldn't Load", borderwidth=0, bg="#2e2e2e" ,image=logo)
AppLogo.place(anchor = CENTER, relx = .5, rely = .2)

AppBorder = Label(app, text="Image Couldn't Load", borderwidth=0, bg="#2e2e2e" ,image=border)
AppBorder.place(anchor = CENTER, relx = .5, rely = .72)

AppVersion = Label(app, text="Installer v0.0.1", bg="#2e2e2e", fg="#bdbdbd")
AppVersion.place(anchor = CENTER, relx = .09, rely = .03)

Modding = Button(app, text="Manual", font=('@Kozuka Gothic Pr6N L',17, 'bold'), bg='#2e2e2e', fg='#bdbdbd', borderwidth=0, activebackground='#2e2e2e',command=ModdingMenu)
Modding.place(anchor = CENTER, relx = .5, rely = .45)

Settings = Button(app, text="Settings", font=('@Kozuka Gothic Pr6N L',17, 'bold'), bg='#2e2e2e', fg='#bdbdbd', borderwidth=0, activebackground='#2e2e2e',command=SettingsButton)
Settings.place(anchor = CENTER, relx = .85, rely = .45)

Automatic = Button(app, text="AutoLoader", font=('@Kozuka Gothic Pr6N L',17, 'bold'), bg='#2e2e2e', fg='#bdbdbd', borderwidth=0, activebackground='#2e2e2e', command=AutoModButton)
Automatic.place(anchor = CENTER, relx = .18, rely = .45)
ModdingMenu()
def DscLink():
    webbrowser.open('https://discord.gg/YQjejw8zrJ')
DiscordLogo = Button(app, text="Image Couldn't Load", borderwidth=0, bg="#2e2e2e" ,image=discordLogo, activebackground='#2e2e2e', command=DscLink)
DiscordLogo.place(anchor = CENTER, relx = .94, rely = .04)


    



app.mainloop()

