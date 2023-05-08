import sqlite3
import customtkinter as ctk
import threading
import subprocess
import webview

#SQL Table initialisation
connection = sqlite3.connect("notes.db")
crsr = connection.cursor()

#Create table of pre-loaded notes
createtable = """CREATE TABLE IF NOT EXISTS notes (
id INTEGER PRIMARY KEY,
link VARCHAR(500),
year VARCHAR(6),
area VARCHAR(20),
topic VARCHAR(50),
type VARCHAR(50),
name VARCHAR(100))"""
crsr.execute(createtable)

#Create user-made database of resources
createtable2 = """CREATE TABLE IF NOT EXISTS resources (
id INT PRIMARY KEY,
link VARCHAR(500),
year VARCHAR(6),
area VARCHAR(20),
topic VARCHAR(50),
name VARCHAR(100),
FOREIGN KEY (id) REFERENCES notes(id))"""
crsr.execute(createtable2)

connection.commit()
connection.close()

#=====================GUI SETUP========================

#window settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Solvector - Equation Solver")

#GUI Commands and Processes
def combo(value):
    pass
    
def resourceopen():
    openlink = (combobox.get()).split(',')
    
    with open('temp.txt', 'w') as f:
        f.write(f'{openlink[1].strip()}')

    def run_program():
        subprocess.run(["python", "webviewcode.py"])

    t = threading.Thread(target=run_program)
    t.start()

def resourcedelete():
    resource = combobox.get()
    
    resourceid,link,year,area,topic,name = resource.split(',')
    resourceid,link,year,area,topic,name = resourceid.strip(),link.strip(),year.strip(),area.strip(),topic.strip(),name.strip()

    connection = sqlite3.connect("notes.db")
    crsr = connection.cursor()

    searchresult = crsr.execute(f'''SELECT * FROM resources WHERE year="{year}" AND area="{area}" AND topic="{topic}" AND name="{name}"''')
    deleteresult = f'DELETE FROM resources {searchresult}'
    crsr.execute(deleteresult)
    resourcecheck = []
    print(searchresult)
    for i in searchresult:
        resourcecheck.append(str(i))
    print(resourcecheck)

def resourceadd():
    def run_program():
        subprocess.run(["python", "addnotes.py"])

    t = threading.Thread(target=run_program)
    t.start()

def search():
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
     
        L = [0] * (n1)
        R = [0] * (n2)
     
        for i in range(0, n1):
            L[i] = arr[l + i]
     
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
     
        i = 0
        j = 0
        k = l
     
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
     
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
     
    def mergeSort(arr, l, r):
        narr = arr
        if l < r:
     
            m = l+(r-l)//2
     
            mergeSort(narr, l, m)
            mergeSort(narr, m+1, r)
            merge(narr, l, m, r)
        return narr
    
    year,area,topic,name,link = yearselect.get(),areaselect.get(),topicselect.get(),nameentry.get(),linkentry.get()

    connection = sqlite3.connect("notes.db")
    crsr = connection.cursor()

    if name=='' and link=='':
        searchresult1 = crsr.execute(f'''SELECT * FROM notes WHERE year="{year}" AND area="{area}" AND topic="{topic}"''')
    elif name=='':
        searchresult1 = crsr.execute(f'''SELECT * FROM notes WHERE year="{year}" AND area="{area}" AND topic="{topic}" AND link="{link}"''')
    elif link=='':
        searchresult1 = crsr.execute(f'''SELECT * FROM notes WHERE year="{year}" AND area="{area}" AND topic="{topic}" AND name="{name}"''')
    else:
        searchresult1 = crsr.execute(f'''SELECT * FROM notes WHERE year="{year}" AND area="{area}" AND topic="{topic}" AND name="{name}" AND link="{link}"''')
        
    resultlist = []
    result2list = []
    for i in searchresult1:
        interimlist = []
        for j in i:
            val = str(j)
##            if len(val) > 20:
##                interimlist.append(val[:20]+"...")
##            else:
            interimlist.append(val)
        resultlist.append(str(interimlist).strip('[]'))

    for i in resultlist:
        for j in eval(i):
            try:
                test = int(j)
                searchresult2 = crsr.execute(f'''SELECT * FROM resources WHERE id={test}''')
                for i in searchresult2:
                    result2list.append(str(i).strip('()'))
            except:
                pass
    for i in result2list:
        resultlist.append(i)

    global combobox

    finalsearch = []
    for i in resultlist:
        i = i.replace("'",'')
        print(i)
        finalsearch.append(i)

    #resultlist = mergeSort(resultlist,0,len(resultlist)-1)
    finalsearch = mergeSort(finalsearch,0,len(finalsearch)-1)
    
    combobox = ctk.CTkComboBox(master=frame,values=finalsearch,command=combo, width=500)
    combobox.place(x=170,y=230)
    connection.close()

#window settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("975x600")
app.title("Solvector - Equation Solver")

#Widget initialisation
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

title = ctk.CTkLabel(master=frame, text="Solvector", font=("BankGothic Lt BT", 30))
title.grid(row=0,column=2,pady=10, padx=10)

instructions = ctk.CTkLabel(master=frame, text='''Search Notes/Resources
Enter your criteria
and hit "Search".''')
instructions.grid(row=1,column=2,pady=10, padx=10)

yearselect = ctk.CTkOptionMenu(master=frame, values=["YEAR 1", "YEAR 2", "ALL"], hover=True)
yearselect.grid(row=2,column=0,pady=10, padx=10)

areaselect = ctk.CTkOptionMenu(master=frame, values=["PURE","STATISTICS","MECHANICS","ALL"])
areaselect.grid(row=2,column=1,pady=10, padx=10)

topicselect = ctk.CTkOptionMenu(master=frame, values=["PROOF", "ALGEBRA AND FUNCTIONS", "COORDINATE GEOMETRY", "SEQUENCES AND SERIES", "TRIGONOMETRY", "EXPONENTIALS AND LOGARITHMS", "DIFFERENTIATION", "INTEGRATION", "NUMERICAL METHODS", "VECTORS", "SAMPLING", "DATA PRESENTATION AND INTERPRETATION", "PROBABILITY", "STATISTICAL DISTRIBUTIONS", "HYPOTHESIS TESTING", "QUANTITIES AND UNITS IN MECHANICS", "KINEMATICS", "FORCES AND NEWTON'S LAWS", "MOMENTS", "ALL"])
topicselect.grid(row=2,column=2,pady=10, padx=10)

nameentry = ctk.CTkEntry(master=frame, placeholder_text="Enter name", width=150)
nameentry.grid(row=2,column=3,pady=10, padx=10)

linkentry = ctk.CTkEntry(master=frame, placeholder_text="Enter link", width=150)
linkentry.grid(row=2,column=4,pady=10, padx=10)

searchbtn = ctk.CTkButton(master=frame, command=search, text = "Search")
searchbtn.grid(row=3,column=2,pady=10,padx=10)

blank = ctk.CTkLabel(master=frame, text="", font=("Arial", 30))
blank.grid(row=5,column=2,pady=10, padx=10)

submitbtn = ctk.CTkButton(master=frame, command=resourceopen, text = "Open Resource")
submitbtn.grid(row=6,column=1,pady=10,padx=10)

deletebtn = ctk.CTkButton(master=frame, command=resourcedelete, text = "Delete Resource")
deletebtn.grid(row=6,column=2,pady=10,padx=10)

addbtn = ctk.CTkButton(master=frame, command=resourceadd, text = "Add New Resources")
addbtn.grid(row=6,column=3,pady=10,padx=10)

app.mainloop()


