import customtkinter as ctk
import math
import numpy as np
import sympy as sp
from sympy import *
import mpmath
from sympy import solve,Symbol,symbols,diff,sin,exp 
from sympy.abc import x,y


#window settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Solvector - Equation Solver")


#Adjust information on data entry + identify selected equation type
def equationselect(type):
    global value
    value = type
    if type == 'Linear':       
        instructions.configure(text='''Enter the constants a, b for a linear equation in the form:
f(x) = ax + b
Separate your constants with a comma, with no spaces in between''')
    if type == 'Quadratic':       
        instructions.configure(text='''Enter the constants a, b, c for a quadratic equation in the form:
f(x) = ax² + bx + c
Separate your constants with a comma, with no spaces in between. Make sure a is not 0.''')
    if type == 'Simultaneous - 2 Var':       
        instructions.configure(text='''Enter the constants a, b, c, d, e, f for a simultaneous equation in the form:
ax + by = c
dx + ey = f
Separate your constants with a comma, with no spaces in between''')
    if type == 'Simultaneous - 3 Var':       
        instructions.configure(text='''Enter the constants a, b, c, d, e, f, g, h, i, j, k, l for a quadratic equation in the form:
ax + by + cz = d
ex + fy + gz = h
ix + jy + kz = l
Separate your constants with a comma, and no spaces in between''')
    if type == 'Trigonometric':       
        instructions.configure(text='''Enter your equation using the rules specified below:
+-*/ for regular operations
** for powers, and brackets to indicate order of operations
Mathematical Functions and constants | (a)sin() (a)cos() (a)tan() pi
Enter your unknown as "x", and enter no spaces in the equation''')
    if type == 'Differentiate':       
        instructions.configure(text='''Enter your equation using the rules specified below:
+-*/ for regular operations
** for powers, and brackets to indicate order of operations
Mathematical Functions and constants | sin() cos() tan() csc() sec() cot() log10() log() e pi
(a) prefix on a trigonometric function denotes inverse e.g. asin(x) for arcsin(x)
Enter no spaces in the equation, and be sure to use brackets where necessary''')
    if type == 'Other':       
        instructions.configure(text='''Enter your equation using the rules specified below:
+-*/ for regular operations
** for powers, and brackets to indicate order of operations
Mathematical Functions and constants | (arc)sin() (arc)cos() (arc)tan() log10() log() abs() e() e pi
Enter your unknown as "x", and enter no spaces in the equation''')


