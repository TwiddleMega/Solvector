import customtkinter as ctk
import math

#Define calculator class
class Calculator:
    #Initialise class attributes
    def __init__(self, master):
        #GUI Setup
        self.master = master
        master.title("Scientific Calculator")

        self.display = ctk.CTkEntry(master, width=300, justify="right")
        self.display.grid(row=0, column=0, columnspan=6, pady=5)
        
        #List that contains button layout
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-', 
            '1', '2', '3', '/', 
            '0', '.', '^', '*', 
            'sin','cos','tan','deg to rad',
	    'arcsin','arccos','arctan','rad to deg',
            'log', 'ln', '(', ')', 
            'pi', 'e', 'sqrt', '-/+', 
            'AC','Ans', '='
        ]

        #Create and add buttons to grid; looping for efficiency
        r = 1
        c = 0
        for button in buttons:
            #Assign default values for colour and hover colour.
            clr = ("#3B8ED0", "#1F6AA5")
            hvrclr = ("#36719F", "#144870")

            #Initialise parameters based on button
            if button == '=':
                cmd = self.calculate #Command when button is clicked
                clr = '#e09e04' #Colour for this type of button
                hvrclr = '#b87802' #Hover colour for this type of button
            elif button in ('(', ')', 'pi', 'e'):
                cmd = lambda x=button: self.append(x)
            elif button == 'Ans':
                cmd = lambda x=button: self.append(x)
                clr = '#e09e04'
                hvrclr = '#b87802'
            elif button in ('sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan'):
                clr = '#025ca1'
                cmd = lambda x=button: self.append(x+'(')
            elif button in ('deg to rad', 'rad to deg'):
                clr = '#025ca1'
                cmd = lambda x=button: self.append(x)
            elif button in ('ln', 'log','sqrt'):
                cmd = lambda x=button: self.append(x+'(')
            elif button == 'AC':
                cmd = lambda x=0: self.status('clear')
                clr = '#e09e04'
            elif button == '-/+':
                cmd = lambda x=0: self.status('sign')

            #Parameters for all other buttons
            else:
                cmd = lambda x=button: self.append(x)
                clr = '#2687d1'            

            #Assign according to parameters for each widget    
            ctk.CTkButton(master, text=button, width=80, height=2, command=cmd, fg_color = clr, hover_color = hvrclr).grid(row=r, column=c)
            c += 1
            if c > 3: #go to new row after 4 columns.
                c = 0
                r += 1

        #Initialise answer value
        self.last_answer = ''

    #Define append function for adding to Entry Widget
    def append(self, value):
        #Identify append based on button
        if value == 'Ans':
            self.display.insert(ctk.END, self.last_answer)#Enter last answer
        elif value == 'ln':
            self.display.insert(ctk.END, 'ln(')
        elif value == 'deg to rad':
            self.display.insert(ctk.END, '*(pi/180)')
        elif value == 'rad to deg':
            self.display.insert(ctk.END, '*(180/pi)')
        else:
            self.display.insert(ctk.END, value)

    #Evaluate and calculate expression
    def calculate(self):
        try:
            expression = self.display.get()#Get expression from Entry

            #Code to replace displayed expression with python math functions
            if '^' in expression:
                expression = expression.replace('^', '**')
            if 'log' in expression:
                expression = expression.replace('log', 'math.log10')
            if 'sqrt' in expression:
                expression = expression.replace('sqrt', 'math.sqrt')
            if 'pi' in expression:
                expression = expression.replace('pi', 'math.pi')
            if 'ln' in expression:
                expression = expression.replace('ln', 'math.log')
            if 'arcsin' in expression:
                expression = expression.replace('arcsin', 'asmathin')
            if 'arccos' in expression:
                expression = expression.replace('arccos', 'acmathos')
            if 'arctan' in expression:
                expression = expression.replace('arctan', 'atmathan')
            if 'sin' in expression:
                expression = expression.replace('sin', 'math.sin')
            if 'cos' in expression:
                expression = expression.replace('cos', 'math.cos')
            if 'tan' in expression:
                expression = expression.replace('tan', 'math.tan')
            if 'e' in expression:
                expression = expression.replace('e', 'math.e')
            if 'asmathin' in expression:
                expression = expression.replace('asmathin', 'math.asin')
            if 'acmathos' in expression:
                expression = expression.replace('acmathos', 'math.acos')
            if 'atmathan' in expression:
                expression = expression.replace('atmathan', 'math.atan')

            #Updates status with the expression.
            self.status('result'+str(expression))
        except:
            pass                

    #Function to update the calculator display status
    def status(self, value):
        if value == 'clear':
            self.display.delete(0, ctk.END)#Clear the Entry
        elif value == 'error':
            self.status('clear')
            self.display.insert(0, "Error")#Clear entry and insert Error
        elif value[:6] == 'result':
            try:
                #Evaluate expression and set answer value
                expression = value[6:]
                result = str(eval(expression))
                self.last_answer = result
                self.status('clear')
                self.display.insert(0, result)#Display result of calculation
            except Exception as e:
                self.status('error')#Error case
        elif value == 'sign':
            #Change sign of value in Entry
            expression = self.display.get()
            expression = f'-({expression})'
            self.status('clear')
            self.display.insert(0, expression)

#GUI appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#GUI run
root = ctk.CTk()
calculator = Calculator(root)
root.mainloop()

