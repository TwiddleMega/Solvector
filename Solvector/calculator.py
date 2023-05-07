import customtkinter as ctk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.display = ctk.CTkEntry(master, width=300, justify="right")
        self.display.grid(row=0, column=0, columnspan=6, pady=5)

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

        # create and add buttons to grid
        r = 1
        c = 0
        for button in buttons:
            clr = ("#3B8ED0", "#1F6AA5")
            hvrclr = ("#36719F", "#144870")
            
            if button == '=':
                cmd = self.calculate
                clr = '#e09e04'
                hvrclr = '#b87802'
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

            else:
                cmd = lambda x=button: self.append(x)
                clr = '#2687d1'            
                
            ctk.CTkButton(master, text=button, width=80, height=2, command=cmd, fg_color = clr, hover_color = hvrclr).grid(row=r, column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1

        self.last_answer = ''

    def append(self, value):
        if value == 'Ans':
            self.display.insert(ctk.END, self.last_answer)
        elif value == 'ln':
            self.display.insert(ctk.END, 'ln(')
        elif value == 'deg to rad':
            self.display.insert(ctk.END, '*(pi/180)')
        elif value == 'rad to deg':
            self.display.insert(ctk.END, '*(180/pi)')
        else:
            self.display.insert(ctk.END, value)

    def calculate(self):
        try:
            expression = self.display.get()
            
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
            if 'fact' in expression:
                num = int(expression[4:])
                expression = expression[:3] + f'{math.factorial(num)}'
            if 'asmathin' in expression:
                expression = expression.replace('asmathin', 'math.asin')
            if 'acmathos' in expression:
                expression = expression.replace('acmathos', 'math.acos')
            if 'atmathan' in expression:
                expression = expression.replace('atmathan', 'math.atan')

            self.status('result'+str(expression))
        except:
            pass                
            
    def status(self, value):
        if value == 'clear':
            self.display.delete(0, ctk.END)
        elif value == 'error':
            self.status('clear')
            self.display.insert(0, "Error")
        elif value[:6] == 'result':
            try:
                expression = value[6:]
                result = str(eval(expression))
                self.last_answer = result
                self.status('clear')
                self.display.insert(0, result)
            except Exception as e:
                self.status('error')
        elif value == 'sign':
            expression = self.display.get()
            expression = f'-({expression})'
            self.status('clear')
            self.display.insert(0, expression)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
calculator = Calculator(root)
root.mainloop()

