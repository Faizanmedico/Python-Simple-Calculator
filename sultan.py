from tkinter import *
from math import factorial

# --- Colorful Theme ---
BACKGROUND_COLOR = 'red'  
BUTTON_COLOR = '#34495e'     
BUTTON_TEXT_COLOR = 'red'
DISPLAY_COLOR = 'gray'     
DISPLAY_TEXT_COLOR = 'white'
ACCENT_COLOR = 'lightblue'      
OPERATION_COLOR = 'pink'   

root = Tk()
root.title('✨ Colorful Calculator ✨')
root.config(bg=BACKGROUND_COLOR)

# It keeps track of the current position on the input text field
i = 0

# Receives the digit as parameter and displays it on the input field
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

# Calculate function scans the string to evaluate and display it
def calculate():
    entire_string = display.get()
    try:
        # Use eval() for basic calculation (with caution for untrusted input)
        result = eval(entire_string)
        clear_all()
        display.insert(0, result)
    except Exception as e:
        clear_all()
        display.insert(0, "Error")
        print(f"Calculation error: {e}")

# Function which takes operator as input and displays it on the input field
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

# Function to clear the input field
def clear_all():
    display.delete(0, END)
    global i
    i = 0

# Function which works like backspace
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")

# Function to calculate the factorial and display it
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# -------------------------------------- UI Design ---------------------------------------------

# Adding the input field
display = Entry(root, width=25, borderwidth=5, font=('Arial', 16), bg=DISPLAY_COLOR, fg=DISPLAY_TEXT_COLOR)
display.grid(row=1, columnspan=6, padx=10, pady=10, sticky=N + E + W + S)

# Code to add buttons to the Calculator
button_params = {'padx': 20, 'pady': 15, 'bg': BUTTON_COLOR, 'fg': BUTTON_TEXT_COLOR, 'font': ('Arial', 12)}
operation_params = {'padx': 20, 'pady': 15, 'bg': OPERATION_COLOR, 'fg': BUTTON_TEXT_COLOR, 'font': ('Arial', 12)}
accent_params = {'padx': 20, 'pady': 15, 'bg': ACCENT_COLOR, 'fg': BUTTON_TEXT_COLOR, 'font': ('Arial', 12)}

Button(root, text="1", command=lambda: get_variables(1), **button_params).grid(row=2, column=0, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="2", command=lambda: get_variables(2), **button_params).grid(row=2, column=1, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="3", command=lambda: get_variables(3), **button_params).grid(row=2, column=2, sticky=N + S + E + W, padx=2, pady=2)

Button(root, text="4", command=lambda: get_variables(4), **button_params).grid(row=3, column=0, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="5", command=lambda: get_variables(5), **button_params).grid(row=3, column=1, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="6", command=lambda: get_variables(6), **button_params).grid(row=3, column=2, sticky=N + S + E + W, padx=2, pady=2)

Button(root, text="7", command=lambda: get_variables(7), **button_params).grid(row=4, column=0, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="8", command=lambda: get_variables(8), **button_params).grid(row=4, column=1, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="9", command=lambda: get_variables(9), **button_params).grid(row=4, column=2, sticky=N + S + E + W, padx=2, pady=2)

# Adding other buttons to the calculator
Button(root, text="AC", command=clear_all, **accent_params).grid(row=5, column=0, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="0", command=lambda: get_variables(0), **button_params).grid(row=5, column=1, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text=".", command=lambda: get_variables("."), **button_params).grid(row=5, column=2, sticky=N + S + E + W, padx=2, pady=2)

Button(root, text="+", command=lambda: get_operation("+"), **operation_params).grid(row=2, column=3, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="-", command=lambda: get_operation("-"), **operation_params).grid(row=3, column=3, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="*", command=lambda: get_operation("*"), **operation_params).grid(row=4, column=3, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="/", command=lambda: get_operation("/"), **operation_params).grid(row=5, column=3, sticky=N + S + E + W, padx=2, pady=2)

# Adding new operations
Button(root, text="π", command=lambda: get_operation("*3.14159"), **button_params).grid(row=2, column=4, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="%", command=lambda: get_operation("/100*"), **button_params).grid(row=3, column=4, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="(", command=lambda: get_operation("("), **button_params).grid(row=4, column=4, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="exp", command=lambda: get_operation("**"), **button_params).grid(row=5, column=4, sticky=N + S + E + W, padx=2, pady=2)

Button(root, text="<-", command=undo, **accent_params).grid(row=2, column=5, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="x!", command=fact, **accent_params).grid(row=3, column=5, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text=")", command=lambda: get_operation(")"), **button_params).grid(row=4, column=5, sticky=N + S + E + W, padx=2, pady=2)
Button(root, text="^2", command=lambda: get_operation("**2"), **button_params).grid(row=5, column=5, sticky=N + S + E + W, padx=2, pady=2)

Button(root, text="=", command=calculate, **accent_params).grid(row=6, columnspan=6, sticky=N + S + E + W, padx=10, pady=10)

# Configure row and column weights for resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()