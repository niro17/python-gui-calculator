import tkinter as tk 

#Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#1C1C1C")

equation = ""

#Function to update the equation on button press
def show(value):
    global equation
    if value == 'x':
        value = '*'
    elif value == '÷':
        value = '/'
    equation += value
    label_result.config(text=equation)

#Function to clear the equation
def clear():
    global equation
    equation = ""
    label_result.config(text="0")

#Function to evaluate the equation
def calculate():
    global equation
    try:
        result = str(eval(equation))
        equation = result
    except:
        result = "Error"
        equation = ""
    label_result.config(text=result)

#Function to toggle the sign of the equation
def toggle_sign():
    global equation
    if equation.startswith('-'):
        equation = equation[1:]
    else:
        equation = '-' + equation
    label_result.config(text=equation)

#Create a label to display the equation/result
label_result = tk.Label(root, width=18, height=2, text="0", font=("digital-7", 30), anchor="e", bg="#1C1C1C", fg="white")
label_result.pack(pady=(20, 0))

#Create a frame to hold the buttons
button_frame = tk.Frame(root, bg="#1C1C1C")
button_frame.pack(pady=10)

#Define the buttons and their layout
buttons = [
    'AC', '%', 'x', '÷',
    '7', '8', '9', '-',
    '4', '5', '6', '+',
    '1', '2', '3', '=',
    '0', '.', '+/-'
]

row_val = 0
col_val = 0

# Create and place buttons on the grid
for button in buttons:
    if button == '=':
        btn = tk.Button(button_frame, text=button, width=5, height=3, font=("Arial", 14, "bold"), bg="#FF9500", fg="white", command=calculate)
        btn.grid(row=row_val, column=col_val, rowspan=2, sticky="nsew")
    elif button == 'AC':
        btn = tk.Button(button_frame, text=button, width=5, height=2, font=("Arial", 14, "bold"), bg="#FF9500", fg="white", command=clear)
        btn.grid(row=row_val, column=col_val, sticky="nsew")
    elif button == '+/-':
        btn = tk.Button(button_frame, text=button, width=5, height=2, font=("Arial", 14, "bold"), bg="#D4D4D2", fg="black", command=toggle_sign)
        btn.grid(row=row_val, column=col_val, sticky="nsew")
    else:
        btn = tk.Button(button_frame, text=button, width=5, height=2, font=("Arial", 14, "bold"), bg="#D4D4D2" if button in ['%', 'x', '÷', '-', '+'] else "#505050", fg="black" if button in ['%', 'x', '÷', '-', '+'] else "white", command=lambda x=button: show(x))
        btn.grid(row=row_val, column=col_val, sticky="nsew")

#Move to the next column
    col_val += 1

#If the column value exceeds 3, reset column value and move to the next row
    if col_val > 3:
        col_val = 0
        row_val += 1

#Configure grid weights for uniform button sizing
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

# Start the main event loop
root.mainloop()
