import tkinter as tk
from tkinter import messagebox
import math

class SuperCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Calculator")
        self.root.geometry("400x600")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=60)

        btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        btns_frame.pack()

        buttons = [
            '7', '8', '9', 'C',
            '4', '5', '6', '/',
            '1', '2', '3', '*',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', '-',
            'sqrt', '^', 'log', 'ln',
            '!',  # Factorial button
        ]

        row = 0
        col = 0
        for button in buttons:
            action = lambda x=button: self.button_click(x)
            tk.Button(btns_frame, text=button, width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=action).grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, item):
        if item == 'C':
            self.expression = ""
            self.input_text.set("")
        elif item == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
                self.expression = ""
                self.input_text.set("")
        elif item in ('sin', 'cos', 'tan', 'sqrt', 'log', 'ln', '!'):
            try:
                if item == 'sin':
                    self.expression = str(math.sin(math.radians(float(self.expression))))
                elif item == 'cos':
                    self.expression = str(math.cos(math.radians(float(self.expression))))
                elif item == 'tan':
                    self.expression = str(math.tan(math.radians(float(self.expression))))
                elif item == 'sqrt':
                    self.expression = str(math.sqrt(float(self.expression)))
                elif item == 'log':
                    self.expression = str(math.log10(float(self.expression)))
                elif item == 'ln':
                    self.expression = str(math.log(float(self.expression)))
                elif item == '!':
                    self.expression = str(math.factorial(int(float(self.expression))))
                self.input_text.set(self.expression)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
                self.expression = ""
                self.input_text.set("")
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SuperCalculator(root)
    root.mainloop()
