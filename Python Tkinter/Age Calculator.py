import tkinter as tk
from datetime import datetime

def calculate_age():
    birth_date_str = entry_birth_date.get()
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        label_result.config(text=f"Your age is {age} years.")
    except ValueError:
        label_result.config(text="Please enter a valid date (YYYY-MM-DD).")

# Create the main window
window = tk.Tk()
window.title("Age Calculator App")

# Create and place widgets
label_instructions = tk.Label(window, text="Enter your birthdate (YYYY-MM-DD):")
label_instructions.pack(pady=10)

entry_birth_date = tk.Entry(window)
entry_birth_date.pack(pady=10)

btn_calculate = tk.Button(window, text="Calculate Age", command=calculate_age)
btn_calculate.pack(pady=10)

label_result = tk.Label(window, text="")
label_result.pack(pady=10)

# Start the main loop
window.mainloop()
