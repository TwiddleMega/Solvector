import customtkinter as ctk
import threading
import subprocess

#GUI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Define subroutines to create new thread and run each function
def calculator():
    def run_program():
        subprocess.run(["python", "calculator.py"])#Function to run python file as subprocess

    t = threading.Thread(target=run_program)#Run function in new thread for simultaneous instances
    t.start()#Start new thread

def grapher():
    def run_program():
        subprocess.run(["python", "graphing.py"])

    t = threading.Thread(target=run_program)
    t.start()

def solver():
    def run_program():
        subprocess.run(["python", "solver.py"])

    t = threading.Thread(target=run_program)
    t.start()

def notes():
    def run_program():
        subprocess.run(["python", "notes.py"])

    t = threading.Thread(target=run_program)
    t.start()

#GUI initialisation
root = ctk.CTk()
root.geometry("250x250")
root.title("Solvector")

#Add GUI widgets and assign function
label = ctk.CTkLabel(root, text="Solvector", font=("BankGothic Lt BT", 30))#Title 
label.pack(pady=10)

button1 = ctk.CTkButton(root, text="Scientific Calculator", command=calculator)#Calculator Button
button1.pack(pady=5)

button2 = ctk.CTkButton(root, text="Graphing Calculator", command=grapher)#Graphing Button
button2.pack(pady=5)

button3 = ctk.CTkButton(root, text="Equation Solver", command=solver)#Solver Button
button3.pack(pady=5)

button4 = ctk.CTkButton(root, text="Notes Database", command=notes)#Notes Button
button4.pack(pady=5)

root.mainloop()