#Function called to solve equations
def equationsolve():
    textbox.delete("0.0", "end")
    textbox.insert("0.0", "Error - Please retry.")

    #Linear equations
    def Linear():
        constants = (entry.get()).split(',')
        a,b = int(constants[0]),int(constants[1])

        #Compute solution
        solution = -b/a

        #Pass values to file, evaluate, and output to textbox
        with open('Solutions/linearsolve.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            data = text

            textbox.delete("0.0", "end")    
            textbox.insert("0.0", eval(data))

    #Quadratic solve
    def Quadratic():
        solved = 0
        #function to properly display signs
        def addsign(a):
            if int(a)>0:
                a=" + "+str(a)
            elif int(a)==0:
                a=''
            else:
                a=" - "+str(a)
            return a

        #Calculate GCD to check for factorisation
        def gcdCalc(a,b):
            while b:
                temp = a
                a = b
                b = temp%b
            return abs(a)

        #Get factors and compute values
        constants = (entry.get()).split(',')
        a,b,c = int(constants[0]),int(constants[1]),int(constants[2])
        ac = a*c
        gcdTemp=gcdCalc(a,b)
        gcd=gcdCalc(gcdTemp,c)
        det = b**2-4*a*c

        #Factoring situation one
        if c==0:
            solution = b/a
#            print(f"x({a}x{addsign(b)})")

            with open('Solutions/quadraticeasy.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                data = text

                textbox.delete("0.0", "end")
                textbox.insert("0.0", eval(data))
        else:
            #Compute quadratic formula numerator
            sol1Numerator=-b+((b**2-4*a*c)**(1/2))
            sol2Numerator=-b-((b**2-4*a*c)**(1/2))
            denom=2*a

            numer1 = sol1Numerator
            numer2 = sol2Numerator
        
            try:
                #Compute factors and define factorised values
                print(det, "det")
                print(math.sqrt(det), "sqrt")
                test = int(math.sqrt(det))
                print(test, "test")
                
                sol1Gcd=gcdCalc(sol1Numerator,denom)
                sol2Gcd=gcdCalc(sol2Numerator,denom)
                sol1Numerator=-sol1Numerator/sol1Gcd
                sol1Denominator=denom/sol1Gcd
                sol2Numerator=-sol2Numerator/sol2Gcd
                sol2Denominator=denom/sol2Gcd

                if str(int(gcd*a/abs(a))) == '1':
                    coeff = ''
                else:
                    coeff = str(int(gcd*a/abs(a)))

                if str(int(sol1Denominator)) == '1':
                    coeff2 = ''
                else:
                    coeff2 = str(int(sol1Denominator))

                if str(int(sol2Denominator)) == '1':
                    coeff3 = ''
                else:
                    coeff3 = str(int(sol2Denominator))
              
                factored = (f"{coeff}({coeff2}x{addsign(str(int(sol1Numerator)))})({coeff3}x{addsign(str(int(sol2Numerator)))})")

                solution1 = int(numer1/denom)
                solution2 = int(numer2/denom)
                
                #Open and evaluate file with values.
                with open('Solutions/quadraticfactorise.txt', 'r', encoding='utf-8') as file:
                    text = file.read()
                    data = text

                textbox.delete("0.0", "end")
                textbox.insert("0.0", eval(data))

                solved = 1
            except:
                pass

            #Compute for complex quadratics
            if float(det)<0:
                with open('Solutions/quadraticcomplex.txt', 'r', encoding='utf-8') as file:
                    text = file.read()
                    data = text

                    textbox.delete("0.0", "end")
                    textbox.insert("0.0", eval(data))

                    solved = 1
            #Compute for regular solve with equation.
            elif solved != 1:
                with open('Solutions/quadraticsolve.txt', 'r', encoding='utf-8') as file:
                    text = file.read()
                    data = text

                    textbox.delete("0.0", "end")
                    textbox.insert("0.0", eval(data))

                    solved = 1
                    
    #Simultaneous solve                
    def Simultaneous2Var():
        def addsign(a):
            if int(a)>0:
                a=" + "+str(a)
            elif int(a)==0:
                a=''
            else:
                a=" - "+str(a)
            return a

        #Get constants
        constants = (entry.get()).split(',')
        a,b,c,d,e,f = int(constants[0]),int(constants[1]),int(constants[2]),int(constants[3]),int(constants[4]),int(constants[5])


        #Check equation consistency and output result through file accordingly
        mat = np.array([[a,b],
                        [d,e]])
        det = np.linalg.det(mat)
        if det:
            arrayone = np.array([[a, b], [d, e]])
            arraytwo = np.array([c, f])
            solution = np.linalg.solve(arrayone, arraytwo)

            print(solution)
            solx,soly = solution[0],solution[1]

            with open('Solutions/simultaneous2varsolve.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                data = text

                textbox.delete("0.0", "end")    
                textbox.insert("0.0", eval(data))
        else:
            with open('Solutions/simultaneous2varnosolution.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                data = text

                textbox.delete("0.0", "end")    
                textbox.insert("0.0", eval(data))

    #3var simultaneous
    def Simultaneous3Var():
        def addsign(a):
            if int(a)>0:
                a=" + "+str(a)
            elif int(a)==0:
                a=''
            else:
                a=" - "+str(a)
            return a


        #Compute consistency and output values from file accordingly
        constants = (entry.get()).split(',')
        a,b,c,d,e,f,g,h,i,j,k,l = int(constants[0]),int(constants[1]),int(constants[2]),int(constants[3]),int(constants[4]),int(constants[5]),int(constants[6]),int(constants[7]),int(constants[8]),int(constants[9]),int(constants[10]),int(constants[11])

        mat = np.array([[a,b,c],[e,f,g],[i,j,k]])
        det = np.linalg.det(mat)
        if det:
            arrayone = np.array([[a,b,c],[e,f,g],[i,j,k]])
            arraytwo = np.array([d,h,l])
            solution = np.linalg.solve(arrayone, arraytwo)

            solx,soly,solz = solution[0],solution[1],solution[2]

            with open('Solutions/simultaneous3varsolve.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                data = text

                textbox.delete("0.0", "end")    
                textbox.insert("0.0", eval(data))
        else:
            with open('Solutions/simultaneous3varnosolution.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                data = text

                textbox.delete("0.0", "end")    
                textbox.insert("0.0", eval(data))   

    #Trigonometric solve
    def Trigonometric():
        #Solve through sympy
        equation = entry.get()
        print(equation)
        x = symbols('x')
        solution = solve(eval(equation),x,3.14)
        answers = []
        for i in solution:
            answers.append(str(i[0]))

        #Solve through eval of file
        with open('Solutions/trigonometricsolve.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                data = text

                textbox.delete("0.0", "end")
                textbox.insert("0.0", eval(data))

    #Solve Differentiation
    def Differentiate():
        equation = entry.get()

        try:
            answer = diff(equation,x)

            with open('Solutions/differentiatesolve.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                data = text

                textbox.delete("0.0", "end")
                textbox.insert("0.0", eval(data))
        #No solution
        except:
            with open('Solutions/differentiatenosolution.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                data = text

                textbox.delete("0.0", "end")
                textbox.insert("0.0", eval(data))

    #Solve other equation through sympy
    def Other():
        equation = entry.get()
        x = Symbol('x')

        try:
            answer = solve(equation,x)

            with open('Solutions/othersolve.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                data = text

                textbox.delete("0.0", "end")
                textbox.insert("0.0", eval(data))
        #No solution
        except:
            with open('Solutions/othernosolution.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                data = text

                textbox.delete("0.0", "end")
                textbox.insert("0.0", eval(data))

    #Compute based on selected value
    if value == "Linear":
        Linear()
    elif value == "Quadratic":
        Quadratic()
    elif value == "Simultaneous - 2 Var":
        Simultaneous2Var()
    elif value == "Simultaneous - 3 Var":
        Simultaneous3Var()
    elif value == "Trigonometric":
        Trigonometric()
    elif value == "Differentiate":
        Differentiate()
    elif value == "Other":
        Other()
    else:
        entry.configure(placeholder_text="Error - Please retry.")

#Initialise all widgets

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

title = ctk.CTkLabel(master=frame, text="Solvector", font=("BankGothic Lt BT", 30))
title.pack(pady=10)

equationtype = ctk.CTkSegmentedButton(master=frame, values=["Linear", "Quadratic","Simultaneous - 2 Var", "Simultaneous - 3 Var", "Trigonometric", "Differentiate","Other"], command=equationselect)
equationtype.pack(pady=10, padx=10)

instructions = ctk.CTkLabel(master=frame, text="Awaiting Equation Selection")
instructions.pack(pady=10)

entry = ctk.CTkEntry(master=frame, placeholder_text="Enter requested values", width=150)
entry.pack(pady=10, padx=10)

submitbtn = ctk.CTkButton(master=frame, command=equationsolve, text = "Solve")
submitbtn.pack(pady=10, padx=10)

textbox = ctk.CTkTextbox(master=frame, width=400)
textbox.pack(pady=10, padx=10)
#textbox.configure(state="disabled")

app.mainloop()
