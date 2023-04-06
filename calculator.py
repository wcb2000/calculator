import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=20, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=4, pady=6)

        # Define buttons for each number and operation
        self.buttons = [    'sin', 'cos', 'tan', 'log',    '√', '^', 'π', 'e',    '7', '8', '9', '/',    '4', '5', '6', '*',    '1', '2', '3', '+',    '0', '.', '=', '-']

        # Create and place each button on the calculator
        row = 1
        col = 0
        for button in self.buttons:
            if button == '=':
                command = self.calculate
            elif button == '√':
                command = lambda: self.sqrt()
            elif button == '^':
                command = lambda: self.power()
            elif button == 'π':
                command = lambda: self.pi()
            elif button == 'e':
                command = lambda: self.e()
            elif button == 'sin':
                command = lambda: self.sin()
            elif button == 'cos':
                command = lambda: self.cos()
            elif button == 'tan':
                command = lambda: self.tan()
            elif button == 'log':
                command = lambda: self.log()
            else:
                command = lambda x=button: self.press(x)
            tk.Button(master, text=button, width=5, height=2, font=('Arial', 12), command=command).grid(row=row, column=col, padx=4, pady=6)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Bind keyboard keys to calculator buttons
        master.bind('<Return>', lambda event: self.calculate())
        master.bind('<Escape>', lambda event: self.clear())
        master.bind('<BackSpace>', lambda event: self.backspace())
        master.bind('<Key>', lambda event: self.press(event.char))

    # Update the display with the pressed button
    def press(self, button):
        self.display.insert(tk.END, button)

    # Calculate the result of the expression in the display
    def calculate(self):
        try:
            expression = self.display.get()
            expression = expression.replace('^', '**')
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    # Clear the calculator display
    def clear(self):
        self.display.delete(0, tk.END)

    # Remove the last character from the calculator display
    def backspace(self):
        text = self.display.get()[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, text)

    # Calculate the square root of the number in the display
    def sqrt(self):
        try:
            result = math.sqrt(float(self.display.get()))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    # Calculate the power of the number in the display
    def power(self):
        self.display.insert(tk.END, '^')

    # Insert the value of pi in the display
    def pi(self):
        self.display.insert(tk.END, math.pi)
    # Insert the value of e in the display
    def e(self):
        self.display.insert(tk.END, math.e)

    # Calculate the sine of the number in the display
    def sin(self):
        try:
            result = math.sin(math.radians(float(self.display.get())))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    # Calculate the cosine of the number in the display
    def cos(self):
        try:
            result = math.cos(math.radians(float(self.display.get())))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    # Calculate the tangent of the number in the display
    def tan(self):
        try:
            result = math.tan(math.radians(float(self.display.get())))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    # Calculate the logarithm of the number in the display
    def log(self):
        try:
            result = math.log10(float(self.display.get()))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
    # Create the calculator GUI
if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

    
