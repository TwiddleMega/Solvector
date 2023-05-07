import customtkinter as ctk
import sqlite3
import time

#GUI Commands and Processes
def resourceadd():
    connection = sqlite3.connect("notes.db")
    crsr = connection.cursor()

    year,area,topic,name,link,noteid = yearselect.get(),areaselect.get(),topicselect.get(),nameentry.get(),linkentry.get(),identry.get()

    if name=='' or link=='':
        instructions.configure(text="You must fill all fields in order to save a resource.")
        time.sleep(2)
        instructions.configure(text='''Select the appropriate attributes for your resource, and enter a link and name.
Once you're done, press "Add Resource" to add the resource to your library.
If you would like to connect your resource to one of the inbuilt notes, enter an ID.''')
    else:
        if noteid=='':
            noteid='None'
        crsr.execute("INSERT INTO resources VALUES(?,?,?,?,?,?)",(noteid, link, year, area, topic, name))

    connection.commit()
    connection.close()

#window settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Solvector - Equation Solver")

#Widget initialisation
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

title = ctk.CTkLabel(master=frame, text="Solvector", font=("BankGothic Lt BT", 30))
title.pack(pady=10)

instructions = ctk.CTkLabel(master=frame, text='''Select the appropriate attributes for your resource, and enter a link and name.
Once you're done, press "Add Resource" to add the resource to your library.
If you would like to connect your resource to one of the inbuilt notes, enter an optional ID.''')
instructions.pack(pady=10)

yearselect = ctk.CTkOptionMenu(master=frame, values=["YEAR 1", "YEAR 2", "ALL"], hover=True)
yearselect.pack(pady=10, padx=10)

areaselect = ctk.CTkOptionMenu(master=frame, values=["PURE","STATISTICS","MECHANICS","ALL"])
areaselect.pack(pady=10, padx=10)

topicselect = ctk.CTkOptionMenu(master=frame, values=["PROOF", "ALGEBRA AND FUNCTIONS", "COORDINATE GEOMETRY", "SEQUENCES AND SERIES", "TRIGONOMETRY", "EXPONENTIALS AND LOGARITHMS", "DIFFERENTIATION", "INTEGRATION", "NUMERICAL METHODS", "VECTORS", "SAMPLING", "DATA PRESENTATION AND INTERPRETATION", "PROBABILITY", "STATISTICAL DISTRIBUTIONS", "HYPOTHESIS TESTING", "QUANTITIES AND UNITS IN MECHANICS", "KINEMATICS", "FORCES AND NEWTON'S LAWS", "MOMENTS"])
topicselect.pack(pady=10, padx=10)

nameentry = ctk.CTkEntry(master=frame, placeholder_text="Enter name", width=150)
nameentry.pack(pady=10, padx=10)

linkentry = ctk.CTkEntry(master=frame, placeholder_text="Enter link", width=150)
linkentry.pack(pady=10, padx=10)

identry = ctk.CTkEntry(master=frame, placeholder_text="Enter ID (optional)", width=150)
identry.pack(pady=10, padx=10)

submitbtn = ctk.CTkButton(master=frame, command=resourceadd, text = "Add Resource")
submitbtn.pack(pady=10, padx=10)

app.mainloop()
