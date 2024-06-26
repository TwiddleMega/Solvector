import customtkinter as ctk
import threading
import subprocess

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def calculator():
    def run_program():
        subprocess.run(["python", "calculator.py"])

    t = threading.Thread(target=run_program)
    t.start()

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

root = ctk.CTk()
root.geometry("250x250")
root.title("Solvector")

label = ctk.CTkLabel(root, text="Solvector", font=("BankGothic Lt BT", 30))
label.pack(pady=10)

button1 = ctk.CTkButton(root, text="Scientific Calculator", command=calculator)
button1.pack(pady=5)

button2 = ctk.CTkButton(root, text="Graphing Calculator", command=grapher)
button2.pack(pady=5)

button3 = ctk.CTkButton(root, text="Equation Solver", command=solver)
button3.pack(pady=5)

button4 = ctk.CTkButton(root, text="Notes Database", command=notes)
button4.pack(pady=5)

root.mainloop()
