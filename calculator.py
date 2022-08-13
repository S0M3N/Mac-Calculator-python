from tkinter import *
from turtle import width

#font
small_font = ("arial", 16)
large_font = ("arial", 40)
digit_font = ("ariel", 24)
default_font = ("ariel", 20)

#color
light_grey = "#F5F5F5"
lb_color = "#D4D4D2"
off_white = "#505050"
operator_color = "#FF9500"
sp_black = "#1C1C1C"

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("300x600")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,1), ".":(4,2)
        }


        self.operations = {"/":"\u00F7", "*":"\u0078", "-":"-", "+":"+"}
        self.button_frame = self.create_button_frame()
        
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_opperator_buttons()

        self.create_special_buttons()

        self.bind_keys()
    
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event,digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
    
    def create_display_labels(self):
        total_label = Label(self.display_frame, text=self.total_expression, anchor=E, bg=off_white, fg = light_grey, padx=24, font=small_font)
        total_label.pack(expand=True, fill="both")
        label = Label(self.display_frame, text=self.current_expression, anchor=E, bg=off_white, fg = light_grey, padx=24, font=large_font)
        label.pack(expand=True, fill="both")
        return total_label, label

    def create_display_frame(self):
        frame = Frame(self.window, height=221, bg=off_white)
        frame.pack(expand=True, fill="both")
        return frame
    
    def add_to_expression(self,value):
        self.current_expression+=str(value)
        self.update_label()
    
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = Button(self.button_frame, text=str(digit), bg=off_white, fg=lb_color, font=digit_font, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1], sticky=NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_opperator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = Button(self.button_frame, text=symbol, bg = operator_color, fg=lb_color, font=default_font, borderwidth=0, command= lambda x=operator: self.append_operator(x))
            button.grid(row = i, column=4, sticky=NSEW)
            i+=1

    def clear(self):
        self.current_expression=""
        self.total_expression = ""
        self.update_total_label()
        self.update_label()

    def create_clear_button(self):
        button = Button(self.button_frame, text="C", bg = sp_black, fg=lb_color, font=default_font, borderwidth=0, command=self.clear)
        button.grid(row = 0, column=1, sticky=NSEW)
    
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = Button(self.button_frame, text="x\u00B2", bg = sp_black, fg=lb_color, font=default_font, borderwidth=0, command=self.square)
        button.grid(row = 0, column=2, sticky=NSEW)
    
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()
        
    def create_sqrt_button(self):
        button = Button(self.button_frame, text="\u221Ax", bg = sp_black, fg=lb_color, font=default_font, borderwidth=0, command=self.sqrt)
        button.grid(row = 0, column=3, sticky=NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = Button(self.button_frame, text="=", bg = operator_color, fg=lb_color, font=default_font, borderwidth=0, command=self.evaluate)
        button.grid(row = 4, column=3, columnspan=2, sticky=NSEW)

    def create_button_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)
    
    def update_label(self):
        self.label.config(text=self.current_expression[:5])
    
    def build(self):
        self.window.mainloop()
    

if __name__ == "__main__":
    calc = Calculator()
    calc.build()
